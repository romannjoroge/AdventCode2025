import pandas as pd
def g(x_graph: int, y_graph: int) -> int:
    """
    This function checks whether the item at coordinate (x_graph ,y_graph) is a roll of paper
    If it is a roll of paper it returns 1
    Else it returns 0
    """
    # x and y can only be 1 in a fixed range of values
    
    if (0 <= x_graph and x_graph <= width - 1) and (0 <= y_graph and y_graph <= height - 1) : 
        x_list = x_graph
        y_list = height - 1 - y_graph
        if (graph[y_list][x_list] == '@'):
            return 1
        
        return 0
    else:
        return 0
    
def r(x_graph: int, y_graph: int) -> int:
    """
    This function returns how many paper roles are around the item around (x_graph, y_graph)
    """
    
    return (g(x_graph=x_graph - 1, y_graph=y_graph + 1) +  
            g(x_graph=x_graph, y_graph=y_graph + 1) +
            g(x_graph=x_graph + 1, y_graph=y_graph + 1) +
            g(x_graph=x_graph - 1, y_graph=y_graph) +
            g(x_graph=x_graph + 1, y_graph=y_graph) +
            g(x_graph=x_graph + 1, y_graph=y_graph - 1) +
            g(x_graph=x_graph, y_graph=y_graph - 1) +
            g(x_graph=x_graph - 1, y_graph=y_graph - 1))
    
def a(x_graph: int, y_graph: int) -> int:
    """
    This function returns if the paper roll at position (x_graph, y_graph)
    is accessible by a forklift.
    
    A paper roll is accessible if there are less than 4 paper rolls around it.
    
    1 is returned if it is accessible otherwise 0 is returned
    
    If (x_graph, y_graph) is not a roll, ignore and return 0
    """
    is_position_role = g(x_graph=x_graph, y_graph=y_graph)
    if is_position_role == 0:
        return 0
    
    rolls_around_position = r(x_graph=x_graph, y_graph=y_graph)
    if rolls_around_position < 4:
        return 1
    else:
        return 0
    
def part_1():
    sum_reachable = 0
    for y_comp, row in enumerate(graph):
        y_graph = height - 1 - y_comp
        for x_graph, _ in enumerate(row):
            sum_reachable += a(x_graph=x_graph, y_graph=y_graph)
            
    print(f"The number of rolls that are reachable are {sum_reachable}")
    
# graph = [
#     "..@@.@@@@.",
#     "@@@.@.@.@@",
#     "@@@@@.@.@@",
#     "@.@@@@..@.",
#     "@@.@@@@.@@",
#     ".@@@@@@@.@",
#     ".@.@.@.@@@",
#     "@.@@@.@@@@",
#     ".@@@@@@@@.",
#     "@.@.@@@.@."
# ]
raw_input = pd.read_csv("day4/input.txt", header=None)
graph = raw_input[0]
width = len(graph[0])
height = len(graph)

x_graph = 5
y_graph = 4

print(f"Width is {width} and height is {height}")
print(f"g of Position at ({x_graph}, {y_graph}) is {g(x_graph=x_graph, y_graph=y_graph)}")
# print(f"The number of paper rolls around position ({x_graph}, {y_graph}) is {r(x_graph=x_graph, y_graph=y_graph)}")
# print(f"Is position ({x_graph, y_graph}) accessible by forklift {a(x_graph=x_graph, y_graph=y_graph)}")
part_1()


