def minor_matrix(M, i, j):
    del M[i]
    for m in range(len(M)):
      del M[m][j]
    return(M)