import numpy as np

def cholesky(a):
	a=np.array(a,float)
	L=np.zeros_like(a)
	n,_ = np.shape(a)
	for j in range(n):
		for i in range(j,n):
			if i == j:
				L[i,j] = np.sqrt(a[i,j]-np.sum(L[i,:j]**2))

			else:					
				L[i,j] = (a[i,j]-np.sum(L[i,:j]*L[j,:j])) /L[j,j]
	return L


A = [[1,1,1],
	 [1,2,2],
	 [1,2,3]]

L = cholesky(A)

print(L)