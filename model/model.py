import random 

class Model:
    def __init__(self):
        self.current_array = []

    def get_array(self):
        return self.current_array

    def generateRandomArray(self, l, low=10, high=1000):
        self.current_array = [random.randint(low, high) for i in range(0, l)]