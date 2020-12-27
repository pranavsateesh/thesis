from qutip import *
import numpy as np
from numpy import pi
import cmath
import matplotlib.pyplot as plt

spinz = jmat(1,'z')
spinp = jmat(1,'+')
spinm = jmat(1,'-')
spinx = jmat(1,'x')
spiny = jmat(1,'y')
d = 2.87
gamma = 2.8
copconst = 0.03
bz  = 0.01
psi0 = basis(3,1)
listx =[]
listy =[]
listz =[]
listt =[]
c_op_list = []
options = Options()
options.nsteps = 5000
t = np.linspace(0,100,10000)
#H0 = d*spinz**2
#H1 = gamma*(1)*spinz
H2 = copconst*(spinx*spiny + spiny*spinx)
H3 = copconst*(spinx**2 - spiny**2)
w = 1.076*10**9
def H2_Coef(t,args):
    return np.sin(w*t)
H = [[H2,H2_Coef],[H3,H2_Coef]]
print(H[1])
output = mesolve(H, psi0, t, c_op_list,[spinx,spiny,spinz], options=options)
sx = output.expect[0]
sy = output.expect[1]
sz = output.expect[2]
plt.plot(t,sx)
plt.plot(t,sy)
plt.plot(t,sz)
plt.show()
