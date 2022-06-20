""" Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures? 
"""

def is_unique(string):
    """ Return True if the string has all unique characters. Return False otherwise. """

    # 1. First approach:
    # Convert the string to a set and compare the length of the string vs the length of the set
    # If the same length -> unique characters -> True. Otherwise, False

    # return len(string) == len(set(string))


    # 2. Second approach: Not using additional data structures
    # Iterate through each char, checking if it is in the remaining of the string by slicing

    for i, char in enumerate(string):
        if char in string[i+1:]:
            return False
    
    return True


if __name__ == "__main__":
    assert is_unique("howdy") is True
    assert is_unique("hello") is False
    assert is_unique("") is True
    assert is_unique("hi you") is True
    assert is_unique("Dod") is True
    print("All tests passed.")