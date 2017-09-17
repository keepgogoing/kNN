import numpy as np
from numpy import *
import operator
import  matplotlib.pyplot as plt

X=np.linspace(-np.pi,np.pi,256,endpoint=True)
(C,S) = np.cos(X),np.sin(X)
fig = plt.figure(figsize=(10,6),dpi=80)
plt.plot(X,C,'b-',lw=2.5)
plt.plot(X,C,'r-',lw=2.5)
print()




