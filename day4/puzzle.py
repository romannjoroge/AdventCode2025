import pandas as pd
import time

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
    
def print_graph():
    for row in graph:
        print(row)
        
def markRemoved(x_graph: int, y_graph: int):
    # x and y can only be 1 in a fixed range of values
    
    if (0 <= x_graph and x_graph <= width - 1) and (0 <= y_graph and y_graph <= height - 1) : 
        x_list = x_graph
        y_list = height - 1 - y_graph
        graph[y_list] = graph[y_list][:x_list] + "X" + graph[y_list][x_list + 1:]
    
removable_rolls = []
sum_removed = 0
def part_2():
    """
    Try removing as many rolls of paper as possible
    """
    global sum_removed
    
    print(f"\n INITIAL GRAPH")
    # print_graph()
    rolls_removed = 0
    
    while True:
        # Get a list of items that can be removed while counting them
        for y_comp, row in enumerate(graph):
            y_graph = height - 1 - y_comp
            for x_graph, _ in enumerate(row):
                if a(x_graph=x_graph, y_graph=y_graph):
                    rolls_removed += 1
                    sum_removed += 1
                    removable_rolls.append((x_graph, y_graph))
                    
                
        # Remove items that can be removed
        for removable in removable_rolls:
            markRemoved(x_graph=removable[0], y_graph=removable[1])
        
        print(f"The number of rolls that were removed this session {rolls_removed}")
        # print_graph()
        
        # If rolls_removed == 0 stop
        if rolls_removed == 0:
            break
        else:
            rolls_removed = 0
            
    print(f"Total number removed {sum_removed}")

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
# print_graph()


if __name__ == "__main__":
    start_time = time.perf_counter()
    part_2()
    end_time = time.perf_counter()
    print(f"Elapsed time is {(end_time - start_time):.4f}")


