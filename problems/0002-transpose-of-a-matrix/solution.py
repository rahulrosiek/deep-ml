def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    result = []
    length_row = len(a[0])
    for k in range(length_row):
        result.append([])
    for v in a:
        for j in range(length_row):
            result[j].append(v[j])
    return result