import numpy as np

X = np.array([[2, -3, -1],
			  [3, 2, -5],
			  [2, 4, -1]])
Y = np.array([3, -9, -5])

n = len(X)
for y in range(0, n - 1):
    for x in range(y + 1, n):
        sum = X[x, y] / X[y, y]
        X[x, y + 1:n] = X[x, y + 1:n] - sum * X[y, y + 1:n]
        X[x, y] = sum

n = len(X)
for k in range(1, n):
    Y[k] = Y[k] - np.dot(X[k, 0:k], Y[0:k])
Y[n - 1] = Y[n - 1] / X[n - 1, n - 1]
for k in range(n - 2, -1, -1):
    Y[k] = (Y[k] - np.dot(X[k, k + 1:n], Y[k + 1:n])) / X[k, k]


print(Y)
