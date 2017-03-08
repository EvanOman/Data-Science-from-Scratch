# Chapter 8 from Data Science from Scratch

isMain = __name__ == "__main__"

def sum_of_squares(v):
    """computes the sum of squared elements in v"""
    return sum(v_i ** 2 for v_i in v)

def difference_quotient(f, x, h):
    return (f(x+h) - f(x))/h

def square(x):
    return x*x

def derivative(x):
    return 2*x

#if (isMain):
    
derivative_est =  lambda x: difference_quotient(square, x, h=.00001)

import matplotlib.pyplot as plt
x = range(-10,10)
plt.title("Actual Derivative vs Esitmates")
plt.plot(x, map(derivative, x), 'rx', label='Actual')
plt.plot(x, map(derivative_est, x), 'b+', label='Estimate')
plt.legend(loc=9)
plt.show()


