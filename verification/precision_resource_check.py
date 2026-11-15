"""Reproducible finite checks for the traversal precision/resource budget.

Generates one64-vertex simple degree-six graph, applies continuous positive
odd-site disorder, and evaluates time averages spectrally. No compiled sparse
simulation or asymptotic classical-hardness certificate is claimed.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


def parameters(n: int, failure: float = 1/3) -> dict:
    k=2*n+1
    z=(3*k+7)/5
    moment=5*2*k/24+2  # v=1,W=2
    horizon=2.**math.ceil(math.log2(4*z*moment))
    norm_bound=8.
    q=math.ceil(math.log2(4*norm_bound*horizon*z))
    grid_size=2**q
    value_error=min(.5,1/(64*z*z*horizon))
    fractional_bits=math.ceil(math.log2(1/value_error))
    simulation_error=1/(64*z*z)
    restart_count=math.ceil(16*z*z*math.log(1/failure))
    conservative_success=1/(16*z*z)
    grid_amplitude_error=norm_bound*horizon/(2*grid_size)
    post_grid_probability=(1/(2*z)-grid_amplitude_error)**2
    post_errors=post_grid_probability-2/(64*z*z)
    assert grid_amplitude_error<=1/(8*z)+1e-15
    assert post_errors>=conservative_success
    assert math.exp(-conservative_success*restart_count)<=failure*(1+1e-14)
    return {'n':n,'k':k,'vertex_count':20*4**n-16,'Z':z,
            'uniform_moment_bound':moment,'dyadic_horizon':horizon,
            'grid_bits':q,'grid_size':grid_size,
            'sufficient_potential_fractional_bits':fractional_bits,
            'value_error_budget':value_error,
            'per_run_simulation_diamond_error':simulation_error,
            'restart_count':restart_count,'failure_target':failure,
            'conservative_per_run_success':conservative_success,
            'post_grid_and_error_lower_bound':post_errors,
            'failure_exponential_upper_bound':math.exp(-conservative_success*restart_count)}


def generate_graph():
    rng=np.random.default_rng(15112026)
    sizes=[1,6,15,20,15,6,1]
    left=[6,5,4,3,2,1]
    right=[1,2,3,4,5,6]
    starts=np.cumsum([0]+sizes)
    count=int(starts[-1])
    adjacency=np.zeros((count,count))
    for j,(degree_left,degree_right) in enumerate(zip(left,right)):
        us=np.repeat(np.arange(sizes[j]),degree_left)
        vs=np.repeat(np.arange(sizes[j+1]),degree_right)
        assert len(us)==len(vs)
        for attempt in range(100000):
            pairs=list(zip(us.tolist(),rng.permutation(vs).tolist()))
            if len(set(pairs))==len(pairs):break
        else:raise RuntimeError('simple biregular configuration sampler exhausted')
        for u,v in pairs:
            a=int(starts[j]+u);b=int(starts[j+1]+v)
            adjacency[a,b]=adjacency[b,a]=1
    assert np.all(np.diag(adjacency)==0)
    assert np.all(adjacency.sum(axis=1)==6)
    potential=np.zeros(count)
    for j in (1,3,5):
        potential[starts[j]:starts[j+1]]=rng.uniform(1,2,sizes[j])
    return adjacency,potential


def spectral_data(h):
    eig,vec=np.linalg.eigh(h)
    coefficients=vec[-1,:]*vec[0,:]
    return eig,coefficients


def continuous_filter(frequencies,horizon):
    return np.exp(-.5j*frequencies*horizon)*np.sinc(frequencies*horizon/(2*np.pi))


def grid_filter(frequencies,horizon,grid_size):
    step=horizon/grid_size
    return (np.exp(-.5j*frequencies*step*(grid_size-1))
            *np.sinc(frequencies*horizon/(2*np.pi))
            /np.sinc(frequencies*step/(2*np.pi)))


def averaged_probability(eig,coefficients,horizon,grid_size=None):
    differences=eig[:,None]-eig[None,:]
    filt=(continuous_filter(differences,horizon) if grid_size is None
          else grid_filter(differences,horizon,grid_size))
    value=np.sum(coefficients[:,None]*coefficients[None,:]*filt)
    assert abs(value.imag)<1e-10
    return float(value.real)


def finite_precision_check():
    par=parameters(1)
    adjacency,potential=generate_graph()
    h=adjacency+np.diag(potential)
    eig,c=spectral_data(h)
    t=par['dyadic_horizon'];m=par['grid_size'];z=par['Z']
    avg_c=np.sum(c*continuous_filter(eig,t))
    avg_g=np.sum(c*grid_filter(eig,t,m))
    gap=abs(avg_c-avg_g)
    grid_error_bound=8*t/(2*m)
    assert gap<=grid_error_bound+1e-12
    continuous_probability=averaged_probability(eig,c,t)
    grid_probability=averaged_probability(eig,c,t,m)
    bits=par['sufficient_potential_fractional_bits']
    rounded=np.round(potential*2**bits)/2**bits
    assert np.all(rounded[potential==0]==0)
    maximum_value_error=float(np.max(abs(rounded-potential)))
    assert maximum_value_error<=par['value_error_budget']
    eig_r,c_r=spectral_data(adjacency+np.diag(rounded))
    rounded_probability=averaged_probability(eig_r,c_r,t,m)
    assert abs(rounded_probability-grid_probability)<=t*maximum_value_error+1e-10
    implemented_lower=rounded_probability-par['per_run_simulation_diamond_error']
    assert implemented_lower>=par['conservative_per_run_success']
    return {'parameters':par,'degree_min':float(adjacency.sum(axis=1).min()),
            'degree_max':float(adjacency.sum(axis=1).max()),
            'potential_fractional_bits':bits,'maximum_value_rounding_error':maximum_value_error,
            'continuous_average_amplitude':[float(avg_c.real),float(avg_c.imag)],
            'grid_average_amplitude':[float(avg_g.real),float(avg_g.imag)],
            'amplitude_grid_difference':float(gap),'amplitude_grid_error_bound':grid_error_bound,
            'continuous_average_probability':continuous_probability,
            'grid_average_probability':grid_probability,
            'rounded_H_grid_average_probability':rounded_probability,
            'probability_rounding_difference':abs(rounded_probability-grid_probability),
            'Duhamel_probability_upper_bound':t*maximum_value_error,
            'implemented_probability_lower_after_channel_error':implemented_lower}


def signed_boundary():
    rows=[]
    for small in (.1,.01,.001,.0001):
        b=np.array([[1.,0.],[1.,0.],[0.,small]])
        v=np.array([[0.,1.],[1.,0.]])
        h=np.block([[np.zeros((3,3)),b],[b.T,v]])
        eig,u=np.linalg.eigh(h)
        nonzero=abs(eig)>1e-10
        moment=float(np.sum(u[0,nonzero]**2/abs(eig[nonzero])))
        rows.append({'small_coupling':small,'local_absolute_inverse_moment':moment,
                     'scaled_moment':small*moment,
                     'predicted_limit':1/math.sqrt(24)})
    assert abs(rows[-1]['scaled_moment']-1/math.sqrt(24))<1e-4
    return rows


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result={'passed':True,'analytic_parameter_checks':[
        parameters(n,failure) for n in (1,2,4,8,16) for failure in (1/3,1e-6)],
        'finite_precision':finite_precision_check(),'signed_boundary':signed_boundary(),
        'scope':'Finite spectral/precision checks, not sparse-circuit execution, asymptotic classical-hardness proof, physical implementation or novelty certificate.'}
    text=json.dumps(result,indent=2)
    if args.output:args.output.write_text(text+'\n')
    print(text)


if __name__=='__main__':main()
