import time

def counting_sort(array, update_func, delay):

    max_value = max(array)

    count = [0]*(max_value+1)
    
    #build the counting array
    for el in array:
        count[el] += 1

    i = 0
    for a in range(max_value +1):
        for c in range(count[a]):
            array[i] = a
            i += 1
            update_func(array, ['yellow' if _ == i else 'lightblue' for _ in range(len(array))])
            time.sleep(delay)
    