import numpy as np
import random
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
    pass
    
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
    return total_distance


def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """
    new_road_map = road_map
    new_road_map[index1],new_road_map[index2]=new_road_map[index2],new_road_map[index1]
    new_total_distance = 0
    for i in range(len(new_road_map)):
        loc1=np.array((new_road_map[i%len(new_road_map)][2], new_road_map[i%len(new_road_map)][3]))
        loc2= np.array((new_road_map[(i+1)%len(new_road_map)][2], new_road_map[(i+1)%len(new_road_map)][3]))
        dist = np.linalg.norm(loc1-loc2)
        new_total_distance += dist
    return new_road_map,new_total_distance


def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """
    new_road_map = road_map
    last=new_road_map[-1] 
    new_road_map[1:] = new_road_map[:-1] 
    new_road_map[0] = last
    return new_road_map


def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    N = 50
    number1 = N * random.random()
    number2 = N * random.random()
    index1= int(number1)
    index2= int(number2)
    best_cycle = road_map
    best_distance = compute_total_distance(road_map)
    road_map_shift = road_map
    road_map_swap = road_map
    for i in range(10000):
        (road_map_swap,distance_swap) = swap_cities(road_map_swap, index1, index2)
        road_map_shift= shift_cities(road_map_shift)
        distance_shift = compute_total_distance(road_map_shift)
        map_distance = [road_map_swap,distance_swap] if distance_swap <= distance_shift else [road_map_shift,distance_shift]
        if map_distance[1] < best_distance:
            best_cycle = map_distance[0]
            best_distance = map_distance[1]
    return best_cycle
    pass


def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """
    total_distance= 0
    print ("City       Connection    Cost")
    for i in range(len(road_map)):
        loc1=np.array((road_map[i%len(road_map)][2], road_map[i%len(road_map)][3]))
        loc2= np.array((road_map[(i+1)%len(road_map)][2], road_map[(i+1)%len(road_map)][3]))
        dist = np.linalg.norm(loc1-loc2)
        print ("{:<14}{:<11}{}".format(road_map[i][1],road_map[(i+1)%len(road_map)][1],dist))
        total_distance += dist
    print("Total cost is=", total_distance)
    pass


def get_longitude(city):
    """
    Longitude coordinate of the city
    """
    return int(city[3])


def get_latitude(city):
    """
    Latitude coordinate of the city
    """
    return int(city[2])


def visualise(road_map):
    """
    This prints a matrix of -1s and replaces city coordinates with the city index
    """
    longitude = {
        'min': get_longitude(min(road_map, key=get_longitude)),
        'max': get_longitude(max(road_map, key=get_longitude))
    }

    latitude = {
        'min': get_latitude(min(road_map, key=get_latitude)),
        'max': get_latitude(max(road_map, key=get_latitude))
    }

    grid = [-1] * (longitude['max'] - longitude['min'] + 1)
    for i in range(len(grid)):
        grid[i] = [-1] * (latitude['max'] - latitude['min'] + 1)

    print('grid: ' + str(len(grid)) + 'x' + str(len(grid[0])))

    for index, city in enumerate(road_map, start=1):
        x = get_longitude(city) - longitude['min']
        y = get_latitude(city) - latitude['min']
        print('city: (' + str(x) + ',' + str(y) + ')')

        grid[x][y] = index

    return grid, longitude, latitude


def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    road_map = read_cities('city-data.txt')
    print(print_cities(road_map))
    print(find_best_cycle(road_map))
    pass


if __name__ == "__main__": #keep this in
    main()
