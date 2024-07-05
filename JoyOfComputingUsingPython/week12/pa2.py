def survival(T):
    for x in range(6):
      for y in range(6):
        if 30 + x**2 + y**2 - 3*x - 4*y <= T:
          return True
    return False

T = int(input())
print(survival(T),end='')