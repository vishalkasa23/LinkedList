class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.nextNode=None
    def append(self,data):
        if(self.nextNode is None):
            self.head=Node(data)
            self.nextNode=self.head
        else:
            self.nextNode.next=Node(data)
            self.nextNode=self.nextNode.next
    def atstart(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
    def atlast(self,data):
        newnode=Node(data)
        if(self.nextNode is None):
            self.head = newnode
            return
        else:
            last = self.head
            while(last.next):
                last=last.next
            last.next=newnode
    def delete(self,key):
        currenthead=self.head
        if(currenthead.data==key):
            self.head=currenthead.next
            currenthead=None
        while(currenthead is not None):
            if(currenthead.data==key):
                break
            previous=currenthead
            currenthead=currenthead.next
        if(currenthead.next==None):
            return
        else:
            previous.next=currenthead.next
            currenthead=None
    def addAtMiddle(self,key,count):
        varify=self.LengthoflL()
        if(varify<count):
            print("Wrong place")
        else:
            count=count-2
            valueNode,valueNodeNext=self.getNode(count)
            newnode=Node(key)
            valueNode.next=newnode
            newnode.next=valueNodeNext
    def getNode(self,count):
        curr=self.head
        while(count!=0):
            curr=curr.next
            count-=1
        countval=self.LengthoflL()
        if(count==countval-1):
            return curr,None
        else:
            return curr,curr.next
    def LengthoflL(self):
        curr=self.head
        count=0
        while(curr is not None):
            count+=1
            curr=curr.next   
        return count
    def display(self):
        curr=self.head
        while(curr is not None):
            print("Elements",curr.data)
            curr=curr.next
            
mylist=LinkedList()
mylist.append(12)
mylist.append(24)
mylist.atstart(10)
mylist.atlast(30)
# mylist.delete(24)
middle,place=input("enter the number and place").split()
if(place=='1'):
    mylist.atstart(middle)
else:
    mylist.addAtMiddle(int(middle),int(place))
mylist.display()
