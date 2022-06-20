""" Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other """

# Permutation: "abcd" and "adbc"
# Not permutation: "abcd" and "abde"

def is_permutation(str1, str2):
    """ Return True if one is a permutation of the other. Otherwise, return False"""

    # Create two dictionaries {char:count}
    # Compare two dicts and return the result

    dict1 = {}
    dict2 = {}

    for char in str1:
        dict1[char] = dict1.get(char, 0) + 1

    for char in str2:
        dict2[char] = dict2.get(char, 0) + 1

    return dict1 == dict2


if __name__ == "__main__":
    assert is_permutation("abcd", "adbc") is True
    assert is_permutation("abcd", "abde") is False
    assert is_permutation("", "") is True
    assert is_permutation("abcd", "") is False
    assert is_permutation("abcdab", "adbc") is False
    assert is_permutation("Abcd", "adbc") is False
    print("All tests passed.")


