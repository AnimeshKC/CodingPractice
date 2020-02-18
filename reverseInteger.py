def reverseInt(val):
    '''Takes an integer and reverses it'''
    reverse = 0
    signVal = 1
    if (val < 0):
        signVal = -1
        val = -1 * val
    while val > 0:
        reverse *= 10
        remainder = val % 10
        reverse += remainder
        val = val // 10
    return reverse * signVal

def tests():
    print("Testing 123: " + str(reverseInt(123)))
    print("Testing -500: " + str(reverseInt(-500)))
tests()

