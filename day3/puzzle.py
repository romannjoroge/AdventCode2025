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

list_string = '987654321111111'
list_int = [int(s) for s in list_string]
print(f"Largest number is {find_largest_number(list_int)} for {list_int}")