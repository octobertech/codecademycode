def count(sequence, item):
    """takes two arguments called sequence(list) and item. Return the number of times the item occurs in the list."""
    found=0
    for i in sequence:
        if i == item:
            found+=1
    return found
