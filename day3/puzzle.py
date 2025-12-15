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
    
def part_2():
    # bank = ['987654321111111', '811111111111119', '234234234234278', '818181911112111']
    banks = pd.read_csv('day3/input.txt', header=None)
    solution = 0
    for list_string in banks[0]:
        list_int = [int(s) for s in list_string]
        starting_index = -1
        current_pos = 0
        joltage_size = 12
        buffer = len(list_int) - joltage_size
        number_parts = []
        
        print(f"\n PROCESSING {list_string} with buffer {buffer}")
        
        while current_pos < joltage_size:
            # Get end position for current start position
            end_pos = current_pos + buffer 
            # Search area is slice from start_index + 1 to end post
            search_area = list_int[starting_index + 1:end_pos + 1]
            largest_in_search, index = find_largest_number(search_area)
            starting_index = starting_index + 1 + index
            number_parts.append(largest_in_search)
            # print(f"The largest number in position {current_pos} with end position {end_pos} is {largest_in_search} with new starting position of {starting_index}")
            current_pos += 1
        
        largest_number = int("".join(map(str, number_parts)))
        print(f"Largest possible number is {largest_number}")
        solution += largest_number
            
    print(f"Solution is {solution}")
    
part_2()



