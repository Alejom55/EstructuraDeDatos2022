class Node:
  def __init__(self, value):
    
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self,size):
    self.head = None
    self.size = size

  def get_head(self):
    return self.head

  def add_at_head(self, value):
    self.size += 1
    new_node = Node(value)
    if(self.head is None):
      self.head = new_node
    else:
      old_head = self.head
      self.head = new_node
      new_node.next = old_head  
      

  def traverse(self, head):
    if(head is None):
      return "Vacía..."
    if(head.next is None):
      print(head.value)
    else:
      print(head.value)
      return self.traverse(head.next)

  def insert_at(self, index, value):
    if (index == 0):
        self.add_at_head(value)
    else: 
        

ll = LinkedList(0)
ll.add_at_head(1)
ll.add_at_head(2)
ll.add_at_head(3)
ll.add_at_head(4)
ll.add_at_head(5)

ll.insert_at(4, 10) #0,1 los tres primeros...
ll.traverse(ll.get_head())
print(f"tamanno lista {ll.size}")
