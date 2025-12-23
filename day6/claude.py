#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 6 Part 2
Trash Compactor - Cephalopod Math (Right-to-Left Column Reading)
"""
import time

def parse_worksheet(input_text):
    """
    Parse the worksheet into a grid.
    
    Returns:
        List of strings representing each row
    """
    lines = input_text.split('\n')
    # Remove empty lines at the end
    while lines and not lines[-1].strip():
        lines.pop()
    return lines


def extract_column(grid, col_idx):
    """
    Extract all characters from a specific column.
    
    Returns:
        String of characters from top to bottom
    """
    column = []
    for row in grid:
        if col_idx < len(row):
            column.append(row[col_idx])
        else:
            column.append(' ')
    return ''.join(column)


def is_separator_column(grid, col_idx):
    """Check if a column contains only spaces."""
    for row in grid:
        if col_idx < len(row) and row[col_idx] != ' ':
            return False
    return True


def solve_part2(input_text):
    """Solve part 2: read cephalopod math right-to-left."""
    grid = parse_worksheet(input_text)
    
    if not grid:
        return 0
    
    # Debug: print the grid
    print("Worksheet grid:")
    for i, row in enumerate(grid):
        print(f"Row {i}: '{row}'")
    print()
    
    num_cols = max(len(row) for row in grid)
    
    # Process columns from right to left
    grand_total = 0
    current_problem_numbers = []
    current_operator = None
    problem_num = 0
    
    for col_idx in range(num_cols - 1, -1, -1):  # Right to left
        column = extract_column(grid, col_idx)
        
        # Check if this is a separator column
        if column.strip() == '':
            # End of current problem, solve it
            if current_problem_numbers and current_operator:
                result = solve_problem(current_problem_numbers, current_operator)
                problem_num += 1
                print(f"Problem {problem_num}: {' {} '.format(current_operator).join(map(str, current_problem_numbers))} = {result}")
                grand_total += result
                current_problem_numbers = []
                current_operator = None
            continue
        
        # Extract the operator from the last row
        operator_char = column[-1]
        if operator_char in ['+', '*']:
            current_operator = operator_char
        
        # Extract the number from this column (all rows except the last)
        digits = []
        for char in column[:-1]:  # Exclude operator row
            if char.isdigit():
                digits.append(char)
        
        if digits:
            number = int(''.join(digits))
            current_problem_numbers.append(number)
    
    # Don't forget the last problem
    if current_problem_numbers and current_operator:
        result = solve_problem(current_problem_numbers, current_operator)
        problem_num += 1
        print(f"Problem {problem_num}: {' {} '.format(current_operator).join(map(str, current_problem_numbers))} = {result}")
        grand_total += result
    
    return grand_total


def solve_problem(numbers, operator):
    """
    Solve a single problem by applying the operator to all numbers.
    
    Args:
        numbers: List of integers
        operator: '+' or '*'
    
    Returns:
        Result of the operation
    """
    if not numbers:
        return 0
    
    result = numbers[0]
    for num in numbers[1:]:
        if operator == '+':
            result += num
        elif operator == '*':
            result *= num
    
    return result


def test_example():
    """Test with the example from the problem."""
    test_input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """
    
    print("Testing with example:")
    print("=" * 70)
    result = solve_part2(test_input)
    print("=" * 70)
    print(f"Grand total: {result}")
    print(f"Expected: 3263827")
    print(f"Match: {result == 3263827}")
    print()


def main():
    # First, run the test
    # test_example()
    
    # Then solve the actual puzzle
    print("\nSolving actual puzzle:")
    print("=" * 70)
    
    try:
        with open('day6/input.txt', 'r') as f:
            input_text = f.read()
    except FileNotFoundError:
        print("Error: input.txt not found!")
        print("\nPlease create a file named 'input.txt' with your puzzle input.")
        print("You can get your input from: https://adventofcode.com/2025/day/6/input")
        return
    
    result = solve_part2(input_text)
    
    print("=" * 70)
    print(f"Grand total: {result}")
    print("=" * 70)

if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Claude has taken {elapsed_time:.4f} seconds")