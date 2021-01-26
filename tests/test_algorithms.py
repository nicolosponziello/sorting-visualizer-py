import unittest
import random
from model.algorithms.insertion_sort import insertion_sort
from model.algorithms.bubble_sort import bubble_sort
from model.algorithms.counting_sort import counting_sort
from model.algorithms.heap_sort import heap_sort
from model.algorithms.merge_sort import merge_sort
from model.algorithms.quick_sort import quicksort
from model.algorithms.selection_sort import selection_sort

def test_func(a, b):
    pass

class TestAlgorithms(unittest.TestCase):
    
    def test_insertion_sort(self):
        array = [random.randint(10, 100) for _ in range(100)]
        sorted_arr = sorted(array)
        self.assertNotEqual(array, sorted_arr)
        insertion_sort(array, test_func, 0)
        self.assertEqual(sorted_arr, array)
    
    def test_bubble_sort(self):
        array = [random.randint(10, 100) for _ in range(100)]
        sorted_arr = sorted(array)
        self.assertNotEqual(array, sorted_arr)
        bubble_sort(array, test_func, 0)
        self.assertEqual(sorted_arr, array)
    
    def test_counting_sort(self):
        array = [random.randint(10, 100) for _ in range(100)]
        sorted_arr = sorted(array)
        self.assertNotEqual(array, sorted_arr)
        counting_sort(array, test_func, 0)
        self.assertEqual(sorted_arr, array)
    
    def test_heap_sort(self):
        array = [random.randint(10, 100) for _ in range(100)]
        sorted_arr = sorted(array)
        self.assertNotEqual(array, sorted_arr)
        heap_sort(array, test_func, 0)
        self.assertEqual(sorted_arr, array)
    
    def test_merge_sort(self):
        array = [random.randint(10, 100) for _ in range(100)]
        sorted_arr = sorted(array)
        self.assertNotEqual(array, sorted_arr)
        merge_sort(array, test_func, 0)
        self.assertEqual(sorted_arr, array)
    
    def test_quick_sort(self):
        array = [random.randint(10, 100) for _ in range(100)]
        sorted_arr = sorted(array)
        self.assertNotEqual(array, sorted_arr)
        quicksort(array, 0, len(array)-1, test_func, 0)
        self.assertEqual(sorted_arr, array)
    
    def test_selection_sort(self):
        array = [random.randint(10, 100) for _ in range(100)]
        sorted_arr = sorted(array)
        self.assertNotEqual(array, sorted_arr)
        selection_sort(array, test_func, 0)
        self.assertEqual(sorted_arr, array)