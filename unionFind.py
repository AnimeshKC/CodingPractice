class QuickFind:
    def __init__(self, arr):
        self.elementDict = {}
        #map each element with the elements in its connectivity list
        #This is initialized as only itself
        for element in arr:
            self.elementDict[element] = [element]
    def connected(self, elementA, elementB):
        assert elementA in self.elementDict
        assert elementB in self.elementDict
        aConnectionsList = self.elementDict[elementA]
        if elementB in aConnectionsList:
            return True 
        else:
            return False
    def union(self, elementA, elementB):
        assert elementA in self.elementDict
        assert elementB in self.elementDict
        aConnectionsList = self.elementDict[elementA]
        bConnectionsList = self.elementDict[elementB]
        if len(bConnectionsList) < len(aConnectionsList): #make elementA the element with the smaller connection list for efficiency
            elementA, elementB = elementB, elementA
            aConnectionsList, bConnectionsList = bConnectionsList, aConnectionsList

        if self.connected(elementA, elementB):
            return #no need to do anything if the elements are already connected
        for aElement in aConnectionsList: 
            if aElement not in bConnectionsList: #put all elements unique to aConnectionsList into bConnectionsList
                bConnectionsList.append(aElement)
        for bElement in bConnectionsList: #update all elements of bConnectionsList to have this new bConnectionsList
            self.elementDict[bElement] = bConnectionsList
        
