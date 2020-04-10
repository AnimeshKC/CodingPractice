def findScrambledWords(word: str, dictList: list)-> list:
    returnList = []
    if len(word) == 0 or len(dictList) == 0:
        return returnList
    wordDict = buildDictForWord(word)

    for currentWord in dictList:
        currentWordDict = buildDictForWord(currentWord)
        if currentWordDict == wordDict:
            returnList.append(currentWord)
    return returnList
def buildDictForWord(word: str) -> dict:
    wordDict = {}
    for char in word: #build a dictionary for the word
        if char in wordDict:
            wordDict[char] += 1
        else:
            wordDict[char] = 1
    return wordDict

def testPrint(testWord, testList)->None:
    print("The resulting list for word " + testWord + " and list " + str(testList) + " is: " + str(findScrambledWords(testWord, testList)))

if __name__ == '__main__':
    word1 = "sport"
    list1 = ["ghost", "sport", "ports", "contort", "torps"]
    result1 = ["sport", "ports", "torps"]
    assert findScrambledWords(word1, list1) == result1

    assert findScrambledWords("", list1) == []

    assert findScrambledWords(word1, []) == []

    print("All tests have passed")