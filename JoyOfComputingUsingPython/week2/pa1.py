m = int(input())
n = int(input())
if m < n:
    result = m
else:
    while m >= n:
        m -= n
    result = m
print(result, end = '')