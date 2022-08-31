class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self,size):
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
      new_node.next = old_head  
      

  def traverse(self, head):
    if(head is not None):
        print(head.value)
        self.traverse(head.next)


  def insert_at(self, index, value):
    if (index == 0):
        self.add_at_head(value)
    else:
        if (self.size <= index):
            return "Indice fuera de rango"
        else:
            pass

  def add_at_tail(self, value):
    if (self.head is None):
        self.add_at_head(value)
    else:
        new_node = Node(value)
        old_tail = self.tail
        self.tail = new_node
        old_tail.next = new_node
