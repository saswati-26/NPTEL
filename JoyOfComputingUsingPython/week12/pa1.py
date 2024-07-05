def f(P):
    mean = sum(P) / len(P)
    return [p - mean for p in P]
 
def g(P, Q):
    return sum(P[i] * Q[i] for i in range(len(P)))
 
def h(x):
    return x ** 0.5

def pearson(X, Y):
  return g( f(X), f(Y) ) / ( h(g( f(X), f(X) ) ) * h(g( f(Y), f(Y) ) ) )

X = [float(x) for x in input().split()]
Y = [float(y) for y in input().split()]
print(f'{pearson(X, Y):.2f}',end='')