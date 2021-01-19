import random 

class Model:
    def __init__(self):
        pass

    def getRandomArray(self, l, low=10, high=1000):
        return [random.randint(low, high) for i in range(0, l)]