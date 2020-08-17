# parameters that we're worried about are weight limit represented as "limit",
# weights of items "weights" and length of list
# Your code here


def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    new_dict = {}
    # iterate through weights of items
    for i in range(length):
        # if weight limit - weight at index i is in dictionary then we set key equal to it
        if limit - weights[i] in new_dict:
            k = limit - weights[i]
            # then we set i2 to be the new_dict value at key
            i2 = new_dict[k]
            # return the tuple (i, i2)
            return [i, i2]
        # set new_dict at weight index to i
        new_dict[weights[i]] = i

    return None
