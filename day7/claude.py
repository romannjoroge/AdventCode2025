#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 7 Part 1
Laboratories - Tachyon Beam Splitting
"""

from collections import deque
import time

def parse_manifold(input_text):
    """
    Parse the manifold diagram.
    
    Returns:
        grid: 2D list of characters
        start_pos: (row, col) of the starting position 'S'
    """
    lines = input_text.strip().split('\n')
    grid = [list(line) for line in lines]
    
    # Find starting position
    start_pos = None
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'S':
                start_pos = (row, col)
                break
        if start_pos:
            break
    
    return grid, start_pos


def simulate_beams(grid, start_pos):
    """
    Simulate the tachyon beams moving through the manifold.
    
    Returns:
        Number of times beams are split
    """
    if not start_pos:
        return 0
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Queue of beams: (row, col)
    # Each beam starts at a position and moves downward
    beams = deque([start_pos])
    
    # Track which positions already have beams passing through
    # to avoid counting the same split multiple times
    active_beams = set()
    active_beams.add(start_pos)
    
    split_count = 0
    
    while beams:
        row, col = beams.popleft()
        
        # Move beam downward until it hits a splitter or exits
        current_row = row + 1
        
        while current_row < rows:
            current_pos = (current_row, col)
            
            # Check what's at this position
            cell = grid[current_row][col]
            
            if cell == '^':
                # Hit a splitter!
                split_count += 1
                
                # Create two new beams: left and right
                left_col = col - 1
                right_col = col + 1
                
                # Add left beam if valid and not already active
                if left_col >= 0:
                    left_pos = (current_row, left_col)
                    if left_pos not in active_beams:
                        beams.append(left_pos)
                        active_beams.add(left_pos)
                
                # Add right beam if valid and not already active
                if right_col < cols:
                    right_pos = (current_row, right_col)
                    if right_pos not in active_beams:
                        beams.append(right_pos)
                        active_beams.add(right_pos)
                
                # Original beam stops at splitter
                break
            
            # Move to next row
            current_row += 1
    
    return split_count


def visualize_beams(grid, start_pos):
    """
    Create a visualization of the beam paths (for debugging).
    """
    if not start_pos:
        return
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Create a copy for visualization
    vis_grid = [row[:] for row in grid]
    
    # Queue of beams with their paths
    beams = deque([(start_pos, [start_pos])])
    visited = set()
    visited.add(start_pos)
    
    while beams:
        (row, col), path = beams.popleft()
        
        # Move beam downward
        current_row = row + 1
        
        while current_row < rows:
            current_pos = (current_row, col)
            cell = grid[current_row][col]
            
            # Mark beam path
            if cell == '.':
                vis_grid[current_row][col] = '|'
            
            if cell == '^':
                # Mark splitter
                if current_row > 0 and vis_grid[current_row - 1][col] == '.':
                    vis_grid[current_row - 1][col] = '|'
                
                # Split into left and right
                left_col = col - 1
                right_col = col + 1
                
                if left_col >= 0 and (current_row, left_col) not in visited:
                    beams.append(((current_row, left_col), path + [(current_row, left_col)]))
                    visited.add((current_row, left_col))
                
                if right_col < cols and (current_row, right_col) not in visited:
                    beams.append(((current_row, right_col), path + [(current_row, right_col)]))
                    visited.add((current_row, right_col))
                
                break
            
            current_row += 1
    
    # Print visualization
    print("\nBeam visualization:")
    for row in vis_grid:
        print(''.join(row))


def solve_part1(input_text, visualize=False):
    """Solve part 1: count beam splits."""
    grid, start_pos = parse_manifold(input_text)
    
    if not start_pos:
        print("Error: Could not find starting position 'S'")
        return 0
    
    print(f"Grid size: {len(grid)} rows x {len(grid[0])} cols")
    print(f"Starting position: {start_pos}")
    
    split_count = simulate_beams(grid, start_pos)
    
    if visualize:
        visualize_beams(grid, start_pos)
    
    return split_count


def test_example():
    """Test with the example from the problem."""
    test_input = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""
    
    print("Testing with example:")
    print("=" * 70)
    result = solve_part1(test_input, visualize=True)
    print("=" * 70)
    print(f"Number of beam splits: {result}")
    print(f"Expected: 21")
    print(f"Match: {result == 21}")
    print()


def main():
    # First, run the test
    # test_example()
    
    # Then solve the actual puzzle
    print("\nSolving actual puzzle:")
    print("=" * 70)
    
    try:
        with open('day7/input.txt', 'r') as f:
            input_text = f.read()
    except FileNotFoundError:
        print("Error: input.txt not found!")
        print("\nPlease create a file named 'input.txt' with your puzzle input.")
        print("You can get your input from: https://adventofcode.com/2025/day/7/input")
        return
    
    result = solve_part1(input_text)
    
    print("=" * 70)
    print(f"Number of beam splits: {result}")
    print("=" * 70)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Claude has taken {elapsed_time:.4f} seconds")