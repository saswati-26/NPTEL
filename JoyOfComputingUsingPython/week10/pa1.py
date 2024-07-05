def rotate(mat):
    rotated_mat=[]
    c=len(mat[0])
    r=len(mat)
    for i in range(0,c):
      li=[]
      for j in range(r-1,-1,-1):
        li=li+[mat[j][i]]
      rotated_mat=rotated_mat+[li] 
    return(rotated_mat)

mat = input()
print(rotate(mat))