import numpy as np

def gaussian_elimination(A, b):
	"""
	Solves the system Ax = b using Gaussian Elimination with partial pivoting.
    
	:param A: Coefficient matrix
	:param b: Right-hand side vector
	:return: Solution vector x
	"""
	result = []
	for k in range(len(A) -1):
		pivot_row = k + np.argmax(np.abs(A[k:, k]))
		A[[k, pivot_row]] = A[[pivot_row, k]]
		b[[k, pivot_row]] = b[[pivot_row, k]]
		pivot = A[k, k]
		for j in range(1, len(A) - k):
			factor = A[k+j, k] / pivot
			A[k+j] -= factor  * A[k]
			b[k+j] -= factor  * b[k]
	for i in range(len(A)):
		for l in range(1, i+1):
			b[-i-1] -= A[-i-1, -l] * result[-l]
		x_value = b[-i-1] / A[-i-1, -i-1]
		result.insert(0,float(x_value))
	return result

