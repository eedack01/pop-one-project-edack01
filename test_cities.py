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
    assert swap_cities(road_map1,0,1)\
    	== pytest.approx(new_road_map, new_total_distance,0.01)

def test_shift_cities():
    '''add your tests'''
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    assert shift_cities(road_map1)\
           == road_map1
    road_map2 = [("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    assert shift_cities(road_map2)\
           == road_map2

    
