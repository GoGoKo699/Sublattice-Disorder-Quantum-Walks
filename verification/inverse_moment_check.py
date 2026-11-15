"""Finite check of inverse-moment bound after quotient symmetry breaks.

Dense synthetic matrices test the theorem, not graph-oracle hardness or sparse
implementation. Tiny singular directions give a vanishing global gap while
source pseudoinverse norms stay controlled. Floating-point diagnostics only.
"""
import json
import numpy as np
from scipy.linalg import block_diag, null_space

rng=np.random.default_rng(151126)
m=6
r=4
alpha=2.
b0=np.zeros((m+1,m))
for j in range(m):b0[j,j]=b0[j+1,j]=alpha
q,_=np.linalg.qr(rng.normal(size=(m+r,m+r)))
vdiag=1+rng.random(m+r)
v=np.diag(vdiag)
s=np.zeros(m+1+r);s[0]=1
t=np.zeros_like(s);t[m]=1
z=np.zeros_like(s);z[:m+1]=(-1.)**np.arange(m+1)/np.sqrt(m+1)
p0=np.outer(z,z)
records=[]
for tiny in (1e-2,1e-3,1e-4,1e-5):
    b=block_diag(b0,tiny*np.eye(r))@q.T
    h=np.block([[np.zeros((len(s),len(s))),b],[b.T,v]])
    ss=np.r_[s,np.zeros(m+r)];tt=np.r_[t,np.zeros(m+r)]
    zz=np.r_[z,np.zeros(m+r)]
    # Remove the known exact kernel before diagonalizing. Otherwise roundoff
    # rotates it into tiny nonzero modes and corrupts inverse moments.
    complement=null_space(zz[None,:])
    eig,ured=np.linalg.eigh(complement.T@h@complement)
    u=complement@ured
    c_s=u.T@ss;c_t=u.T@tt
    nz=np.abs(eig)>1e-13
    invabs=np.zeros_like(eig);invabs[nz]=1/np.abs(eig[nz])
    invsigned=np.zeros_like(eig);invsigned[nz]=1/eig[nz]
    ms=float(np.sum(c_s*c_s*invabs))
    mt=float(np.sum(c_t*c_t*invabs))
    ys=np.linalg.lstsq(b,s-p0@s,rcond=None)[0]
    yt=np.linalg.lstsq(b,t-p0@t,rcond=None)[0]
    es=float(ys@v@ys)
    signed=float(np.sum(c_s*c_s*invsigned))
    bound_s=float(2*np.dot(ys,ys)+2.)
    bound_t=float(2*np.dot(yt,yt)+2.)
    horizon=4*(m+1)*max(bound_s,bound_t)
    ff=np.ones_like(eig,dtype=complex)
    ff[nz]=np.expm1(-1j*eig[nz]*horizon)/(-1j*eig[nz]*horizon)
    zeroval=float(t@p0@s)
    amplitude=zeroval+np.sum(c_t*c_s*ff)
    avg_error=abs(amplitude-zeroval)
    inv_bound=2*np.sqrt(ms*mt)/horizon
    records.append({'tiny_singular_scale':tiny,
      'minimum_nonzero_eigenvalue':float(np.min(np.abs(eig[nz]))),
      'inverse_moment_source':ms,'inverse_moment_target':mt,
      'source_upper_bound':bound_s,'target_upper_bound':bound_t,
      'signed_inverse_plus_constrained_energy_residual':abs(signed+es),
      'zero_projector_amplitude':zeroval,
      'time_average_amplitude_error':float(avg_error),
      'inverse_moment_error_upper_bound':float(inv_bound),
      'horizon':horizon})
    assert ms<=bound_s+1e-6 and mt<=bound_t+1e-6
    assert avg_error<=inv_bound+1e-8
    assert abs(signed+es)<2e-5
print(json.dumps({'passed':True,'records':records,
 'scope':'Finite dense non-quotient-invariant V diagnostics; no graph generation or classical-hardness certificate.'},indent=2))
