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
    """
    Function for getting the number of digits that are in a number
    """
    m = 0
    while (x > 0):
        x = x // 10
        m += 1
    return m

def get_invalid_id(X: int, n: int) -> int:
    """
    Function for getting a fake product ID from an X and n value
    """
    assert n >= 1, "n must be at least 1 for it to be a sequence of digits repeated twice"
    assert (10 ** (n - 1)) <= X and X < 10 ** n, "Invalid X value" 
    i = X * ((10 ** n) + 1)
    return i

def get_first_last_number_from_range(range: str) -> (int, int):
    """
    Function for getting the first and last number in the provided number range
    """
    numbers = range.split('-')
    assert len(numbers) >= 2
    return int(numbers[0]), int(numbers[-1])

def get_part2_invalid_id(d: int, x: int, n: int) -> int:
    """
    Function for getting invalid id where there is a sequence of numbers d with n digits repeated x times
    """
    assert x > 1, "n must be greater than 2"
    assert (10 ** (n - 1)) <= d and d < 10 ** n, "Invalid d value"
    
    r = 10 ** n
    print(f"r {r} r ^ x {r ** x} 1 - r {1 - r}")
    denominator = 1 - r
    numerator = d * (1 - r ** x)
    i = numerator / denominator
    return i 
    

def part_1():
    # Get input from file
    input_text = "269194394-269335492,62371645-62509655,958929250-958994165,1336-3155,723925-849457,4416182-4470506,1775759815-1775887457,44422705-44477011,7612653647-7612728309,235784-396818,751-1236,20-36,4-14,9971242-10046246,8796089-8943190,34266-99164,2931385381-2931511480,277-640,894249-1083306,648255-713763,19167863-19202443,62-92,534463-598755,93-196,2276873-2559254,123712-212673,31261442-31408224,421375-503954,8383763979-8383947043,17194-32288,941928989-941964298,3416-9716"
    ranges = input_text.split(",")
    sum_invalid_ids = 0
    
    # For each range in input
    for invalid_range in ranges:
        print(f"\n PROCESSING RANGE {invalid_range}, sum of invalid ids is {sum_invalid_ids}")
        # Get first and last number from input
        f, l = get_first_last_number_from_range(invalid_range)
        
        # Get m of first and last number
        f_m = get_number_digits(f)
        l_m = get_number_digits(l)
        
        # Get list of all m's in between that of first and last number
        valid_ms = []
        for possible_m in range(f_m, l_m + 1):
            # From this list get valid m's, where m is an even number
            if possible_m % 2 == 0 and possible_m > 0:
                valid_ms.append(possible_m)
                
        print(f"Valid m values {valid_ms} for f -> {f} and l -> {l}")
        if len(valid_ms) == 0:
            print("No valid m so skipping")
            continue
        
        if len(valid_ms) == 1:
            valid_m = valid_ms[0]
            n = valid_m / 2
            # Get list of all possible X's for getting invalid numbers (in between those of first and last number)
            f_X = int(f // ((10 ** n) + 1))
            l_X = int(l // ((10 ** n) + 1))
        
            print(f"The valid m is {valid_m}, first valid X is {f_X} and last valid X is {l_X}")    
            
            valid_Xs = []
            for X in range(f_X, l_X + 1):
                if (10 ** (n - 1)) <= X and X < 10 ** n:
                    valid_Xs.append(X)
            
            if len(valid_Xs) == 0:
                print("No valid Xs skipping")
                continue
            
            # Get all possible invalid numbers
            all_possible_invalid = [get_invalid_id(X, n) for X in valid_Xs]
            print(f"All Possible invalid {all_possible_invalid}")
            
            while True:
                if all_possible_invalid[0] < f:
                    all_possible_invalid.pop(0)
                else:
                    break
            
            print(f"Possible invalid values that are in range of f and l {all_possible_invalid}")
            
            # Add together those that are in range [f, l]
            sum_invalid_ids += sum(all_possible_invalid)
        else:
            raise "Got more than 1 valid m, need to handle this case"
        
    print(f"Answer is {sum_invalid_ids}")

d_configurations = {
    2: [1],
    3: [1],
    4: [2, 1],
    5: [1],
    6: [1, 2, 3],
    7: [1],
    8: [1, 2, 4],
    9: [1, 3],
    10: [1, 2, 5]
}

# Hoping I can do something similar for part 2
def part_2():
    # Get input from file
    # input_text = "269194394-269335492,62371645-62509655,958929250-958994165,1336-3155,723925-849457,4416182-4470506,1775759815-1775887457,44422705-44477011,7612653647-7612728309,235784-396818,751-1236,20-36,4-14,9971242-10046246,8796089-8943190,34266-99164,2931385381-2931511480,277-640,894249-1083306,648255-713763,19167863-19202443,62-92,534463-598755,93-196,2276873-2559254,123712-212673,31261442-31408224,421375-503954,8383763979-8383947043,17194-32288,941928989-941964298,3416-9716"
    input_text = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862"
    ranges = input_text.split(",")
    sum_invalid_ids = 0
    
    # For each range in input
    for invalid_range in ranges:
        print(f"\n PROCESSING RANGE {invalid_range}, sum of invalid ids is {sum_invalid_ids}")
        # Get first and last number from input
        f, l = get_first_last_number_from_range(invalid_range)
        num_digits_f = get_number_digits(f)
        num_digits_l = get_number_digits(l)
        
        if num_digits_f == num_digits_l:
            print("Both f and l have same number of digits")
            # Get possible d configurations
            num_digits_d_config = d_configurations[num_digits_f]
            invalid_ids = []
            for n in num_digits_d_config:
                x = num_digits_f / n
                r = 10 ** n
                f_d = f // r ** (x - 1)
                print(f"f_d is {f_d} when f is {f} num_digits_f is {num_digits_f} r is {r} and x is {x} and n is {n}")
        else:
            print(f"f has {num_digits_f} while l has {num_digits_l}")
            pass
        
part_2()