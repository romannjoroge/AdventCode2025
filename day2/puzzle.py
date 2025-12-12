"""
We know the following information about this problem:

Let number of digits in a number be m
For a number to be invalid ID m must be even (so that you can have sequence of digit repeated twice)
Let n be m / 2

Let a valid number be XX where X is a positive integer
We know that 10^(n-1) <= X < 10^n
We know that formula for a number with digit repeated twice, i, is
i = X(10^n + 1)

We can use the range of X and the formula of i to get all numbers with digit repeated twice that has m numbers in it
"""

def get_number_digits(x: int) -> int:
    m = 0
    while (x > 0):
        x = x // 10
        m += 1
    return m