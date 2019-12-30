import pytest
from cities import *


def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    assert compute_total_distance(road_map1)==\
           pytest.approx(9.386+18.496+10.646, 0.01)

    '''add your further tests'''

def test_swap_cities():
    '''add your tests'''
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755)]
    road_map2= [("Delaware", "Dover", 39.161921, -75.526755),\
                ("Kentucky", "Frankfort", 38.197274, -84.86311)]
    assert swap_cities(road_map1)\
           road_map1[0]==road_map2[0]\
           road_map1[1]==road_map2[1]   

def test_shift_cities():
    '''add your tests'''
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    road_map2 = [("Minnesota", "Saint Paul", 44.95, -93.094),\
                ("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755)]
    assert shift_cities(road_map1)\
           road_map1[0]==road_map2[1]\
           road_map1[1]==road_map2[2]\
           road_map1[2]==road_map2[0]
    
def read_cities():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    assert road_map[16]==road_map1[0]\
           road_map[7]==road_map1[1]\
           road_map[22]==road_map1[2]

def print_cities():
    pass

def find_best_cycle():
    pass

def print_map():
    pass

def main():
    pass
    
    
