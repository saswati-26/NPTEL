password = input()
if len(password) >= 8 and len(password) <= 32 and password[0].isalpha() and '/' not in password and '\\' not in password and '=' not in password and "'" not in password and '"' not in password and ' ' not in password :
    print ("TRUE" , end = '')
else: 
    print("FALSE")