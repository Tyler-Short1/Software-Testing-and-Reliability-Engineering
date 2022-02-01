import pytest
from Car import Car

def test_currentspeed():
    car_1 = Car(20, 90, 80)
    assert car_1.currentspeed == 20

def test_maxspeed():
    car_1 = Car(20, 90, 80)
    assert car_1.maxspeed == 90

def test_fuellevel():
    car_1 = Car(20, 90, 80)
    assert car_1.fuellevel == 80

def test_refuel():
    car_1 = Car(20, 90, 80)
    car_1.refuel(10)
    assert car_1.fuellevel == 90