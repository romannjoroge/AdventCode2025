import pandas as pd

"""
Our joltage values, j , 1 <= j <= 9

Banks are an unordered collection of jolatage values

Need 2 find largest 2 values that follow each other
"""
def find_largest_number(bank: list[int]) -> (int, int):
    largest = 0
    largest_index = 0
    
    for index, joltage in enumerate(bank):
        if (joltage == 9):
            largest = joltage
            largest_index = index
            break
        elif (joltage > largest):
            largest = joltage
            largest_index = index
            
    return largest, largest_index

def part_1():
    banks = pd.read_csv('day3/input.txt', header=None)
    solution = 0
    
    for list_string in banks[0]:
        list_int = [int(s) for s in list_string]
        end_index = len(list_int) - 1
        x = 0
        y = 0
        x, index_x = find_largest_number(list_int)
        if (index_x < end_index):
            new_list = list_int[index_x + 1:]
            y, _ = find_largest_number(new_list)
        else:
            y = x
            new_list = list_int[:end_index]
            x, _ = find_largest_number(new_list)
            
        solution += (x * 10) + y
        
    print(f"Solution is {solution}")
    
part_1()


