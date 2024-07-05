l = input().split(',')
k = int(input())
for i in range(1,k+1):
  last = l.pop()
  l.insert(0, last)
print(",".join([str(i) for i in l]), end = '')