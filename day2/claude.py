#!/usr/bin/env python3
import time
"""
Advent of Code 2025 - Day 2 Part 2
Gift Shop - Invalid Product IDs (Pattern Repeated At Least Twice)
"""

def is_invalid_id(id_num):
    """
    Check if an ID is invalid (made of a pattern repeated at least twice).
    
    An ID is invalid if it can be expressed as a string repeated 2+ times.
    For example: 123123 (123 twice), 12121212 (12 four times), 111 (1 three times)
    """
    id_str = str(id_num)
    n = len(id_str)
    
    # Try all possible pattern lengths from 1 to n//2
    # (pattern must repeat at least twice, so max length is n//2)
    for pattern_len in range(1, n // 2 + 1):
        # Check if the string length is divisible by pattern length
        if n % pattern_len == 0:
            pattern = id_str[:pattern_len]
            repetitions = n // pattern_len
            
            # Check if repeating the pattern gives us the original string
            if pattern * repetitions == id_str:
                # Must repeat at least twice
                if repetitions >= 2:
                    return True
    
    return False

def parse_ranges(input_text):
    """Parse the input string into a list of (start, end) tuples."""
    # Remove whitespace and split by comma
    ranges_str = input_text.strip().replace('\n', '').replace(' ', '')
    range_parts = ranges_str.split(',')
    
    ranges = []
    for part in range_parts:
        if '-' in part and part:  # Skip empty strings
            # Split on the last dash to handle negative numbers (though not in this problem)
            start_end = part.split('-')
            if len(start_end) == 2:
                start, end = start_end
                ranges.append((int(start), int(end)))
    
    return ranges

def solve_part2(input_text):
    """Solve part 2: find all invalid IDs with patterns repeated at least twice."""
    ranges = parse_ranges(input_text)
    
    total_sum = 0
    all_invalid_ids = []
    
    for start, end in ranges:
        invalid_in_range = []
        
        for id_num in range(start, end + 1):
            if is_invalid_id(id_num):
                invalid_in_range.append(id_num)
                total_sum += id_num
        
        if invalid_in_range:
            print(f"{start}-{end}: {len(invalid_in_range)} invalid ID(s): {invalid_in_range}")
        else:
            print(f"{start}-{end}: No invalid IDs")
        
        all_invalid_ids.extend(invalid_in_range)
    
    return total_sum, all_invalid_ids

def test_examples():
    """Test with the examples from the problem."""
    test_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""
    
    print("Testing with examples:")
    print("=" * 70)
    
    # Test individual cases
    test_cases = [
        (11, True, "11 (1 twice)"),
        (99, True, "99 (9 twice)"),
        (111, True, "111 (1 three times)"),
        (999, True, "999 (9 three times)"),
        (1010, True, "1010 (10 twice)"),
        (1188511885, True, "1188511885 (11885 twice)"),
        (222222, True, "222222 (2 six times or 22 three times)"),
        (446446, True, "446446 (446 twice)"),
        (38593859, True, "38593859 (3859 twice)"),
        (565656, True, "565656 (56 three times)"),
        (824824824, True, "824824824 (824 three times)"),
        (2121212121, True, "2121212121 (21 five times)"),
        (12341234, True, "12341234 (1234 twice)"),
        (101, False, "101 (not a pattern)"),
    ]
    
    print("\nTesting individual cases:")
    for num, expected, description in test_cases:
        result = is_invalid_id(num)
        status = "✓" if result == expected else "✗"
        print(f"{status} {description}: {result}")
    
    print("\n" + "=" * 70)
    print("Testing full example:")
    print("=" * 70)
    result, invalid_ids = solve_part2(test_input)
    print("=" * 70)
    print(f"Total sum: {result}")
    print(f"Expected: 4174379265")
    print(f"Match: {result == 4174379265}")
    print()

def main():
    # First, run tests
    test_examples()
    
    # Then solve the actual puzzle
    print("\nSolving actual puzzle:")
    print("=" * 70)
    
    try:
        with open('day2/input.txt', 'r') as f:
            input_text = f.read()
    except FileNotFoundError:
        print("Error: input.txt not found!")
        print("\nPlease create a file named 'input.txt' with your puzzle input.")
        print("You can get your input from: https://adventofcode.com/2025/day/2/input")
        return
    
    result, invalid_ids = solve_part2(input_text)
    
    print("=" * 70)
    print(f"Total sum of all invalid IDs: {result}")
    print("=" * 70)

if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Elapsed time is {elapsed_time:.4f}")