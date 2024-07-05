def depth(exp):
    max_nest = 0
    Open_Bracket = 0
    Close_Bracket = 0
    for i in exp:
      if i == '(':
        Open_Bracket+=1
      elif i == ')':
        if Open_Bracket > max_nest:
          max_nest = Open_Bracket
        Open_Bracket-=1
    return max_nest

exp = input()
print(depth(exp))