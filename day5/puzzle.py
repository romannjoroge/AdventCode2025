"""
This puzzle uses inequalities to find the solution
"""
class Inequality:
    def __init__(self, low: int, high: int):
        self.low = low
        self.high = high
        
    @classmethod
    def from_string(cls, inequality_string: str):
        """
        Function for parsing inequality from string
        
        inequality looks like this x - y where x is low number and y is the high number
        
        The function extracts x and y from string and makes class instance from this
        
        This function assumes that x is less than y
        """
        nums = inequality_string.split('-')
        if len(nums) != 2:
            raise "Invalid inequality string"
        
        x = int(nums[0])
        y = int(nums[1])
        
        assert x < y, "The first number in inequality should be lower than second"
        
        return cls(x, y)
    
    def __str__(self):
        """Returns a readable version of inequality that can be used by the print function"""
        return f"[{self.low}, {self.high}]"

unioned_inequalities = []

inequalities_input = ["3-5", "10-14", "16-20", "12-18"]

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
    print(f"Combining {inequality} to {unioned_inequalities}")
    
    
    # If unioned_inequalities is empty add inequality to list and end
    if len(unioned_inequalities) == 0:
        print(f"Inequality list was empty, adding {inequality} to list")
        unioned_inequalities.append(inequality)
        return
        
    
    # For each item in union inequalities list
    for index, item in enumerate(unioned_inequalities):
        # Determine the case of input and item
        pass
        
        # If case B move to next item
        
        # Else combine the inequalities
            # Set item to not case B
            # Remove item from list, replace input with combination, call again and return
            
    # Add inequality to list

def process_raw_inequalities():
    """
    This function processes inequalities input to get list of unioned inequalities
    """
    for raw_inequality in inequalities_input:
        pass
    

test_raw_inequality = "3-5"
test_inequality = Inequality.from_string(test_raw_inequality)
print(test_inequality)

test_inequality_2 = Inequality.from_string("4-5")

print(f"Is {test_inequality} and {test_inequality_2} in case B => {is_case_b(test_inequality, test_inequality_2)}")

# combine_inequalities(test_inequality)
# unioned_inequalities.append(test_inequality)

# test_raw_inequality_2 = "10-14"

