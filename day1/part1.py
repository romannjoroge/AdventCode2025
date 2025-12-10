import pandas as pd
def right(original: int, rotation: int) -> int:
    """
    Do the right operation, which is meant to increase number
    in safe.
    
    The result should be a number in interval [0, 99]
    
    We use 100 instead of 99 because we have 100 total numbers I 
    guess
    """
    return (original + rotation) % 100

def left(original: int, rotation: int) -> int:
    """
    Do left operation, which is meant to decrease number in safe
    
    The result is a number in interval [0, 99]
    
    We use 100 instead of 99 because we have 100 total numbers
    I guess
    """
    
    return (original - rotation) % 100

def operation_from_string(original: int, operation: str) -> int :
    """
    Operations are represented as either LX or RX. 
    
    LX represents a left operation of X while RX represents
    a right operation of X
    
    Where X is an integer
    
    This function performs this operation on the original and returns
    the result
    
    original: number to perform operation on
    operation: operation and amount to perform it on
    """
    splitIndex = 1 # Location of where numbers start
    operation_type = operation[:splitIndex]
    number = int(operation[splitIndex:])
    
    if (operation_type == "L"):
        return left(original=original, rotation=number)
    elif (operation_type == "R"):
        return right(original=original, rotation=number)
    else:
        raise "None supported operation"
    
    
# operations = [
#     "L68",
#     "L30",
#     "R48",
#     "L5",
#     "R60",
#     "L55",
#     "L1",
#     "L99",
#     "R14",
#     "L82"
# ]
# currentPos = 50

# print(f"The dial starts by point at {currentPos}")
# for operation in operations:
#     currentPos = operationFromString(original=currentPos, operation=operation)
#     print(f"The dial is rotated {operation} to point at {currentPos}")
    
# Import operations from file
operations = pd.read_csv('day1/input.txt', header=None)

# Go through all operations
num_time_at_zero = 0
current_step = 50
print(f"The dial starts at {current_step}")

for operation in operations[0]:
    # Update position
    current_step = operation_from_string(original=current_step, operation=operation)
    print(f"The dial is rotated {operation} to point at {current_step}")
    # If position = 0 update count
    if (current_step == 0):
        num_time_at_zero += 1
        
print(f"The code is {num_time_at_zero}")