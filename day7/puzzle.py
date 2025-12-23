tachyon_manifold = []
tachyon_manifold_width = 0
tachyon_manifold_height = 0

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
            
        print(f"Found beams {beams}")        
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
                        
                    print(f"New beams {beams} at y {y_graph} split at {beam}")

part_1()