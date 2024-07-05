words = input().split(",")

print("words: ", words)

real_dict = {}
k = list("abcdefghijklmnopqrstuvwxyz")
for w in words:
  if w[0] not in real_dict :
    real_dict[w[0]] = [w]
  else :
    real_dict[w[0]].append(w)
    
print(real_dict)