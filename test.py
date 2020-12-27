import numpy as np 
from qutip import *
import matplotlib.pyplot as plt 
listx = []
listt = []
listy = [] 
w = 1.076*10**9
copconst = 0.03
spinz = jmat(1,'z')
spinp = jmat(1,'+')
spinm = jmat(1,'-')
spinx = jmat(1,'x')
spiny = jmat(1,'y')
for i in range(164):
    H2= np.sin(w*i)*copconst*(spinx*spiny + spiny*spinx)
    H3 =np.sin(w*i)*copconst*(spinx**2 - spiny**2)
    H = H3 + H2 
    x,y = np.linalg.eig(H)
    listx.append(x)
    listy.append(y)
    listt.append(i)
plt.plot(listt,listx)
plt.show()
print(listy)
