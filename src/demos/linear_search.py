def iterative_search(items, target): # O(n)
    # iterate over all items
    for item in range(len(items) - 1, 0, -1):
        # if our target is equal to our item
        if target == items[item]:
            # return True to the caller
            return True
    # return False
    return False

def recursive_search(items, target): # O(n)
    # some sort of base case / break put clause
    # if we pass in an empty array?
    if len(items) == 0:
        # return False to the caller
        return False

    # is our item at the end of items
    # equal to target?
    if items[-1] == target:
        # return True to the caller
        return True

    # recursive call
    # return a recursive call using a slice of the items
    # from the beginning of list to all but the last one
    # passing on the target
    return recursive_search(items[:-1], target)