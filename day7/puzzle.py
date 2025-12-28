tachyon_manifold = []
tachyon_manifold_width = 0
tachyon_manifold_height = 0

import time
from collections import deque, defaultdict

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

class Splinter:
    def __init__(self, x_graph: int, y_graph: int):
        self.x = x_graph
        self.y = y_graph
        
    def __repr__(self):
        return f"Splinter at ({self.x}, {self.y})"
    
    @classmethod
    def from_id(cls, id: str):
        coordinates = id.split(',')
        assert len(coordinates) >= 2 , "Invalid id"
        x_graph = int(coordinates[0])
        y_graph = int(coordinates[1])
        return cls(x_graph=x_graph, y_graph=y_graph)
    
    def to_id(self) -> str:
        return f"{self.x},{self.y}"
    
    def __eq__(self, other):
        if other == None:
            return False
        if isinstance(other, Splinter):
            return self.x == other.x and self.y == other.y
        
    def __hash__(self):
        return hash(self.to_id())
    
class Beam:
    def __init__(self, parent_splinter: Splinter, x: int):
        self.parent = parent_splinter
        self.x = x
    
    def __repr__(self):
        if self.parent == None:
            return "The first beam"
        return f"Beam that came from {self.parent} with x = {self.x}"
    
    def __eq__(self, other):
        if other == None:
            return False
        if isinstance(other, Beam):
            return self.parent == other.parent and self.x == other.x
        
    def __hash__(self):
        return hash((self.parent, self.x))
    
class Node:
    def __init__(self, splinter: Splinter):
        self.splinter = splinter
        self.left = None
        self.right = None
        
    def assing_left_child(self, left: 'Node'):
        self.left = left
        
    def assign_right_child(self, right: 'Node'):
        self.right = right
        
    def __repr__(self):
        return f"Node at {self.splinter}"

calculated_paths = defaultdict(int)
def get_num_paths_from_node(node: Node) -> int:
    """
    Function for recursively getting number of paths in node by recursively
    adding up number of paths from children
    """
    if calculated_paths[node.splinter.to_id()] != 0:
        return calculated_paths[node.splinter.to_id()]
    
    total = 0
    print(f"Getting number of paths from {node} with left {node.left} and right {node.right}")
    
    if node.left == None:
        total += 1
        print(f"No left child just add 1 to get sum {total}")
    else:
        additon = get_num_paths_from_node(node.left)
        total += additon
        print(f"{node} Getting for sum of {node.left} = {additon} to get sum {total}")
        
        
    if node.right == None:
        total += 1
        print(f"No right child just adding 1 to sum to get {total}")
    else:
        addition = get_num_paths_from_node(node.right)
        total += addition
        print(f"{node} Gettign sum for right {node.right} = {addition} to get sum {total}")
        
        
    calculated_paths[node.splinter.to_id()] = total
    return total

visited_children: list[Node] = []

def get_left_child(node: Node) -> Node | None:
    children: list[Splinter] = node_index[node.splinter.to_id()]
    if len(children) == 0:
        return None
    elif len(children) == 1:
        child = children[0]
        if child.x < node.splinter.x:
            return Node(splinter=child)
        else:
            return None
    else:
        for child in children:
            if child.x < node.splinter.x:
                return Node(splinter=child)
            
        return None
    
def get_right_child(node: Node) -> Node | None:
    children: list[Splinter] = node_index[node.splinter.to_id()]
    if len(children) == 0:
        return None
    elif len(children) == 1:
        child = children[0]
        if child.x > node.splinter.x:
            return Node(splinter=child)
        else:
            return None
    else:
        for child in children:
            if child.x > node.splinter.x:
                return Node(splinter=child)
            
        return None

def return_if_node_in_visited(node: Node) -> bool:
    global visited_children
    
    in_visited = False
    for visited in visited_children:
        if visited.splinter == node.splinter:
            in_visited = True
            break
        
    return in_visited

def build_tree(node: Node):
    """
    Function that builds tree from a node
    """
    global visited_children
    print(f"Processing node {node}")
    
    left_child = get_left_child(node=node)
    right_child = get_right_child(node=node)
    
    if left_child:
        print(f"{node} has left child {left_child}")
        node.assing_left_child(left_child)
        if return_if_node_in_visited(left_child) == False:
            # print(f"Left child {left_child} was not in {visited_children}")
            build_tree(left_child)
    if right_child:
        print(f"{node} has right child {right_child}")
        node.assign_right_child(right=right_child)
        if return_if_node_in_visited(right_child) == False:
            # print(f"Right child {right_child} was not in {visited_children}")
            build_tree(node=right_child)

    visited_children.append(node)        
    
node_index = defaultdict(list)

def print_tree(node: Node):
    """
    Print's tree by getting children at each level of manifold
    """
    line_level = node.splinter.y
    queue: set[Node] = [node]
    
    def add_node_queue(node: Node):
        """
        Adds node to queue in a way that respects line level and order of arrival in queue
        """
        if node == None:
            return 
        
        if len(queue) == 0:
            queue.append(node)
        else:
            item_added = False
            for index, item in enumerate(queue):
                if item.splinter.y < node.splinter.y:
                    queue.insert(index, node)
                    item_added = True
                    break
                
            if item_added == False:
                queue.append(node)
    
    while line_level >= 0:
        nodes_x_in_level = []
        first_item: Node = None
        # Get first item in queue
        if len(queue) > 0:
            first_item: Node = queue[0]
        else:
            break
        
        
        # If first item is at line level add it to list
        while first_item.splinter.y == line_level:
            nodes_x_in_level.append(first_item.splinter.x)
            # Pop first item and add its adjecent children to queue
            queue.remove(first_item)
            add_node_queue(first_item.left)
            add_node_queue(first_item.right)
            if len(queue) > 0:
                first_item = queue[0]
            else:
                break
            
        string_to_print = ""
        for x_graph in range(tachyon_manifold_width):
            if x_graph in nodes_x_in_level:
                string_to_print += '^'
            else:
                string_to_print += ' '
                
        print(string_to_print)
        line_level -= 1

def part_2():
    """
    Solving part 2
    """
    
    global tachyon_manifold_width
    global tachyon_manifold
    global tachyon_manifold_height
    
    beams: set[Beam] = set()
    
    # Input data
    with open("day7/input.txt", 'r') as file:
        tachyon_manifold = [line.strip() for line in file]
        tachyon_manifold_height = len(tachyon_manifold)
        tachyon_manifold_width = len(tachyon_manifold[0])
        
        first_beam_x = 0
    
        # Get first beam
        for x_graph in range(tachyon_manifold_width):
            if get_item_at_coordinate(x_graph=x_graph, y_graph=tachyon_manifold_height - 1) == "S":
                # Insert a beam
                first_beam_x = x_graph
                break
        
        # Find root node
        root_splinter = None
        for y_graph in range(tachyon_manifold_height - 2, -1, -1):
            if len(beams) == 0:
                if get_item_at_coordinate(x_graph=first_beam_x, y_graph=y_graph) == "^":
                    # print(f"No beams so far looking for root splinter at y = {y_graph}")
                    root_splinter = Splinter(x_graph=first_beam_x, y_graph=y_graph)
                    left_beam = Beam(parent_splinter=root_splinter, x=first_beam_x - 1)
                    right_beam = Beam(parent_splinter=root_splinter, x=first_beam_x + 1)
                    beams.add(left_beam)
                    beams.add(right_beam)
            else:
                beams_iter = list(beams)
                # print(f"More than one beam {beams_iter} at y = {y_graph}")
                for beam in beams_iter:
                    # If there is a splinter at y level remove beam from set
                    if get_item_at_coordinate(x_graph=beam.x, y_graph=y_graph) == "^":
                        beams.remove(beam)
                        new_splinter = Splinter(x_graph=beam.x, y_graph=y_graph)
                        # print(f"New splinter found {new_splinter}")
                    
                        # Mark that parent splinter can reach this current splinter
                        node_index[beam.parent.to_id()].append(new_splinter)
                        
                        # Insert 2 beams coming from new splinter
                        left_beam_x = new_splinter.x - 1
                        right_beam_x = new_splinter.x + 1
                        
                        if 0 <= left_beam_x:
                            left_beam = Beam(parent_splinter=new_splinter, x=left_beam_x)
                            # print(f"Adding left beam from splinter")
                            beams.add(left_beam)
                        if right_beam_x <= tachyon_manifold_width:
                            right_beam = Beam(parent_splinter=new_splinter, x = right_beam_x)
                            # print(f"Adding right child from splinter")
                            beams.add(right_beam)
        
        # Build index table with all nodes and the nodes that they can reach
        # print(f"Beams should only have first pair of beams {beams} and root splinter is {root_splinter}")
        print(f"Root splinter is: {root_splinter}")
        print(f"\nThe Node Lookup Table\n")
        print(node_index)
        
        # Construct tree from lookup table
        root_node = Node(splinter=root_splinter)
        build_tree(root_node)
        
        print(f"\nConstructed Tree\n")
        print_tree(root_node)
        
        print(f"Number paths: {get_num_paths_from_node(root_node)}")
        
part_2()
    
    