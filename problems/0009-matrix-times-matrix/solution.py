def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    result = []
    if len(a[0]) != len(b):
        return -1
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            som = 0
            for k in range(len(b)):
                som += a[i][k] * b[k][j]
            row.append(som)
        result.append(row)
    return result

        
        
