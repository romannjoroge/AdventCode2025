tachyon_manifold = []
tachyon_manifold_width = 0
tachyon_manifold_height = 0

import time

def get_item_at_coordinate(x_graph: int, y_graph: int) -> str:
    """
    Get's the item at a coordinate. Item can either be S, . or ^
    """
    x_list = x_graph
    y_list = tachyon_manifold_height - 1 - y_graph
    return tachyon_manifold[y_list][x_list]

def part_1():
    """
    Counts the number of times splinter is in path of beam
    """
    global tachyon_manifold_width
    global tachyon_manifold
    global tachyon_manifold_height
    
    num_times_splinter_in_path = 0
    beams = set()
    
    with open("day7/input.txt", 'r') as file:
        tachyon_manifold = [line.strip() for line in file]
        tachyon_manifold_height = len(tachyon_manifold)
        tachyon_manifold_width = len(tachyon_manifold[0])
        
        # Find starting coordinate assuming it's at y = height
        for x_graph in range(tachyon_manifold_width):
            if get_item_at_coordinate(x_graph=x_graph, y_graph=tachyon_manifold_height - 1) == "S":
                # Insert a beam
                beams.add(x_graph)
                break
            
        # print(f"Found beams {beams}")        
        # Find colliding splinters for each beam
        for y_graph in range(tachyon_manifold_height - 2, -1, -1):
            # For each beam check if there is a splinter at corresponding y and x
            beams_iter = list(beams)
            for beam in beams_iter:
                if get_item_at_coordinate(x_graph=beam, y_graph=y_graph) == "^":
                    # Remove old beam and add collission
                    beams.remove(beam)
                    num_times_splinter_in_path += 1
                    
                    # Add 2 new beams if within range
                    left_beam = beam - 1
                    right_beam = beam + 1
                    
                    if 0 <= left_beam:
                        beams.add(left_beam)
                    if right_beam <= tachyon_manifold_width:
                        beams.add(right_beam)
                        
                    # print(f"New beams {beams} at y {y_graph} split at {beam}")
                    
        print(f"Has split {num_times_splinter_in_path} times")
        
class Node:
    def __init__(self, x_graph: int):
        self.x_graph = x_graph
        self.left = None
        self.right = None
        
    def assign_left(self, left: 'Node'):
        self.left = left
        
    def assign_right(self, right: 'Node'):
        self.right = right

def get_num_paths_from_node(node: Node) -> int:
    """
    Function for recursively getting number of paths in node by recursively
    adding up number of paths from children
    """
    sum = 0
    
    if node.left == None:
        sum += 1
    else:
        sum += get_num_paths_from_node(node.left)
        
    if node.right == None:
        sum += 1
    else:
        sum += get_num_paths_from_node(node.right)
        
    return sum
    

        
def part_2():
    """
    Counts the number of paths that the particle could have used
    """
    global tachyon_manifold_width
    global tachyon_manifold
    global tachyon_manifold_height
    
    beams = set[Node]()
    
    with open("day7/input.txt", 'r') as file:
        tachyon_manifold = [line.strip() for line in file]
        tachyon_manifold_height = len(tachyon_manifold)
        tachyon_manifold_width = len(tachyon_manifold[0])
        
        root_node = None
        
        # Find starting coordinate assuming it's at y = height
        for x_graph in range(tachyon_manifold_width):
            if get_item_at_coordinate(x_graph=x_graph, y_graph=tachyon_manifold_height - 1) == "S":
                # Insert a beam
                root_node = Node(x_graph=x_graph)
                beams.add(root_node)
                break
            
        # print(f"Found beams {beams}")        
        # Find colliding splinters for each beam
        for y_graph in range(tachyon_manifold_height - 2, -1, -1):
            # For each beam check if there is a splinter at corresponding y and x
            beams_iter = list(beams)
            for beam in beams_iter:
                if get_item_at_coordinate(x_graph=beam.x_graph, y_graph=y_graph) == "^":
                    # Remove old beam and add collission
                    beams.remove(beam)
                   
                    # Add 2 new beams if within range
                    left_beam = beam.x_graph - 1
                    right_beam = beam.x_graph + 1
                    
                    if 0 <= left_beam:
                        left_child = Node(left_beam)
                        beam.assign_left(left_child)
                        beams.add(left_child)
                    if right_beam <= tachyon_manifold_width:
                        right_child = Node(right_beam)
                        beam.assign_right(right_child)
                        beams.add(right_child)
                        
                    # print(f"New beams {beams} at y {y_graph} split at {beam}")
        
        print("Processing nodes")
                    
        

# start_time = time.perf_counter()
# part_1()
# end_time = time.perf_counter()
# elapsed_time = end_time - start_time
# print(f"My code took {elapsed_time:.4f} seconds")

# part_2()
test_node = Node(1)
test_right_child_node = Node(2)
test_node.assign_right(test_right_child_node)
test_left_child_node = Node(3)
test_node.assign_left(test_left_child_node)
test_right_grandchild_node = Node(4)
test_right_child_node.assign_right(test_right_grandchild_node)
print(f"Sum of paths from test node is {get_num_paths_from_node(test_node)}")