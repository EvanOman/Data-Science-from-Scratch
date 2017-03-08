# Chapter 7: Hypothesis and Inference

from __future__ import division
import Ch6
import math
import random

# We want to check whether a given coin is fair. So we make our null hypothesis
# that the coin is fair (p = .5) and the alternative hypothesis that the coin is
# not fair (p =/= .5)

# Our test will then involve flipping the coin n times. We use the bernoulli 
# trials and normal approximation explored in Chapter 6 

def normal_approximation_to_binomial(n, p):
    """Finds mu and sigma corresponding to a Binomial(n, p)"""
    mu = p * n
    
    # p*q*n
    sigma = math.sqrt(p*(1-p)*n)
    
    return mu, sigma
    
# probability that variable is below threshold
normal_probability_below = Ch6.normal_cdf

# it is above the threshold if it isn't below the threshold
def normal_probabilty_above(lo, mu=0, sigma=1):
    return 1 - Ch6.normal_cdf(lo, mu, sigma)
    
# it is in between if it is less than hi but not let than lo
def normal_probability_between(lo, hi, mu=0, sigma=1):
    return Ch6.normal_cdf(hi, mu, sigma) - Ch6.normal_cdf(lo, mu, sigma)
    
# it is outside if it is not in between
def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, sigma, mu)
    

# We can also perform the reverse of all the above operations to find z values
# corresponding to certain p ranges

def normal_upper_bound(probability, mu=0, sigma=1):
    """returns the z for which p(Z <= z) = probability"""
    return Ch6.inverse_normal_cdf(probability, mu, sigma)
    
def normal_lower_bound(probability, mu=0, sigma=1):
    """returns the z for which p(Z >= z) = probability"""
    return Ch6.inverse_normal_cdf(1 - probability, mu, sigma)
    
def normal_two_sided_bounds(probability, mu=0, sigma=1):
    """returns the symmetric(about the mean) bounds that contain specified p"""
    tail_probability = (1 - probability) / 2
    
    # upper bound should have tail_probability above it
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)
    
    
    # lower bound should have tail_probability below it
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)
    
    return lower_bound, upper_bound
    
    
if __name__ == "__main__":
    # In particular, suppose we were to flip a coin 100 times. If our hypothesis is 
    # true, X should be distributed approximately normally iwth mean 50 and std 15.8
    mu_0, sigma_0 = normal_approximation_to_binomial(1000,.5)
    
    # We now need to decide on a level of significance, that is how willing are
    # we to make a type I, false positive error with respect to H_0
    
    # Suppose H_0 falls out the following bounds:
    normal_two_sided_bounds(.95, sigma_0, mu_0) # (469, 531)
    
    # Then we say that we reject the null hypothesis because we should be 95% 
    # confident that the mean should lie within the range (469, 531)
    
    # Here we want to check what happens when p = .55
    
    # 95% bounds based on assumption that p = .5
    lo, hi = normal_two_sided_bounds(.95, mu_0, sigma_0)
    
    # actual mu and sigma based on p = .55
    mu_1, sigma_1 = normal_approximation_to_binomial(1000, .55)
    
    # a type 2 error means we fail to reject the null hypothesis
    # which will happen when X is still in our original interval
    type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
    power = 1 - type_2_probability
    print("The power is {:f}".format(power)) # .887
    
    # Suppose instead we assumed that the coin is not biassed against heads, 
    # this is, p <= .5. Here we would use the one sided test:
    hi = normal_upper_bound(.95, mu_0, sigma_0)
    print("The upper limit is {:f}".format(hi)) # 526
    
    type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
    power = 1 - type_2_probability
    print("The power is {:f}".format(power)) #.936
    
# Instead of specifying the bounds, we compute the probability, assuming that
# H_0 is true, that the system exhibits the observed value
def two_sided_p_value(x, mu=0, sigma=1):
    # essentially we are figuring out which tail to compute and return the 
    # double of
    if x >= mu:
        # if x is greater than the mean, the tail is what's greater than x
        return 2 * normal_probabilty_above(x, mu, sigma)
    else:
        # if x is less than the mean, the tail is what's less than x
        return 2 * normal_probability_below(x, mu, sigma)
    
if __name__ == "__main__":
    # If we got 530 heads we would get:
    print("The p-value is {:f}".format(two_sided_p_value(529.5, mu_0, sigma_0))) # .062
    
    # NOTE: We use 529.5 instead of 530 because of the continuity correction
    
    # Empirical verification of the above p value
    extreme_value_count = 0
    for _ in range(100000):
        num_heads = sum(1 if random.random() < .5 else 0 for _ in range(1000))
    
        if num_heads >= 530 or num_heads <= 470:
            extreme_value_count += 1
    
    print("The percentage that were extreme was {:f}".format(extreme_value_count / 100000))
    # .062
    
# Similarily we have:
upper_p_value = normal_probabilty_above
lower_p_value = normal_probability_below

if __name__ == "__main__":
    print("Upper: {:f}".format(upper_p_value(524.5, mu_0, sigma_0))) # .061
    print("Upper: {:f}".format(upper_p_value(526.5, mu_0, sigma_0))) # .047
    
    # In the former case, we are above .05 so we fail to reject the null hyp.
    # In the latter case, we are below .05 so we reject the null hypothesis
    
    
    