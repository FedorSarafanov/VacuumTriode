import numpy as np 
from matplotlib import pyplot as plt 
from scipy import interpolate

A=np.genfromtxt('s_uc.tsv',delimiter='\t',skip_header=1)
uc1=A.T[0]
S=A.T[1]

ss = interpolate.interp1d(uc1,S)

A=np.genfromtxt('r_uc.tsv',delimiter='\t',skip_header=1)
r=A.T[0]
uc2=A.T[1]

rr = interpolate.interp1d(uc2,r)

mu=np.array(ss(uc1)*rr(uc1))

for i in range(0,len(mu)):
	print(str(uc1[i])+'\t'+str(mu[i]*1000))
plt.plot(uc1,mu)
plt.show()
