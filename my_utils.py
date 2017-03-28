""" 
	Collection of "From Scratch" utility functions
"""
def linspace(b, e, n):
    return [b + (i/(n-1)) * (e - b) for i in range(n)]