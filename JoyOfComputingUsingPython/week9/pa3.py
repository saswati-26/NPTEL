def power(A, m):
    if m == 1:
      return A
    else:
      n = len(A)
      B = power(A,m-1)
      C = []
      for i in range(n):
        row = []
        for j in range(n):
          sum = 0
          for k in range(n):
            sum += int(A[i][k]) * int(B[k][j])
          row.append(sum)
        C.append(row)
      return C
    

n = int(input())
m = int(input())
A = []
for i in range(n):
    row_input = input()
    row_elements = row_input.split(',')
    row = [int(elem) for elem in row_elements]
    A.append(row)

result = power(A , m)

for row in result:
    print(','.join(map(str, row)),end="\n")