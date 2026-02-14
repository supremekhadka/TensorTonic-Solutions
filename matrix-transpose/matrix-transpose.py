import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    rows = len(A)
    cols = len(A[0])
    
    A_t = [[0 for i in range(rows)] for i in range(cols)]
    
    for i in range(rows):
      for j in range(cols):
        A_t[j][i] = A[i][j]
    
    return np.array(A_t)
  


    
    
        


