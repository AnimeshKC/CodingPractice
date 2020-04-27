def hasUniqueCharacters(input_str: str) -> bool:
    '''Input: a string
    returns true if a string has unique characters and false otherwise
    O(n) time complexity and O(c) space complexity, where n is the number of characters in the string,
    and c is the number of unique characters'''

    charSet = set()
    is_unique = False

    #If only ASCII characters:
    #if len(input_str > 128): #Assuming ASCII characters
        #return is_unique

    for char in input_str:
        if char in charSet:
            return is_unique
        else:
            charSet.add(char)
    is_unique = True
    return is_unique

def main():
    assert(hasUniqueCharacters("abc") == True)
    assert(hasUniqueCharacters("abad") == False)
    print("All tests have passed")

if __name__ == "__main__":
    main()