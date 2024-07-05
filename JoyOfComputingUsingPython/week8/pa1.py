def MyFn(s):
    return s[0]
A = []
for i in range(0,8):
  A = A + input().split("\n")
  A[i] = A[i].split(",")
A = sorted(A,key=MyFn)
A = sorted(A,key=len, reverse=True)
dict = {}
for i in range(0,8):
  dict[A[i][0]] =len(A[i])-1
for key, value in dict.items():
    print(f'{key}:{value}')