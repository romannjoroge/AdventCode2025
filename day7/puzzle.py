tachyon_manifold = []
tachyon_manifold_width = 0
tachyon_manifold_height = 0

import time
from collections import deque

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
    
node_index = {}

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
            if get_item_at_coordinate(x_graph=first_beam_x, y_graph=y_graph) == "^":
                root_splinter = Splinter(x_graph=first_beam_x, y_graph=y_graph)
                left_beam = Beam(parent_splinter=root_splinter, x=first_beam_x - 1)
                right_beam = Beam(parent_splinter=root_splinter, x=first_beam_x + 1)
                beams.add(left_beam)
                beams.add(right_beam)
                break
        
        # Build index table with all nodes and the nodes that they can reach
        print(f"Beams should only have first pair of beams {beams} and root splinter is {root_splinter}")
        
        
part_2()
    
    