# Chapter 8 from Data Science from Scratch
from collections import Counter
#from linear_algebra import distance, vector_subtract, scalar_multiply
from functools import reduce
import math, random

import Ch4

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

if (isMain):
    derivative_est = lambda x: difference_quotient(square, x, h=.00001)

    import matplotlib.pyplot as plt
    x = range(-10,10)
    plt.title("Actual Derivative vs Esitmates")
    plt.plot(x, [derivative(x_i) for x_i in x], 'rx', label='Actual')
    plt.plot(x, [derivative_est(x_i) for x_i in x], 'b+', label='Estimate')
    plt.legend(loc=9)
    plt.show()


def partial_difference_quotient(f, v, i, h):
    """compute the ith partial difference quotient of f at v"""
    w = [v_j + (h if j == i else 0) for j, v_j in enumerate(v)]
    return (f(w) - f(v)) / h


def estimate_gradient(f, v, h=.00001):
    return [partial_difference_quotient(f, v, i, h) for i, _ in enumerate(v)]

# Obviously sum of squares has minimum at v = {0} but lets find this using gradient descent

# Gradient Descent: Choose random starting point, take steps in the direction of 
# greatest down slope (minimum direction)

def step(v, direction, step_size):
    """move step_size in the direction from v"""
    return [v_i + step_size * direction_i for v_i, direction_i in zip(v, direction)]

def sum_of_squares_gradient(v):
    return [2 * v_i for v_i in v]

if (isMain):
    # pick a random starting point
    v = [random.randint(-10, 10) for _ in range(3)]

    tolerance = .00000001

    while True:
        gradient = sum_of_squares_gradient(v)
        next_v = step(v, gradient, -0.01)
        if Ch4.distance(next_v, v) < tolerance:
            break
        v = next_v
    print(v)

# But what should the step size be?

# This is a safe apply function, just in case we try a bad step size
def safe(f):
    """Return a new function that is the same as f, except
        that it outputs infinity whenver f produces an error"""
    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return float('inf')
    return safe_f






































