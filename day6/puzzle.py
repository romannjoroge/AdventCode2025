"""
Try seeing if I can get a stream of each line in input file

For each line, get the next number and end buffer. Get number by seeing strings whos ord [0, 9]

Add up numbers from each line

When reach end of line of any line stop
"""
import math
import re

def part_1():
    result = 0
    # Get stream for each line in file
    with open("day6/input.txt", "r") as file:
        iterators = [line.split() for line in file]
        
        for args in zip(*iterators):
            operation = args[-1]
            numbers = [int(x) for x in args[0:-1]]
            if operation == "+":
                result += sum(numbers)
            else:
                result += math.prod(numbers)
            
    print(f"Result is {result}")
    
# part_1()

def cephalapod_math(item: list[str]) -> int:
    print(f"Doing cephalapod math for {item}")
    raw_numbers = item[0:-1]
    operation = item[-1]
    intepreted_nums = []
    place = 1
    
    while True:
        num_has_place = False
        num_to_add = ""
        for num in raw_numbers:
            if len(num) >= place:
                num_has_place = True
                num_to_add += num[place - 1]
                
        if (num_has_place == False):
            break
        else:
            intepreted_nums.append(int(num_to_add))
            place += 1
            
    print(f"Interpreted nums are {intepreted_nums}")
        
    if operation == "+":
        return sum(intepreted_nums)
    else:
        return math.prod(intepreted_nums)
    
def get_column_space_position(x: str, start: int) -> int:
    """
    This function gets possible position of column space in string
    
    Column space is point in string that is empty space and comes after a number
    """
    number_found = False
    column_space = start
    
    for char in x[start:]:
        if number_found:
            if char.isspace():
                break
        else:
            if char != "":
                number_found = True
        column_space += 1
                
    return column_space
                
                
    
def part_2():
    result = 0
    # Get stream for each line in file
    with open("day6/input.txt", "r") as file:
        lines = [line for line in file]
        raw_numbers = lines[0:-1]
        operations = lines[-1]
        
        columns = []
        column_number = 0
        start = 0
        
        while True:
            print(f"Processing {raw_numbers} from start: {start}")
            if len(raw_numbers[0]) <= start:
                break
            
            end = start
            for nums in raw_numbers:
                possible_column_space = get_column_space_position(nums, start=start)
                end = max(end, possible_column_space)
             
            new_column = [row[start:end] for row in raw_numbers]
            new_column.append(operations[start])
            start = end + 1
            column_number += 1
            columns.append(new_column)
            print(f"Found column space {new_column}")
               
            
            
            
    # print(f"Result is {result}")
    
part_2()         
