""" URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: 'Mr John Smith ', 13
Output: 'Mr%20John%20Smith' 
"""

def urlify(string, length):
    """ Return the string with all spaces replaced by '%20' """

    # Create a new string.
    # Iterate through the input string, check if it is whitespace
        # if yes -> replace with %20 and add to new string
        # if not -> add char to new string

    if length == 0:
        return ""

    url = ""

    for i in range(length + 1):
        if string[i] == " " and i != length:
            url += "%20"
        elif string[i] != " ":
            url += string[i]

    return url

if __name__ == "__main__":
    # Unit test
    assert urlify('Mr John Smith ', 13) == "Mr%20John%20Smith"
    assert urlify('Mr John Smith', 12) == "Mr%20John%20Smith"
    assert urlify('', 0) == ""
    assert urlify(' Mr John Smith ', 14) == "%20Mr%20John%20Smith"
    print("All tests passed.")
