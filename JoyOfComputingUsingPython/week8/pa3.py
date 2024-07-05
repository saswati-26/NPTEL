def two_level_sort(scores):
  for i in range(len(scores)):
    for j in range(0,len(scores)-i-1):
      if(scores[j][0]>scores[j+1][0]):
        tmp = scores[j]
        scores[j] = scores[j+1]
        scores[j+1] = tmp
  for i in range(len(scores)):
    for j in range(0,len(scores)-i-1):
      if(scores[j][1]>scores[j+1][1]):
        tmp = scores[j]
        scores[j] = scores[j+1]
        scores[j+1] = tmp  
  return(scores)