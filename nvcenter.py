import matplotlib.pyplot as plt

import numpy as np

from numpy import linalg as LA

blist = []
clist = []
dlist = []
elist = []
flist = []
glist = []
hlist = []
hc = 1.545*(10**-34)
Bx = 0
By = 0
Bz = 0.1
B  =  np.matrix([[Bx,0,0],[0,By,0],[0,0,Bz]])
Ex = 0
Ey = 0
Ez = 0
sx = np.matrix([[0,(1/(2**(1/2))),0],[(1/(2**(1/2))),0,(1/(2**(1/2)))],[0,(1/(2**(1/2))),0]]) 
sy = np.matrix([[0,-1j*(1/(2**(1/2))),0],[1j*(1/(2**(1/2))),0,-1j*(1/(2**(1/2)))],[0,1j*(1/(2**(1/2))),0]])
sz = np.matrix([[(1),0,0],[0,0,0],[0,0,(-1)]])
I  = np.matrix([[2/3,0,0],[0,2/3,0],[0,0,2/3]])

gm = 28*(10**9)
d  = 2.87*(10**9)
ez = 0.17
exy= 3*(10**-3)
for Bz in range(0,100000,1):
	m = (((d*((sz**2)-I))) + (gm*((Bx*sx)+(By*sy)+((Bz/100000.0)*sz)) + (ez*Ez*((sz**2)-(I))) + (exy*((Ex*((sx*sy)+(sy*sx)))+(Ey*((sx**2)+(sy**2)))))))
	w,v=LA.eig(m)
	a = w.ravel()
	flist.append(Bz/10000.0)
        #print(flist) 	

	for i in range (0,3,1):
		blist.append(a[i])

 

for j in range(0,len(blist),3):
	clist.append(blist[j])


for j in range(1,len(blist),3):
	dlist.append(blist[j])


for j in range(2,len(blist),3):
	elist.append(blist[j])



glist = abs(np.array(clist)-np.array(dlist))
hlist= abs(np.array(elist)-np.array(dlist))    
Ghzlist1 = np.array(glist)/(10**9)
Ghzlist2 = np.array(hlist)/(10**9)
mTlist  = np.array(flist)*(10**2)


plt.plot(mTlist,Ghzlist1)
plt.plot(mTlist,Ghzlist2)


#print(mTlist)
plt.title("Difference between +1,0 and -1,0 states")
plt.xlabel("Magnetic field in mT units")
plt.ylabel("Frequency in Ghz units")
plt.legend(["+1 state - 0 state","-1 state - 0 state"])
plt.show()

#plt.plot(mTlist,clist)
#plt.plot(mTlist,dlist)
#plt.plot(mTlist,elist)
#plt.legend(["+1 state","0 state","-1 state"])
#plt.xlabel("Magnetic field in mT units")
#plt.ylabel("Relative level in Hz")
#plt.show()
