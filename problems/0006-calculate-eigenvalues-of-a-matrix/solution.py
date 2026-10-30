import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	eigenvalues = []
	b = -1 * (matrix[0][0] + matrix [1][1])
	c = matrix[0][0] * matrix [1][1] - matrix[0][1] * matrix [1][0]
	D = b*b - 4*c
	eigenvalue1 = (-1* b + math.sqrt(D))/2
	eigenvalue2 = (-1 * b - math.sqrt(D))/2
	eigenvalues.append(eigenvalue1)
	eigenvalues.append(eigenvalue2)
	return sorted(eigenvalues, reverse=True)