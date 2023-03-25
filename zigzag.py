import numpy as np

def traverse(matrix):
    # initialize variables
    n = len(matrix)
    m = len(matrix[0])
    result = []
    i, j = 0, 0
    # traverse matrix in zigzag pattern
    for k in range(n * m):
        result.append(matrix[i][j])
        if (i + j) % 2 == 0:  # moving up
            if j == m - 1:
                i += 1
            elif i == 0:
                j += 1
            else:
                i -= 1
                j += 1
        else:  # moving down
            if i == n - 1:
                j += 1
            elif j == 0:
                i += 1
            else:
                i += 1
                j -= 1
    return result

