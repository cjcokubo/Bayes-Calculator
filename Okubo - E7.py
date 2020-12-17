# Author: Christine Okubo
# Date: 11-27-20
# Input: : a) prior probability of A, b) prior probability of B / probability of B given not A, 
# c) probability of B given A, d) flag (1 or 2) 
# Output: posterior probability of A given B

def bayesCalculator (a, b, c, d):
    if d==1:
        p_A_given_B = (a*c) / b
        return p_A_given_B
    elif d==2:
        p_A_given_B = (a*c) / (a*c + (1-a)*b)
        return p_A_given_B
    else: 
        print("Please input valid flag (1 or 2).")