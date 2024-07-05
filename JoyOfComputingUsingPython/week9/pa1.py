def balanced(word):
    """
    Determine if a string is balanced
    Argument:
        word: string
    Return:
        result: bool
    """
    Braces, Brackets, Parentheses = 0, 0, 0
    if word[0] == '{':
      Braces+=1
    elif word[0] == '[':
      Brackets+=1
    elif word[0] == '(':
      Parentheses+=1
    else :
      return False
    x = 1
    for i in range(1,len(word)):
      if word[i] == '{':
        Braces+=1
      elif word[i] == '[':
        Brackets+=1
      elif word[i] == '(':
        Parentheses+=1
      elif word[i] == '}':
        if word[i-x] == '{':
          Braces-=1
          x+=2
        else:
          return False
      elif word[i] == ')':
        if word[i-x] == '(':
          Parentheses-=1
          x+=2
        else:
          return False
      elif word[i] == ']':
        if word[i-x] == '[':
          Brackets-=1
          x+=2
        else:
          return False
      
    if (Braces, Brackets, Parentheses) == (0, 0, 0):
      return True
    else:
      return False
    
word = input()
print(balanced(word))