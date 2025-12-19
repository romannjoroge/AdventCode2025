"""
This puzzle uses inequalities to find the solution
"""
class Inequality:
    def __init__(self, low: int, high: int):
        assert low <= high, "Low should be less than high"
        self.low = low
        self.high = high
        
    @classmethod
    def from_string(cls, inequality_string: str):
        """
        Function for parsing inequality from string
        
        inequality looks like this x - y where x is low number and y is the high number
        
        The function extracts x and y from string and makes class instance from this
        
        This function assumes that x is <= y
        """
        nums = inequality_string.split('-')
        if len(nums) != 2:
            raise "Invalid inequality string"
        
        x = int(nums[0])
        y = int(nums[1])
        
        assert x <= y, f"The first number in inequality {inequality_string} should be <= than second {x}, {y}"
        
        return cls(x, y)
    
    def test_number(self, num: int) -> bool:
        """This function tests if a number is in the range of inequality"""
        return self.high >= num >= self.low
    
    def __repr__(self):
        """Returns a readable version of inequality that can be used by the print function"""
        return f"[{self.low}, {self.high}]"

unioned_inequalities: list[Inequality] = []

def is_case_b(inequality1: Inequality, inequality2: Inequality) -> bool:
    """
    Function returns whether two inequalities are in case B
    
    For them to be in case B it means that there is no overlap between them
    """
    return (inequality1.high < inequality2.low) or (inequality2.high < inequality1.low)

def combine_inequalities(inequality: Inequality):
    """
    This function combines the given in equality to the list of unioned inequalites to get a new list of unioned inequalites
    """
    global unioned_inequalities
    # print(f"Combining {inequality} to {unioned_inequalities}")
    
    
    # If unioned_inequalities is empty add inequality to list and end
    if len(unioned_inequalities) == 0:
        # print(f"Inequality list was empty, adding {inequality} to list")
        unioned_inequalities.append(inequality)
        return
        
    
    # For each item in union inequalities list
    for index, item in enumerate(unioned_inequalities):
        # Determine the case of input and item
        if is_case_b(inequality1=inequality, inequality2=item):
            # If case B move to next item
            continue
        
        # Else combine the inequalities
        new_inequality_low = min(item.low, inequality.low)
        new_inequality_high = max(item.high, inequality.high)
        new_inequality = Inequality(new_inequality_low, new_inequality_high)
        # print(f"Inequality {inequality} could combine with {item} to form {new_inequality}")
        
        # Remove item from list, replace input with combination, call again and return
        del unioned_inequalities[index]
        combine_inequalities(new_inequality)
        return
            
    # Add inequality to list
    unioned_inequalities.append(inequality)
    # print(f"Inequality {inequality} has been added to list to make {unioned_inequalities}")

def process_raw_inequalities():
    """
    This function processes inequalities input to get list of unioned inequalities
    """
    for raw_inequality in inequalities_input:
        combine_inequalities(Inequality.from_string(raw_inequality))
        
    print(f"Final combined inequality is {unioned_inequalities}")
    
def part_1():
    num_fresh = 0
    # Get final combined inequality
    process_raw_inequalities()
    
    # Compare each ingredient id with union inequality
    for raw_ingredient in ingredient_ids:
        ingredient_id = int(raw_ingredient)
        for item in unioned_inequalities:
            if item.test_number(ingredient_id):
                num_fresh += 1
                break
    
    # Print solution
    print(f"\nNumber of fresh items is {num_fresh}")
 
blank_found = False   
inequalities_input = []
ingredient_ids = []
with open("day5/input.txt") as file:
    for line in file:
        formatted_line = line.strip()
        if (formatted_line == ""):
            blank_found = True
            continue
            
        if blank_found:
            ingredient_ids.append(formatted_line)
        else:
            inequalities_input.append(formatted_line)

# print(f"Extracted inequalities are {inequalities_input} and extracted ingredient_id are {ingredient_ids}")
part_1()