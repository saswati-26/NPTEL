num = int(input("Enter a number: "))
want_to_continue = 'y' or 'Y'
while want_to_continue == 'y' or want_to_continue == 'Y':
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz") 
    elif num % 3 == 0:
        print("Fizz")
    elif num % 3 != 0 and num % 5 != 0:
        print(num)
    else:
        print("Invalid")
    want_to_continue = input("Do you want to continue(y/n)?: ")
    num = int(input("Enter a number: "))