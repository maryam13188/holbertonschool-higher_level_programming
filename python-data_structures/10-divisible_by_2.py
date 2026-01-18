def divisible_by_2_alt3(my_list=[]):
    """Using while loop."""
    result = []
    i = 0
    while i < len(my_list):
        result.append(my_list[i] % 2 == 0)
        i += 1
    return result
