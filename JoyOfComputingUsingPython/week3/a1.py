elements = []
n = int(input("Enter no of elements: "))
for i in range (n):
    item = input("Enter element " + str(i + 1) + ": ")
    elements.append(item)
print("The entered elements are: ", elements)