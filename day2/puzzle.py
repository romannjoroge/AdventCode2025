"""
We know the following information about this problem:

Let number of digits in a number be m
For a number to be invalid ID m must be even (so that you can have sequence of digit repeated twice)
Let n be m / 2

Let an invalid number be XX where X is a positive integer
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

def get_invalid_id(X: int, n: int) -> int:
    assert n >= 1, "n must be at least 1 for it to be a sequence of digits repeated twice"
    assert (10 ** (n - 1)) <= X and X < 10 ** n, "Invalid X value" 
    i = X * ((10 ** n) + 1)
    return i

def get_first_last_number_from_range(range: str) -> (int, int):
    numbers = range.split('-')
    assert len(numbers) >= 2
    return numbers[0], numbers[-1]