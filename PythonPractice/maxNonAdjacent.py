
def maxNonAdjacent(arr):
    exclusiveMax = 0 #represents the maximum sum before the current number
    inclusiveMax = 0 #represents the maximum sum including the current number

    for num in arr:
        previousMax = max(exclusiveMax, inclusiveMax) 
        #update the inclusive and exclusive max
        inclusiveMax = max(previousMax, exclusiveMax + num) 
        exclusiveMax = previousMax #update exclusive max to be the previous maximum
    return inclusiveMax

if __name__ == "__main__":
    assert(maxNonAdjacent([30, 20, 10, 5]) == 40)
    assert(maxNonAdjacent([4, 1, 1, 4, 2, 1]) == 9)
    print("Tests have passed")

