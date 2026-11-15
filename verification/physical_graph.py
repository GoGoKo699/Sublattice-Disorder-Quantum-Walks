"""Finite full-graph diagnostic for microscopic sublattice disorder.

Run from any directory. Prints JSON; uses a seeded simple-biregular sampler.
This small explicit matrix is a verification specimen, not an exponentially
large instance used as a free input to the oracle algorithm.
"""
import numpy as np
import json
rng=np.random.default_rng(261115)
n=2
# Every tuple is (name,size,parity). k=5 odd layers for n=2.
layers=[('E0',1,0),('O0',6,1),('E1',15,0),('O1',30,1),('E2',60,0),('Oc',80,1),('E2r',60,0),('O1r',30,1),('E1r',15,0),('O0r',6,1),('Eexit',1,0)]
left_degrees=[6,5,4,4,4,3,2,2,2,1]
right_degrees=[1,2,2,2,3,4,4,4,5,6]
starts=np.cumsum([0]+[s for _,s,_ in layers]); N=int(starts[-1])
A=np.zeros((N,N))
rejections=[]
for i,(du,dv) in enumerate(zip(left_degrees,right_degrees)):
 nu,nv=layers[i][1],layers[i+1][1]
 assert nu*du==nv*dv
 us=np.repeat(np.arange(nu),du)
 vs=np.repeat(np.arange(nv),dv)
 for trial in range(100000):
  shuffled=rng.permutation(vs)
  pairs=list(zip(us.tolist(),shuffled.tolist()))
  if len(set(pairs))==len(pairs): break
 else: raise RuntimeError('simple configuration sampler exhausted')
 rejections.append(trial)
 for u,v in pairs:
  a,b=starts[i]+u,starts[i+1]+v
  A[a,b]=A[b,a]=1
assert np.all(A.sum(axis=1)==6)
U=np.zeros((N,len(layers)))
parity=np.zeros(N,dtype=int)
for i,(_,s,p) in enumerate(layers):
 U[starts[i]:starts[i+1],i]=1/np.sqrt(s)
 parity[starts[i]:starts[i+1]]=p
V=np.zeros(N)
V[parity==1]=rng.integers(1,3,size=int(np.sum(parity==1)))
H=A+np.diag(V)
q=U.T@A@U
base_res=np.linalg.norm(A@U-U@q)
disorder_res=np.linalg.norm(H@U-U@(U.T@H@U))
inds_even=np.flatnonzero(parity==0);inds_odd=np.flatnonzero(parity==1)
B=A[np.ix_(inds_even,inds_odd)]
start=0; end=N-1
vals,vecs=np.linalg.eigh(H)
zero=np.abs(vals)<1e-9
P0=vecs[:,zero]@vecs[:,zero].T
Bplus=np.linalg.pinv(B,rcond=1e-12)
S=[];M=[];bounds=[]
for e in [start,end]:
 u=np.eye(N)[:,e];s=u-P0@u
 y=Bplus@s[inds_even]
 M_e=np.sum((vecs[:,~zero].T@u)**2/np.abs(vals[~zero]))
 bound=2*np.dot(y,y)+2*np.dot(s,s)
 S.append(float(np.dot(y,y)));M.append(float(M_e));bounds.append(float(bound))
 assert M_e<bound+1e-9
k=(len(layers)-1)//2; Z=2+(k-1)*3/5
assert abs(abs(P0[end,start])-1/Z)<1e-9
Mbar=5*2*k/24+2
T=4*Z*Mbar
factors=np.ones_like(vals,dtype=complex)
factors[~zero]=(1-np.exp(-1j*vals[~zero]*T))/(1j*vals[~zero]*T)
avg_amp=np.dot(vecs[end,:]*vecs[start,:],factors)
rem=abs(avg_amp-P0[end,start]);rem_bound=2*np.sqrt(M[0]*M[1])/T
assert rem<=rem_bound+1e-10
result={'N':N,'layers':[{'name':name,'size':size,'parity':p} for name,size,p in layers],'degree_min':float(A.sum(axis=1).min()),'degree_max':float(A.sum(axis=1).max()),'simple_configuration_rejections':rejections,'base_equitable_residual':float(base_res),'disordered_equitable_residual':float(disorder_res),'kernel_dimension':int(sum(zero)),'endpoint_zero_projector':float(P0[end,start]),'predicted_absolute_projector':1/Z,'endpoint_Bplus_norm_squared':S,'endpoint_absolute_inverse_moment':M,'moment_bound_using_actual_Bplus':bounds,'uniform_Mbar':Mbar,'T':T,'average_transition_amplitude_real':float(avg_amp.real),'average_transition_amplitude_imag':float(avg_amp.imag),'actual_nonzero_remainder':float(rem),'analytical_nonzero_remainder_bound':float(rem_bound),'jensen_success_lower_from_actual_average':float(abs(avg_amp)**2),'guaranteed_success_lower':1/(4*Z**2),'scope':'One finite random simple degree-six graph, iid binary odd-site potentials. Floating point verifies model and identities only, not asymptotic hardness or novelty.'}
print(json.dumps(result,indent=2))
