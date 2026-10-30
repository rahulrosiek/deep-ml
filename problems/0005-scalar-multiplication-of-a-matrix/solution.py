def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			element = matrix[i][j]
			matrix[i][j] = element * scalar
	return matrix