from model.insertion_sort import insertion_sort
from model.merge_sort import merge_sort
from algorithms import Algorithms
import random
class Model:
    def __init__(self):
        self.current_array = []

    def get_array(self):
        return self.current_array

    def generateRandomArray(self, l, min=10, max=100):
        self.current_array = [random.randint(min, max) for i in range(0, l)]
    
    def sort(self, method):
        if method == None or method == '':
            raise Exception('No sorting algorithm selected')

        if Algorithms[method] == Algorithms.INSERTION_SORT:
            insertion_sort(self.current_array)
        if Algorithms[method] == Algorithms.MERGE_SORT:
            merge_sort(self.current_array, 0, len(self.current_array))