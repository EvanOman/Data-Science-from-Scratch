from __future__ import division
import random

# Chapter 6: Probabilty

# Here we empirically check the probability that both children are girls(event B) given 
# that at least one of the children is a girl (event L)

# Theoretically we have: P(B|L) = P(B,L)/P(L) = P(B)/P(L) = 1/3

def random_kid():
    return random.choice(["boy", "girl"])
    
both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)

for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    
    if older == "girl":
        older_girl += 1
    
    if older == "girl" and younger == "girl":
        both_girls += 1
        
    if older == "girl" or younger == "girl":
        either_girl += 1
        
print "P(both | older) = %f" % (both_girls / older_girl) # .514 ~ 1/2
print "P(both | either) = %f" % (both_girls / either_girl) # .341 ~ 1/3