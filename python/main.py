class Node(object):

    def __init__(self,data,next=None):   #it is an constructer
        self.data=data
        self.next=next

class linkedList(object):

    def __init__(self):
        self.head=None

    def printlist(self):
        temp=self.head
        while(temp):
            print(f'{temp.data}-> ',end="")
            # print(temp.next) #address where data is stored
            temp=temp.next
        print('NULL')
    

    def insertAtStart(self,data):
        if self.head==None:
            newNode=Node(data)
            self.head=newNode
        else:
            newNode=Node(data)
            newNode.next=self.head
            self.head=newNode


    def insertAtEnd(self,data):
        newNode=Node(data)
        temp=self.head
        while(temp.next != None):
            temp=temp.next
        temp.next=newNode

    def insertBetween(self,previousNode,data):



if __name__=="__main__":
    List=linkedList()
    List.head=Node(1)
    List.insertAtEnd(17)
    List.insertAtEnd(19)
    List.insertAtStart(16) 
    List.printlist()