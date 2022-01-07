#!/usr/bin/python3
"""
Script for the function minOperations(n)
"""


def minOperations(n):
    """
    Function to find the min operations
    """
    if n <= 1:
        return 0

    divisor = 2
    oper = 0
    quotient = n
    while quotient > 1:
        if (quotient % divisor) == 0:
            quotient = quotient // divisor
            oper += divisor
        else:
            divisor += 1

    return oper
