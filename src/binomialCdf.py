__author__ = 'Brandon Yeo'

import operator as op
from functools import reduce

#Calculates binomial cdf with n,p and x
#P(X < x)
#n is number of trials in the distribution
#p is probability of success
#r is the random variable

def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, range(n, n-r, -1))
    denom = reduce(op.mul, range(1, r+1))
    return numer//denom

def binomialPdf(n, r, p):
    return ncr(n, r) * pow(p, r) * pow(1-p, n-r)

def binomialCdf(n, r, p):
    totalResult = 0
    for k in range(1, r):
        totalResult += binomialPdf(n,k,p)
    return totalResult

numTrials = input("Number of trials: ")
randomVar = input("Number of success: ")
probability = input("Probability of success: ")

print("Result is : " + str(binomialCdf(int(numTrials), int(randomVar), float(probability))))