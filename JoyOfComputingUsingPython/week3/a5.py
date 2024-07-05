numbers = []
n = int(input("Enter the no of elements: "))
for i in range (n):
    num = int(input("Enter number " + str(i + 1) + " : "))
    numbers.append(num)
result = sum(numbers)
average = result / n
print("Sum : ", result)
print("Average : ", average)