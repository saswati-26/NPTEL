from statistics import mean
from scipy import stats
estimates = [100, 1010, 250,200, 350, 202, 2600, 2700, 220, 260, 2003, 2020, 2015]
estimates.sort()
m=stats.trim_mean(estimates,0.1)
print(m)