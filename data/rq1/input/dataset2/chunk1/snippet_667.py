#Source: https://stackoverflow.com/questions/77589004/problem-execute-calculations-in-a-nested-loop-typeerror-numpy-float64-object
from numpy import mean
import math

values = [5, 2, 3, 4, 0]

mean = mean(values)

for x in values:
  values_subtraction_mean = x - mean
  print(values_subtraction_mean)
  #2.2, -0.8, 0.2, 1.2, -2.8

  for y in values_subtraction_mean:
    result = sum(math.sqrt(y))
    print(result)
    #sqrt: 4.84, 0.64, 0.04, 1.44, 7.84
    #sum and result: 14.8