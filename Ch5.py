# Chapter 5: Statistics

from __future__ import division
import matplotlib.pyplot as plt
from collections import Counter
import random as r
# For reproducibility 
r.seed(1248)

# Data set:
num_friends = [r.randint(1,100) for i in xrange(200)]

# Create a histogram for the data
friends_counts = Counter(num_friends)
xs = range(101)
ys = [friends_counts[x] for x in xs]
# plt.bar(xs, ys)
# plt.axis([0, 101, 0, 25])
# plt.title("Histogram of Friend Counts")
# plt.xlabel("# of friends")
# plt.ylabel("# of people")
# plt.show()

num_points = len(num_friends)

largest_value = max(num_friends)
smallest_value = min(num_friends)

sorted_values = sorted(num_friends)
second_smallest_value = sorted_values[1]
print((smallest_value, second_smallest_value))

def mean(x):
	return sum(x)/len(x)

print(mean(num_friends))

def median(v):
	n = len(v)
	sorted_v = sorted(v)
	midpoint = n // 2

	if n % 2 :
		return sorted_v[midpoint]
	else:
		# if it is even, we need to average
		lo = midpoint - 1
		hi = midpoint
		return (sorted_v[lo] + sorted_v[hi])/2

print("Median: "  + str(median(num_friends)))

# Medians generalize well into quantiles:
def quantile(x,p):
	p_index = int(p * len(x))
	return sorted(x)[p_index]

print(quantile(num_friends, .10))
print(quantile(num_friends, .25))
print(quantile(num_friends, .75))
print(quantile(num_friends, .90))

