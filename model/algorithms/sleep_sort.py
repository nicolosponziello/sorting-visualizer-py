import time
from threading import Timer

def sleep_sort(array, update_func, delay):
    print(delay)
    res = []
    max_value = max(array)

    def add_element(el):
        res.append(el)
        update_func(res, [])
        if el == max_value:
            update_func(res, ['lightgreen' for _ in range(len(res))])

    for el in array:
        Timer(el * delay, add_element, [el]).start()

    time.sleep((delay * max(array)) / 1000)
    array.clear()
    for el in res:
        array.append(el)
    
