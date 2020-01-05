def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return 
    them as a list of four-tuples: 

      [(state, city, latitude, longitude), ...] 

    Use this as your initial `road_map`, that is, the cycle 

      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """
    road_map = []
    with open(file_name, 'r') as f:
      for line in f:
        tmp = line.split("\t")
        road_map.append((tmp[0], tmp[1], float(tmp[2]), float(tmp[3])))
    return road_map

def print_cities(road_map):
    """
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    """
    for t in road_map:
      print(f'{t[1]} ({t[2]:.2f}, {t[3]:.2f})')
     
def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    total_distance = 0
    for i in range(len(road_map)):
        loc1=np.array((road_map[i%len(road_map)][2], road_map[i%len(road_map)][3]))
        loc2= np.array((road_map[(i+1)%len(road_map)][2], road_map[(i+1)%len(road_map)][3]))
        dist = np.linalg.norm(loc1-loc2)
        total_distance += dist
    print(total_distance)

def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """

def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """
    last=road_map[-1] 
    road_map[1:] = road_map[:-1] 
    road_map[0] = last
    print(road_map)

def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    pass

def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """
    pass

def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    road_map = read_cities('city-data.txt')
    print_cities(road_map)
    compute_total_distance(road_map)
    pass

if __name__ == "__main__": #keep this in
    main()
