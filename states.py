from qutip import *
import numpy
spin = basis(3,0)
ham = [[0,0,0],[0,2,1],[0,1,2]]
print(numpy.dot(ham,spin))