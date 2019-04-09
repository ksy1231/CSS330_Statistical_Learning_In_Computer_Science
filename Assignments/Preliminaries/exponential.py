import math

def exponential(x):
     """Calculate the exponential function by a series expansion.
          
         Sample exponential formula is for e^x as given in
         https://en.wikipedia.org/wiki/Exponential_function (accessed
         January 15, 2019)
         
         Args:
             x: a scalar input.

         Returns:
             scalar output of the exponential function.

         """
     result = 1
     temp = 1
     sum = 0
     pres = 0.0001
     while result > pres:
          sum = sum + result
          result = (x**temp) / math.factorial(temp)
          temp = temp + 1
     return sum

print(exponential(3.4))
