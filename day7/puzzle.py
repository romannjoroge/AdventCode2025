def part_1():
    """
    Counts the number of times splinter is in path of beam
    """
    num_times_splinter_in_path = 0
    
    with open("day7/input.txt", 'r') as file:
        tachyon_manifold = [line.strip() for line in file]
        print(tachyon_manifold)
        
part_1()