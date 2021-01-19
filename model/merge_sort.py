def merge_sort(array, left_index, right_index):
    if left_index >= right_index:
        return
    #find the middle point
    middle = (left_index + right_index) // 2
    #recursively sort first half
    merge_sort(array, left_index, middle)
    #recursively sort second half
    merge_sort(array, middle + 1, right_index)

    #merge the halves
    merge(array, left_index, middle, right_index)

def merge(array, left_index, middle, right_index):
    left_array = array[left_index:middle+1]
    right_array = array[middle+1:right_index+1]

    i = 0
    k = 0
    j = 0

    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    while i < len(left_array):
        array[k] = left_array[i]
        i += 1
        k += 1
    
    while j < len(right_array):
        array[k] = right_array[j]
        j += 1
        k += 1
