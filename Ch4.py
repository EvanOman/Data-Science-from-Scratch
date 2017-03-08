height_weight_age = [70,  # inches
					 170, # pounds
					 40]  # years
grades = [95, # exam 1
		  80, # exam 2
		  75, # exam 3
		  62] # exam 4

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
