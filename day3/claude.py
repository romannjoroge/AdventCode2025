#!/usr/bin/env python3
import time
"""
Advent of Code 2025 - Day 3 Part 2
Lobby - Battery Joltage (Select 12 batteries)
"""

def find_max_joltage(bank, num_batteries):
    """
    Find the maximum joltage by selecting exactly num_batteries from the bank.
    
    Strategy: We want to keep the largest digits and skip the smallest ones.
    We need to skip (len(bank) - num_batteries) digits.
    
    We use a greedy approach: at each position, we take the largest digit
    that still allows us to select enough remaining digits.
    """
    n = len(bank)
    to_skip = n - num_batteries
    
    if to_skip < 0:
        # Not enough batteries in the bank
        return None
    
    if to_skip == 0:
        # Take all batteries
        return int(bank)
    
    result = []
    skip_count = 0
    
    i = 0
    while len(result) < num_batteries:
        # How many batteries do we still need to select?
        remaining_needed = num_batteries - len(result)
        # How many positions are left (including current)?
        remaining_positions = n - i
        # How many more can we skip?
        can_skip = remaining_positions - remaining_needed
        
        # Find the best digit we can take from current position
        # We can look ahead up to 'can_skip' positions
        best_digit = bank[i]
        best_pos = i
        
        for j in range(i, min(i + can_skip + 1, n)):
            if bank[j] > best_digit:
                best_digit = bank[j]
                best_pos = j
        
        # Take the best digit we found
        result.append(best_digit)
        # Skip everything before it (and the digit itself)
        i = best_pos + 1
    
    return int(''.join(result))

def solve_part2(input_text):
    """Solve part 2: select 12 batteries from each bank."""
    lines = input_text.strip().split('\n')
    
    total_joltage = 0
    
    for i, line in enumerate(lines, 1):
        bank = line.strip()
        max_joltage = find_max_joltage(bank, 12)
        
        if max_joltage is None:
            print(f"Bank {i}: Not enough batteries (only {len(bank)})")
            continue
        
        print(f"Bank {i}: {bank} -> {max_joltage}")
        total_joltage += max_joltage
    
    return total_joltage

def test_examples():
    """Test with the examples from the problem."""
    test_input = """987654321111111
811111111111119
234234234234278
818181911112111"""
    
    print("Testing with examples:")
    print("=" * 60)
    result = solve_part2(test_input)
    print("=" * 60)
    print(f"Total output joltage: {result}")
    print(f"Expected: 3121910778619")
    print(f"Match: {result == 3121910778619}")
    print()

def main():
    # First, run tests
    test_examples()
    
    # Then solve the actual puzzle
    print("\nSolving actual puzzle:")
    print("=" * 60)
    
    try:
        with open('day3/input.txt', 'r') as f:
            input_text = f.read()
    except FileNotFoundError:
        print("Error: input.txt not found!")
        print("\nPlease create a file named 'input.txt' with your puzzle input.")
        print("You can get your input from: https://adventofcode.com/2025/day/3/input")
        return
    
    result = solve_part2(input_text)
    
    print("=" * 60)
    print(f"Total output joltage: {result}")
    print("=" * 60)

if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Code took {elapsed_time:.4f}")