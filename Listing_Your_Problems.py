def count(sequence, item):
    """takes two arguments called sequence(list) and item. Return the number of times the item occurs in the list."""
    found=0
    for i in sequence:
        if i == item:
            found+=1
    return found


def median(some_list):
    """takes a list as an input and returns the median value of the list."""
    result = 0
    work_list = []
    work_list = sorted(some_list)
    list_length = len(work_list)
    if list_length%2==0:
        med_index_2 = list_length/2
        med_index_1 = med_index_2-1
        med_2 = work_list[med_index_2]
        med_1 = work_list[med_index_1]
        result = (med_1+med_2)/2.0
        return result
    else:
        med_index = (list_length/2)
        med = work_list[med_index]
        result = med
        return result
        
def remove_duplicates(some_list):
    """takes in a list and removes elements of the list that are the same."""
    new_list = []
    for i in some_list:
        if i not in new_list:
            new_list.append(i)
    return new_list
    
    
def product(list_of_int):
    """takes a list of integers as input and returns the product of all of the elements in the list. 
    For example: product([4, 5, 5]) should return 100 (because 4 * 5 * 5 is 100)."""
    result = 1
    for i in list_of_int:
        result = result*i
    return result
    
    
def purify(list_of_num):
    """takes in a list of numbers, removes all odd numbers in the list, and returns the result."""
    new_list = []
    for i in list_of_num:
        if i%2==0 and i!=1:
            new_list.append(i)
    return new_list
