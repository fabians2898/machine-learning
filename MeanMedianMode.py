import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
# fake income data, centered around 27000 with a normal distribution 
# and standard deviation of 15000, with 10000 data points
incomes = np.random.normal(2700, 15000, 10000)
print "Mean = ", np.mean(incomes)
print "Median = ", np.median(incomes)
print "Mode = ", stats.mode(incomes)
plt.hist(incomes, 50)
plt.show()