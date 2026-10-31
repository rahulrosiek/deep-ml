import numpy as np
def lu_decomposition(A: list) -> tuple:
    """
    Perform LU decomposition on a square matrix using Doolittle's method.

    Args:
        A: Square matrix as a list of lists

    Returns:
        tuple: (L, U) where L is lower triangular with 1s on diagonal,
               U is upper triangular, and A = L @ U
    """
    U = np.array(A, dtype=float)
    L = np.eye(len(A))
    for i in range(len(A)-1):
        pivot = U[i,i]
        for k in range(1, len(A) - i):
            factor = U[k+i, i] / pivot
            U[i+k] -= factor  * U[i]
            L[i+k,i] = factor
    return(L,U)
		
		
	