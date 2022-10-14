class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class Linkedlist:
    def __init__(self):
        self.head=None
        self.nextnode=None
    
    def append(self,data):
        if(self.nextnode is None):
            self.head=Node(data)
            self.nextnode=self.head
        else:
            self.nextnode.next=Node(data)
            self.nextnode=self.nextnode.next
    def atstart(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
    def atend(self,data):
        newnode=Node(data)
        if(self.head is None):
            self.head= newnode
            return
        else:
            last=self.head
            while(last.next):
                last=last.next
            last.next=newnode 
    def delete(self,position):
        current=self.head
        if(position==0 or position==1):
            self.head=current.next
            current=None
        elif(position==self.findlength()-1):
            while(current.next):
                current=current.next
            current.next=None
        elif(position>self.findlength()):
            print("Invalid selection")
        else:
            pt,pt1=self.deleteGetPointer(position)
            pt.next=pt1
    def deleteGetPointer(self,pos):
        point=self.head
        cnt=0
        while(cnt!=pos-2):
            cnt+=1
            point=point.next
        return point,point.next.next
            
    def atmiddle(self,value,data):
        length=self.findlength()
        if(value>length):
            print("Invalid Place")
        elif(value==length-1):
            self.atend(data)
        elif(value==1 or value==0):
            self.atstart(data)
        else:
            first,last=self.getpointer(value)
            newnode=Node(data)
            first.next=newnode
            newnode.next=last
    def getpointer(self,value):
        cnt=0
        point=self.head
        while(cnt!=value-2):
            cnt+=1
            point=point.next
        return point,point.next
    def findlength(self):
        point=self.head
        cnt=0
        while(point):
            cnt+=1
            point=point.next
        return cnt
    def display(self):
        name=self.head
        while(name is not None):
            print(name.data)
            name=name.next
obj=Linkedlist()
obj.append(10)
obj.append(20)
obj.append(30)
obj.append(40)
obj.atstart(20)
obj.atend(15)
obj.atmiddle(2,90)
obj.delete(8)
obj.display()

        
    
