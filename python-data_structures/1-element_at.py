#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Retrieve an element from a list at a specific index
    
    Args:
        my_list: The list to retrieve from
        idx: The index of the element to retrieve
        
    Returns:
        The element at index idx, or None if idx is out of range or negative
    """
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return None
    
    # Return the element at the specified index
    return my_list[idx]


# Test function
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    
    # Test cases
    print("Element at index 0 is", element_at(my_list, 0))      # Expected: 1
    print("Element at index 2 is", element_at(my_list, 2))      # Expected: 3
    print("Element at index 4 is", element_at(my_list, 4))      # Expected: 5
    print("Element at index 5 is", element_at(my_list, 5))      # Expected: None (out of range)
    print("Element at index -1 is", element_at(my_list, -1))    # Expected: None (negative)
    print("Element at index 3 is", element_at(my_list, 3))      # Expected: 4
