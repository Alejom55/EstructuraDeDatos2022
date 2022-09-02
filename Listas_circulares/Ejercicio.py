class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class CircularList:
    def __init__(self, size):
        self.head = None
        self.tail = None
        self.size = size

    def add_at_head(self, value):
        self.size += 1
        new_node = Node(value)
        if(self.head is None):
            self.head = new_node
            self.tail = new_node
        else:
            old_head = self.head
            self.head = new_node
            self.tail.next = self.head
            new_node.next = old_head
       
    def sonIguales(self):
        return self.tail.next == self.head
    
    def traverse(self, head):
        if(head is None):
            print(head.value)
            #return self.traverse(head)
        

    
    def is_circular(self, head, variable):
        if (head.next is None):
            return False
        else:
            if (variable == head):
                return True

            elif(variable is None):
                return False

            else:
                return self.is_circular(head, variable.next)




CL = CircularList(0)

n1 = Node(5)
n2 = Node(6)
n3 = Node(7)
n4 = Node(8)

CL.add_at_head(1)
CL.add_at_head(2)
CL.add_at_head(3)
CL.add_at_head(4)
CL.add_at_head(5)
CL.add_at_head(5)


print(CL.sonIguales())
CL.traverse(CL.head)
print(CL.is_circular(n1, n2))
