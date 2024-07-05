def factors(n):
    factorset = set()
    for i in range(1,n+1):
      if n%i == 0:
        factorset.add(i)
    return(factorset)
 
def common_factors(a, b):
    return(factors(a).intersection(factors(b)))
 
def factors_upto(n):
    D = {}
    for i in range(1,n+1):
      D[i] = factors(i)
    return(D)

print(factors_upto(4))