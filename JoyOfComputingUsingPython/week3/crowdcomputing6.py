#plot made by estimates constant y

import matplotlib.pyplot as plt
import statistics

estimates = [100, 1010, 250,200, 350, 202, 2600, 2700, 220, 260, 2003, 2020, 2015]
y = []

estimates.sort()
tv = int(0.1 * (len(estimates)))
estimates = estimates[tv:]
estimates = estimates[:len(estimates)-tv]

num = int(input("Enter the constant y value: "))
for i in range(len(estimates)):
    n = num
    y.append(n)

plt.plot(estimates)
plt.plot([statistics.mean(estimates)],[n],'ro')
plt.plot([statistics.median(estimates)],[n],'bs')
plt.plot([375],[n],'g^')