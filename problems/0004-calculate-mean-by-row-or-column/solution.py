def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	if mode == "row":
		for i in matrix:
			means.append(sum(i)/len(i))
	elif mode == "column":
		for i in range (len(matrix[0])):
			som = 0
			for j in range (len(matrix)):
				som +=	matrix[j][i]
			means.append(som/len(matrix))
	return means
	