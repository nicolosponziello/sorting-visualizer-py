import time

def heapify(array, length, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < length and array[i] < array[left]:
        largest = left
    
    if right < length and array[largest] < array[right]:
        largest = right

    #change root
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, length, largest)

def heap_sort(array, update_func, delay):
    length = len(array)

    #build max-heap
    for i in range(length // 2 - 1, -1, -1):
        heapify(array, length, i)
    
    #sort
    for i in range(length-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        update_func(array, ['yellow' if _ == i else 'lightblue' for _ in range(length)])
        time.sleep(delay)
        heapify(array, i, 0)
    
    update_func(array, ['lightgreen' for _ in range(length)])