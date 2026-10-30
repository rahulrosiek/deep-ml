def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	result = []
	if len(a[0]) != len(b):
		return -1
	for i in a:
		j = 0
		sum = 0
		while j != len(b):
			sum += i[j] * b[j]
			j+=1
		result.append(sum)
	return result
