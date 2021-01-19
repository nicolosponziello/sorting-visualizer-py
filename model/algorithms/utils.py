import random

def generate_array(l, low=10, high=1000):
    return [random.randint(low, high) for i in range(0, l)]