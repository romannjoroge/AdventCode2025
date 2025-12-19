#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 5 Part 2
Cafeteria - Count All Fresh Ingredient IDs in Ranges
"""

import time

class Range:
    """Represents a range of ingredient IDs."""
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __repr__(self):
        return f"Range({self.start}-{self.end})"
    
    def __lt__(self, other):
        """Enable sorting by start position."""
        return self.start < other.start
    
    def overlaps_or_adjacent(self, other):
        """Check if this range overlaps or is adjacent to another range."""
        return self.start <= other.end + 1 and other.start <= self.start + 1
    
    def merge_with(self, other):
        """Merge this range with another range, returning a new merged Range."""
        return Range(
            min(self.start, other.start),
            max(self.end, other.end)
        )
    
    def count(self):
        """Count the number of IDs in this range (inclusive)."""
        return self.end - self.start + 1
    
    def get_ids(self):
        """Get all IDs in this range as a list."""
        return list(range(self.start, self.end + 1))
    
    def contains(self, value):
        """Check if a value is within this range."""
        return self.start <= value <= self.end


def parse_input(input_text):
    """
    Parse the input to extract fresh ingredient ID ranges.
    
    Returns:
        List of Range objects
    """
    lines = input_text.strip().split('\n')
    ranges = []
    
    # Parse until we hit a blank line
    for line in lines:
        if line.strip() == '':
            break
        if '-' in line:
            start, end = line.strip().split('-')
            ranges.append(Range(int(start), int(end)))
    
    return ranges


def merge_ranges(ranges):
    """
    Merge overlapping or adjacent ranges to avoid double-counting.
    
    Args:
        ranges: List of Range objects
    
    Returns:
        List of merged non-overlapping Range objects
    """
    if not ranges:
        return []
    
    # Sort ranges by start position
    sorted_ranges = sorted(ranges)
    
    merged = [sorted_ranges[0]]
    
    for current_range in sorted_ranges[1:]:
        last_range = merged[-1]
        
        # Check if current range overlaps or is adjacent to the last merged range
        if current_range.start <= last_range.end + 1:
            # Merge by creating a new range that spans both
            merged[-1] = last_range.merge_with(current_range)
        else:
            # No overlap, add as a new range
            merged.append(current_range)
    
    return merged


def count_fresh_ids(ranges):
    """
    Count the total number of ingredient IDs considered fresh.
    
    Args:
        ranges: List of Range objects
    
    Returns:
        Total count of unique fresh ingredient IDs
    """
    # Merge overlapping ranges first to avoid double-counting
    merged = merge_ranges(ranges)
    
    total_count = 0
    all_fresh_ids = []
    
    print("Merged ranges:")
    for range_obj in merged:
        count = range_obj.count()
        total_count += count
        print(f"  {range_obj.start}-{range_obj.end}: {count} IDs")
        
        # For visualization (only show if reasonable size)
        if count <= 20:
            ids_in_range = range_obj.get_ids()
            all_fresh_ids.extend(ids_in_range)
            print(f"    IDs: {ids_in_range}")
    
    if all_fresh_ids:
        print(f"\nAll fresh IDs: {sorted(set(all_fresh_ids))}")
    
    return total_count


def solve_part2(input_text):
    """Solve part 2: count all ingredient IDs in the fresh ranges."""
    ranges = parse_input(input_text)
    
    print(f"Original fresh ingredient ranges:")
    for r in ranges:
        print(f"  {r.start}-{r.end}")
    print()
    
    total_fresh = count_fresh_ids(ranges)
    
    return total_fresh


def test_example():
    """Test with the example from the problem."""
    test_input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
    
    print("Testing with example:")
    print("=" * 60)
    result = solve_part2(test_input)
    print("=" * 60)
    print(f"Total fresh ingredient IDs: {result}")
    print(f"Expected: 14")
    print(f"Match: {result == 14}")
    print()


def main():
    # First, run the test
    # test_example()
    
    # Then solve the actual puzzle
    print("\nSolving actual puzzle:")
    print("=" * 60)
    
    try:
        with open('day5/input.txt', 'r') as f:
            input_text = f.read()
    except FileNotFoundError:
        print("Error: input.txt not found!")
        print("\nPlease create a file named 'input.txt' with your puzzle input.")
        print("You can get your input from: https://adventofcode.com/2025/day/5/input")
        return
    
    result = solve_part2(input_text)
    
    print("=" * 60)
    print(f"Total fresh ingredient IDs: {result}")
    print("=" * 60)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Claude has taken {elapsed_time:.4f} seconds")