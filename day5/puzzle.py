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

def combine_inequalities(inequality: Inequality):
    """
    This function combines the given in equality to the list of unioned inequalites to get a new list of unioned inequalites
    """

def process_raw_inequalities():
    """
    This function processes inequalities input to get list of unioned inequalities
    """
    for raw_inequality in inequalities_input:
        pass
    

test_raw_inequality = "310-500"
test_inequality = Inequality.from_string(test_raw_inequality)
print(test_inequality)
