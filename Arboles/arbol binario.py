class BinaryTree:
    def __init__(self, root = None):
        self.root = root

    def existe(self, e, root):
        current_root = root
        if self.root == None:
            return False
        elif (e == current_root):
            return True
        else:
            if (current_root.left == None):
                return False
            elif(current_root.right == None):
                return False
            else:
                return self.existe(e, current_root.left) or self.existe(e, current_root.right)

    def agregar(self, value, nodo = None, izq = False, der = False):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
        else:
            pass 
            

class Node:
    def __init__(self, value ,left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


arbol = BinaryTree()
nodo1 = Node(10)
nodo2 = Node(5)
nodo3 = Node(3)
nodo4 = Node(4)
nodo5 = Node(50)

#Raiz nodo1
arbol.root = nodo1

nodo1.left = nodo2
nodo1.right = nodo3
nodo2.left = nodo4
#nodo2.right = nodo5

print(arbol.existe(nodo5,nodo1))

