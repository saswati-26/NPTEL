def std_dev(X):
    mean = sum(X) / len(X)
    ad = [p - mean for p in X]
    return ( sum(ad[i] * ad[i] for i in range(len(ad))) / (len(X)-1) )** 0.5
X = [float(x) for x in input().split(',')]
sigma = std_dev(X)
print(f'{sigma:.2f}',end='')