import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	result = []
	if len(a) * len(a[0]) != new_shape[0] * new_shape[1]:
		return result
	array = np.array(a).flatten().tolist()
	j = 0
	for i in range(new_shape[0]):
		row = array[j:j+new_shape[1]]
		result.append(row)
		j += new_shape[1]
	return result