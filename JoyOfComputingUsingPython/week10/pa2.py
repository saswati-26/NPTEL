def is_magic(matrix):
    value=0
    for i in range(0,len(matrix)):
      value+= matrix[0][i]
    for i in range(0,len(matrix)):
      total = 0
      for j in range(0,len(matrix)):
        total+=matrix[i][j]
      if total != value:
        return('NO')
    for j in range(0,len(matrix)):
      total = 0
      for i in range(0,len(matrix)):
        total+=matrix[i][j]
      if total != value:
        return('NO')
    total = 0
    for i in range(0,len(matrix)):
      for j in range(0,len(matrix)):
        if i==j:
          total+=matrix[i][j]
    if total != value:
      return('NO')
    return('YES')

matix = input()
print(is_magic(matix))