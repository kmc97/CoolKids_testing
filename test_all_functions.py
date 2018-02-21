
import pytest
import math

from all_functions import Numbers

list_of_decimals = Numbers([1.23, 9, 6.97, 7, 27.01])
x = Numbers([1,2,-1,10])


def test_max_diff():
    maxdiff_output = x.maxdiff() 
    assert maxdiff_output == 11


def test_sum_list_integer():
    sum_ = x.sum_list()
    assert sum_ == 12


def test_sum_list_decimals():
    sum_ = list_of_decimals.sum_list()
    assert sum_ == 51.21

def test_min_max():
    min_max = x.find_min_max()
    assert min_max[0] == -1
    assert min_max[1] == 10


def test_tuple_size():
    min_max = x.find_min_max()
    assert len(min_max) == 2

def test_exception_type():
    with pytest.raises(TypeError):
        y = Numbers(['a',1,2])
        sum_ = y.sum_list()

    
def test_exception_value():
    with pytest.raises(ValueError):
        y = Numbers([1, math.sqrt(-12), 3])
        sum_ = y.sum_list()
        min_max = y.find_min_max()
        maxdiff_output = y.maxdiff()

def test_exception_import():
    with pytest.raises(ImportError):
        import ThisIsNotaFile

