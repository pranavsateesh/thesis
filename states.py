file = open("test.txt", 'w')
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
gamma = 28024.951 
copconst = 0.03
bz  = 0.01 
listx =[]
listy =[]
listz =[]
listt =[]
psi0 = basis(3,1)
sigmax = 10000000
sigmay = 10000000
options = Options()
options.nsteps = 5000
t = np.linspace(0,0.000000001,10000)
c_op_list = []
H0 = d*spinz**2 
H1 = gamma*bz*spinz 
H2 = copconst*(spinx*spiny + spiny*spinx)
H3 = copconst*(spinx**2 + spiny**2)
g    = 2   #g constant
me = 9.1*(10**(-31))  #mass of an electron
e = 1.6*(10**(-19))   #charge of an electron
theta = 0.2 * pi       # qubit angle from sigma_z axis (toward sigma_x axis)
gamma1 = 0.0     # qubit relaxation rate
gamma2 = 0.0     # qubit dephasing rate
h = 1.054*(10**(-34))
Bx = 0.01
gmr = 28024.951 #gyromagnetic ratio in Mhz/T 
omega = gmr * Bx * (10 ** (-6))/ pi
def H2_Coeff(t,args):
    return 10*t
H = [H0,H1,[H2,H2_Coeff],[H3, H2_Coeff]]
output = mesolve(H, psi0, t, c_op_list,[spinx,spiny,spinz], options=options)
sx = output.expect[0]
sy = output.expect[1]
sz = output.expect[2]
plt.plot(t,sx)
plt.plot(t,sy)
plt.plot(t,sz)
plt.show()
