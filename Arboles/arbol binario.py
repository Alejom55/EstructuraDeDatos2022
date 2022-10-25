class BinaryTree:
    def __init__(self, root = None):
        self.root = root

    def existe(self, e, root):
        current_root = root
        if (e == current_root):
            return True
        else:
            if (current_root.left == None):
                return False
            elif(current_root.right == None):
                return False
            else:
                return self.existe(e, current_root.left) or self.existe(e, current_root.right)

    def insertarEspecifico(self, value, padre = None):
        new_node = Node(value)
        if self.existe(padre, self.root) is False:
            return f"No existe el nodo {padre.value}"
        else:
            pass

class BST():
    def __init__(self, root = None):
        self.root = Node(root)

    def agregar(self,val, raiz = None):
        current_root = raiz
        if raiz is None:
            raiz = Node(val)
            self.root = raiz
        else:
            if val < current_root.value:
                if current_root.left is None:
                    current_root.left = Node(val)
                else:
                    return self.agregar(val, current_root.left)
            else:
                if current_root.right is None:
                    current_root.right = Node(val)
                else:
                    return self.agregar(val,current_root.right)
    
    def buscar(self, val, raiz):
        current_root = raiz
        if val == current_root.value:
            return True
        else:
            if (current_root.left == None):
                return False
            elif(current_root.right == None):
                return False

            if val < current_root.value:
                return self.buscar(val, current_root.left)
            else:
                return self.buscar(val, current_root.right)

    

    def pretty_print_tree(self, node, prefix="", is_left=True):
        if not node:
          print("Empty Tree")
          return
        if node.right:
          self.pretty_print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
        if node.left:
          self.pretty_print_tree(node.left, prefix + ("    " if is_left else "│   "), True)

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
nodo5 = Node(5)


arbolBST = BST(5)

arbolBST.agregar(2, arbolBST.root)
arbolBST.agregar(20, arbolBST.root)
arbolBST.agregar(40, arbolBST.root)
arbolBST.agregar(3, arbolBST.root)
arbolBST.agregar(1, arbolBST.root)
arbolBST.agregar(22, arbolBST.root)
arbolBST.agregar(23, arbolBST.root)
arbolBST.agregar(41, arbolBST.root)
arbolBST.agregar(20, arbolBST.root)




arbolBST.pretty_print_tree(arbolBST.root)

print(arbolBST.buscar(23, arbolBST.root))

#
##Raiz nodo1
#arbol.root = nodo1
#
#nodo1.left = nodo2
#nodo1.right = nodo3
#nodo2.left = nodo4
##nodo2.right = nodo5
#
#print(arbol.existe(nodo5,nodo1))
#print(arbol.insertarEspecifico(nodo3,nodo5))
#
