from model.algorithms.heap_sort import heap_sort
from model.algorithms.selection_sort import selection_sort
from model.algorithms.quick_sort import quicksort
from model.algorithms.bubble_sort import bubble_sort
from model.algorithms.insertion_sort import insertion_sort
from model.algorithms.merge_sort import merge_sort
from algorithms import Algorithms
import random

BASIC_SPEED = 50 #ms
class Model:
    def __init__(self):
        self.current_array = []

    def get_array(self):
        return self.current_array

    def generateRandomArray(self, l, min=10, max=100):
        self.current_array = [random.randint(min, max) for i in range(0, l)]
    
    def sort(self, method, update_callback, speed):
        if method == None or method == '':
            raise Exception('No sorting algorithm selected')

        delay = BASIC_SPEED * speed / 1000

        if Algorithms[method] == Algorithms.INSERTION_SORT:
            insertion_sort(self.current_array, update_callback, delay)
        if Algorithms[method] == Algorithms.MERGE_SORT:
            merge_sort(self.current_array, update_callback, delay)
        if Algorithms[method] == Algorithms.BUBBLE_SORT:
            bubble_sort(self.current_array, update_callback, delay)
        if Algorithms[method] == Algorithms.QUICK_SORT:
            quicksort(self.current_array, 0, len(self.current_array)-1, update_callback, delay)
        if Algorithms[method] == Algorithms.SELECTION_SORT:
            selection_sort(self.current_array, update_callback, delay)
        if Algorithms[method] == Algorithms.HEAP_SORT:
            heap_sort(self.current_array, update_callback, delay)