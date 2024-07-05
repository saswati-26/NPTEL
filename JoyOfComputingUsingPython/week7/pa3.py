s = input()
S = ''
for i in range (len(s)):
    S += chr(219 - ord(s[i]))
print(S, end='')