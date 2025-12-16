graph = []
def g(x_graph: int, y_graph: int) -> int:
    """
    This function checks whether the item at coordinate (x,y) is a roll of paper
    If it is a roll of paper it returns 1
    Else it returns 0
    """
    # x and y can only be 1 in a fixed range of values
    width = len(graph[0])
    height = len(graph)
    if (0 <= x_graph and x_graph <= width - 1) and (0 <= y_graph and y_graph <= height - 1) : 
        x_list = x_graph
        y_list = height - 1 - y_graph
        if (graph[y_list][x_list] == '@'):
            return 1
        
        return 0
    else:
        return 0
    
graph = [
    "..@@.@@@@.",
    "@@@.@.@.@@",
    "@@@@@.@.@@",
    "@.@@@@..@.",
    "@@.@@@@.@@",
    ".@@@@@@@.@",
    ".@.@.@.@@@",
    "@.@@@.@@@@",
    ".@@@@@@@@.",
    "@.@.@@@.@."
]

x_graph = 3
y_graph = 6

print(f"g of Position at ({x_graph}, {y_graph}) is {g(x_graph=x_graph, y_graph=y_graph)}")

