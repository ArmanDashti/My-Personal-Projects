from statistics import mean
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import style
import random

style.use('fivethirtyeight')

def create_dataset(n, variance, step = 2, correlation = False):
     val = 1
     ys = []
     for i in range(n):
          y = val + random.randrange(-variance, variance)
          ys.append(y)
          if correlation and correlation == 'pos':
               val += step
          elif correlation and correlation == 'neg':
               val -+ step
     xs = [i for i in range(len(ys))]
     
     return np.array(xs, dtype = np.float64), np.array(ys, dtype = np.float64)

def best_fit_slope_and_intercept(x, y):
     
     m = ( ((mean(x) * mean(y)) - mean(x*y)) /
          ((mean(x))**2 - mean(x**2)) ) 
     
     b = mean(y) - mean(x)*m
     
     return m, b

def squared_error(y_org, y_line):
     
     se = sum([(y_org[i] - y_line[i])**2 for i in range(len(y_org))])
     
     return se

def coefficient_of_determination(y_org, y_line):
     y_mean_line = [mean(y_org) for y in y_org]
     squared_error_regr = squared_error(y_org, y_line)
     squared_error_y_mean = squared_error(y_org, y_mean_line)
     
     return 1 - (squared_error_regr / squared_error_y_mean)

#xs = np.array([1, 2, 3, 4, 5, 6], dtype = np.float64)
#ys = np.array([5, 4, 6, 5, 6, 7], dtype = np.float64)

xs, ys = create_dataset(40, 40, 2, correlation = 'pos')

m, b = best_fit_slope_and_intercept(xs, ys)

regression_line = [(m*x) + b for x in xs]

r_squared = coefficient_of_determination(ys, regression_line)
print(r_squared)

plt.scatter(xs, ys)
plt.plot(xs, regression_line)
plt.show()