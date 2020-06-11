class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class LinkedList():

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def prepend(self, data):
        self.head = ListNode(data, self.head)
        self.length += 1
        if self.length == 1:
            self.tail = self.head

    def append(self, data):
        newNode = ListNode(data)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    def insert(self, insertIndex, data):
        if insertIndex == self.length:
            self.append(data)
            return
        if insertIndex > self.length:
            raise Exception("invalid index")
        if insertIndex == 0:
            self.prepend(data)
            return
        newNode = ListNode(data)
        currentIndex = 0
        temp = self.head
        while currentIndex < self.length:
            if currentIndex + 1 == insertIndex:
                next = temp.next
                temp.next = newNode
                newNode.next = next
                self.length += 1
            temp = temp.next
            currentIndex += 1

    def remove(self, removeIndex):
        if self.length == 0:
            raise Exception("Cannot remove from empty linked list")
        if removeIndex >= self.length:
            raise Exception("Index exceeds bounds")
        if removeIndex == 0:
            self.head = self.head.next
            self.length -= 1
            if self.length == 0:
                self.tail = None

            return
        currentIndex = 0
        temp = self.head
        while currentIndex < self.length:
            if currentIndex + 1 == removeIndex:
                if removeIndex == self.length - 1:
                    self.tail = temp
                    temp.next = None
                else:
                    temp.next = temp.next.next
                self.length -= 1
            temp = temp.next
            currentIndex += 1

    def printl(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next
        print()
        print('Length = '+str(self.length))

    def reverse(self):
        prev = None
        self.tail = self.head
        while self.head != None:
            temp = self.head
            self.head = self.head.next
            temp.next = prev
            prev = temp
        self.head = temp


test1 = LinkedList()
test1.append(1)
test1.prepend(5)
test1.insert(1, 7)
test1.remove(1)
test1.printl()


l = LinkedList()
l.append(10)
l.append(5)
l.append(6)
l.prepend(1)
l.insert(2, 1)
#l.insert(34, 23)
# l.remove(4)
l.reverse()
l.printl()
