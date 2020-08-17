def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create an index of values
    index = {}
    # create a list where we will add matching numbers
    result = []
    # first loop through the arrays
    for array in arrays:
        # now we loop through the numbers within each array
        for int in array:
            # if the num is already in the index of values we count
            if int in index:
                index[int] += 1
                # if num equals the length then we add it to result because we know it's in all lists
                if index[int] == len(arrays):
                    result.append(int)
            # otherwise we set it equal to 1
            else:
                index[int] = 1

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
