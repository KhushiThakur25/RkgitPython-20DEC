class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def insertion_at_first(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insertion_at_end(self,data):
        new_node = Node(data)
        cur = self.head
        if self.head is None:
            self.head = new_node
            return
        else:
            while cur.next != None:
                cur = cur.next
            cur.next = new_node
    
    def insertion_at_anywhere(self,pos,data):
        new_node = Node(data)
        cur = self.head
        prev = None
        while pos > 1 and cur != None:
            prev = cur
            cur = cur.next
            pos -= 1
        if pos == 1:
            prev.next = new_node
            new_node.next = cur

    def deletion_at_first(self):
        if self.head is None:
            print("No node is here to delete..")
            return 
        self.head = self.head.next

    def deletion_at_end(self):
        if self.head is None:
            print("No node is here to delete..")
            return 
        cur = self.head
        while cur.next.next != None:
            cur = cur.next
        cur.next = None

    def deletion_at_anywhere(self,pos):
        cur = self.head
        prev= None
        while pos > 1 and cur != None:
            prev = cur
            cur = cur.next
            pos -= 1
        if pos == 1:
            prev.next = cur.next


    
    def show(self):
        cur = self.head
        while cur != None:
            print(f"{cur.data}-->",end=" ")
            cur = cur.next
        print()

obj = LL()
for i in range(10):
    obj.insertion_at_end(i)
obj.show()

# obj.insertion_at_first(85)
# obj.show()

# obj.insertion_at_anywhere(3,65)
# obj.show()
obj.deletion_at_first()
obj.show()
obj.deletion_at_end()
obj.show()
obj.deletion_at_anywhere(3)
obj.show()
