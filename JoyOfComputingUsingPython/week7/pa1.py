column_label = input()
column_number = 0
for i in range(len(column_label)):
    column_number += (ord(column_label[ - (i + 1)]) - 64) * (26 ** i)
print(column_number , end='')