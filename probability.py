# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 18:25:23 2018

@author: Khang

Use for Data analysis
"""

from math import *

def combination(N,n):
    return factorial(N)/(factorial(n)*factorial(N-n))

def permuatation(N, n): 
    return factorial(N)/factorial(N-n)
    
def hypergeometric(success_set, failure_set, x, n): 
    """
    hypergeometric func will return the probability of success for picking x elements from the 
    total success set out of n trials. 
    
    Ex: what is the probability of drawing 5 heart cards from a 52 cards deck without replacement, if 10 draws happened. 
    
    success_set = 13 
    failure_set = 39
    x = 5
    n = 5
    """

    return combination(success_set, x)*combination(failure_set, n-x)/combination(success_set + failure_set, n)
