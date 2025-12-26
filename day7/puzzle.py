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
    def __init__(self, x_graph: int, y_graph: int):
        self.y_graph = y_graph
        self.x_graph = x_graph
        self.left = None
        self.right = None
        
    def assign_left(self, left: 'Node'):
        self.left = left
        
    def assign_right(self, right: 'Node'):
        self.right = right
        
    def __repr__(self):
        return f"Node with coordinate ({self.x_graph}, {self.y_graph})"
    
    def __eq__(self, other):
        if other == None:
            return False
        elif not isinstance(other, Node):
            return False
        return self.y_graph == other.y_graph and self.x_graph == other.x_graph
    
    def __hash__(self):
        return hash((self.x_graph, self.y_graph))
    
class Beam:
    def __init__(self, x_graph: int, parent_node: Node):
        self.x_graph = x_graph
        self.parent_node = parent_node
        
    def __repr__(self):
        return f"Beam: x = {self.x_graph} from {self.parent_node}"
    
    def __eq__(self, other):
        if other == None:
            return False
        elif not isinstance(other, Beam):
            return False
        return self.x_graph == other.x_graph and self.parent_node == other.parent_node
    
    def __hash__(self):
        return hash((self.x_graph, self.parent_node))

def get_num_paths_from_node(node: Node) -> int:
    """
    Function for recursively getting number of paths in node by recursively
    adding up number of paths from children
    """
    print(f"Getting number of points for node ({node.x_graph}, {node.y_graph})")
    sum = 0
    
    if node.left == None:
        sum += 1
        print(f"Node has no left child adding 1 to sum {sum}")
    else:
        sum += get_num_paths_from_node(node.left)
        print(f"Node had left child {node.left} making new sum {sum}")
        
    if node.right == None:
        sum += 1
        print(f"Node had no right child, adding 1 to make sum {sum}")
    else:
        sum += get_num_paths_from_node(node.right)
        print(f"Node had right child {node.right} adding its sum to get {sum}")
        
    return sum

def find_left_right_child(node: Node):
    """
    Gets the left and right child of a node
    """
    left_child_x = node.x_graph - 1
    right_child_x = node.x_graph + 1
    
    # If possible left and right child x within tachyeon manifold look for them
    if 0 <= left_child_x:
        left_found = False
        for y_graph in range(node.y_graph, -1, -1):
            if get_item_at_coordinate(x_graph=left_child_x, y_graph=y_graph) == "^":
                node.assign_left(Node(x_graph=left_child_x, y_graph=y_graph))
                left_found = True
                break
                      
        if left_found == False:
            node.assign_left(None)
    else:
        node.assign_left(None)
    if right_child_x <= tachyon_manifold_width:
        right_found = False
        for y_graph in range(node.y_graph, -1, -1):
            if get_item_at_coordinate(x_graph=right_child_x, y_graph=y_graph) == "^":
                node.assign_right(Node(x_graph=right_child_x, y_graph=y_graph))
                right_found = True
                break
            
        if right_found == False:
            node.assign_right(None)
    else:
        print(f"Right child x is {right_child_x} is {tachyon_manifold_width}")
        node.assign_right(None)
    
def part_2():
    global tachyon_manifold_width
    global tachyon_manifold
    global tachyon_manifold_height
    
    # Get tree with possible paths
    root_node = None
    first_beam_x = None
    # Import data
    with open("day7/input.txt", 'r') as file:
        tachyon_manifold = [line.strip() for line in file]
        tachyon_manifold_height = len(tachyon_manifold)
        tachyon_manifold_width = len(tachyon_manifold[0])
        
        # Find coordinate of first beam
        for x_graph in range(tachyon_manifold_width):
            if get_item_at_coordinate(x_graph=x_graph, y_graph=tachyon_manifold_height - 1) == "S":
                # Insert a beam
                first_beam_x = x_graph
                break
        
        # Find root node
        for y_graph in range(tachyon_manifold_height - 2, -1, -1):
            if get_item_at_coordinate(x_graph=first_beam_x, y_graph=y_graph) == "^":
                root_node = Node(x_graph=first_beam_x, y_graph=y_graph)
                break
        
    
    print(f"Root node is {root_node} and x coordinate of first beam is {first_beam_x}")
    find_left_right_child(root_node)
    print(f"Left child of node is {root_node.left} and right child of node is {root_node.right}")
    # Calculate all possible paths
                    
        

# start_time = time.perf_counter()
# part_1()
# end_time = time.perf_counter()
# elapsed_time = end_time - start_time
# print(f"My code took {elapsed_time:.4f} seconds")

part_2()