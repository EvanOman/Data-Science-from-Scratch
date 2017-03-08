# Chapter 4: Linear Algebra


### VECTORS ###


def vector_add(v, w):
	"""adds corresponding elements"""
	# zip makes a list of 2-tuples from each list v and w
	return [v_i + w_i for v_i, w_i in zip(v, w)]


def vector_subtract(v, w):
	"""adds corresponding elements"""
	# zip makes a list of 2-tuples from each list v and w
	return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
	"""sums all corresponding elements"""
	# reduce along the list of vectors using the sum function
	return reduce(vector_add, vectors)

def scalar_multiply(c,v):
	"""c is a number, v is a vector"""
	return [c * v_i for v_i in v]

def vector_mean(vectors):
	"""compute the vector whose ith element is the mean of the ith elements
	of the input vectors"""
	n = len(vectors)
	return scalar_multiply(1/n, vector_sum(vectors))

def dot(v, w):
	"""v_1 * w_1 + ... + v_n * w_n"""
	return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
	return dot(v,v)

import math

def magnitude(v):
	return math.sqrt(sum_of_squares(v))

def distance(v, w):
	return magnitude(vector_subtract(v,w))


### MATRICES ###

# For now we represent matrices as lists of lists

# Returns a tuple: (# rows, # cols)
def shape(A):
	num_rows = len(A)
	# Python ternary use
	num_cols = len(A[0]) if A else 0
	return num_rows, num_cols

def get_row(A, i):
	return A[i]

def get_col(A, j):
	return [A_i[j] for A_i in A]

# Populates a matrix using the passed entry_fn
def make_matrix(num_rows, num_cols, entry_fn):
	return [[entry_fn(i,j) for j in range(num_cols)] for i in range(num_rows)]

# Example usage:
"""
>> entry_fn = lambda i,j: i + j

>> make_matrix(5,5,entry_fn)
Out: 
[[0, 1, 2, 3, 4],
 [1, 2, 3, 4, 5],
 [2, 3, 4, 5, 6],
 [3, 4, 5, 6, 7],
 [4, 5, 6, 7, 8]]

"""

# Determines if coordinates i, j lie along a diagonal
def is_diagonal(i, j):
	return 1 if i == j else 0

# Makes a dim x dim identity matrix
def eye(dim):
	return make_matrix(dim, dim, is_diagonal)