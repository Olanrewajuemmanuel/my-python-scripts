#single linked list

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    #insert new node
    def AtBeginning(self, newdata):
        NewNode = Node(newdata)
    #update the linked list
        NewNode.nextval = self.headval
        self.headval = NewNode

    #insert at end
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval = NewNode
    #insert at middle
    def Inbetween(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode
    #Remove a node
    # def RemoveNode(self, RemoveKey):
    #     Headval = self.headval
    #     if Headval is not None:
    #         if Headval.newdata == RemoveKey:
    #             self.headval = Headval.nextval
    #             Headval = None
    #             return

    #     while(Headval is not None):
    #         if Headval.newdata == RemoveKey:
    #             break
    #         prev = Headval
    #         Headval = Headval.nextval

    #     if (Headval == None):
    #         return

    #     prev.nextval = Headval.nextval
    #     Headval = None




list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

#link first node to second

list.headval.nextval = e2
e2.nextval = e3
list.AtBeginning("Sun")
list.AtEnd("Thu")
list.Inbetween(list.headval.nextval, "Fri")

list.listprint()

#stack
class Stack:
    def __init__(self):
        self.stack = []
    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
    def remove(self):
        if len(self.stack) <= 0:
            return("No element in stack")
        else:
            return self.stack.pop()

    def peek(self):
        return self.stack[-1]

NewStack = Stack()
NewStack.add("Mon")
NewStack.add("Tue")
print(NewStack.peek())
NewStack.add("Wed")
NewStack.add("Thu")
print(NewStack.peek())
print(NewStack.remove())
print(NewStack.peek())

#Queue
class Queue:
    def __init__(self):
        self.q = []
    
    def addtoq(self, dataval):
        if dataval not in self.q:
            self.q.insert(0, dataval)
            return True
        return False

    def size(self):
        return len(self.q)

    def contents(self):
        return self.q

    def removefromq(self):
        if len(self.q) > 0:
            return self.q.pop()
        return ("No element in queue")

NewQueue = Queue()
NewQueue.addtoq("Mon")
NewQueue.addtoq("Tue")
NewQueue.addtoq("Wed")
print(NewQueue.size())
print(NewQueue.contents())

#Binary treee
class BinaryNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, data):
        #if there is a root node already
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryNode(data)
                else:
                    self.right.insert(data)
        else:   #if there is no root node
            self.data = data

    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval) + " Not found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval) + " Not found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + " is found")

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

root = BinaryNode(10)
root.insert(6)
root.insert(12)
root.insert(18)
root.insert(3)
root.insert(11)
root.insert(9)
print(root.findval(3))
print(root.findval(12))

    
        


