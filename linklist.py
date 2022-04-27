class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
    def printd(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.next=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1

    def pop(self):
        if self.head==None:
            print('No node to eliminate')
        elif self.tail==None:
            '''print('the deleted element is'+self.value)'''
            self.head=None
        else:
            temp=self.head
            pre=self.head
            while(temp.next):
                pre=temp
                temp=temp.next
            self.tail=pre
            self.tail.next=None
        self.length-=1
        print(self.length)





class Node:
    def __init__(self,value):
        self.value=value
        self.next=None



mylink=LinkedList(4)
mylink.printd()
mylink.append(9)
mylink.printd()
mylink.pop()
mylink.printd()
