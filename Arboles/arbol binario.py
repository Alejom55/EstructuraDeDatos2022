class BinaryTree:
    def __init__(self, root = None):
        self.root = root

    #Funciona
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

    #No funciona
    def insertarEspecifico(self, value, padre = None):
        new_node = Node(value)
        if self.existe(padre, self.root) is False:
            return f"No existe el nodo {padre.value}"
        else:
            pass

    def inOrder(self,raiz):
        #izq,root,der
        if(raiz):
            self.inOrder(raiz.left)
            print(raiz.value)
            self.inOrder(raiz.right)


class BST():
    def __init__(self, root = None):
        self.root = Node(root)

    #Funciona
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
    
    #Funciona
    def meterLista(self, lista, root):
        num = len(lista)
        for n in range(num):
            self.agregar(lista[n], root)



    #Funciona
    def buscar(self, val, raiz):
        current_root = raiz
        if val == current_root.value:
            return True
        else:
            if (current_root.left is None and current_root.right is None):
                return False
            if val < current_root.value:
                return self.buscar(val, current_root.left)
            else:
                return self.buscar(val, current_root.right)

    #Funciona
    def invertir(self,raiz):
        current_root = raiz

        if current_root is not None:
            current_right = current_root.right
            current_left = current_root.left
            raiz.left = current_right
            raiz.right = current_left
            return self.invertir(current_left), self.invertir(current_right)

    #Funciona
    def altura(self, raiz, cont = 0):
        current_root = raiz
        current_cont = cont

        if current_root is not None:
            current_cont += 1
            if self.altura(current_root.left, current_cont) >= self.altura(current_root.right, current_cont):
                current_cont = self.altura(current_root.left, current_cont)
            else:
                current_cont = self.altura(current_root.right, current_cont)
        return current_cont


    #Funciona
    def valance(self, raiz):
        current_root = raiz
        
        izq = self.altura(current_root.left)
        der = self.altura(current_root.right)
        valanced = izq - der
        if valanced == -1 or valanced == 0 or valanced == 1:
            return True
        else:
            return False


    #Funciona
    def listaValance(self, raiz, lstNoValanced = list(), lstValanced = list()):
        current_root = raiz
        
        if current_root is not None:
            current_left = raiz.left
            current_right = raiz.right
            izq = self.altura(current_left)
            der = self.altura(current_right)
            valanced = izq - der
            if valanced < -1 or valanced > 1:
                lstNoValanced.append(current_root.value)
            else:
                lstValanced.append(current_root.value)
            self.listaValance(current_left)
            self.listaValance(current_right)
        return lstNoValanced, lstValanced
    
    def eliminar(self, val, raiz):
        current_root = raiz

        if current_root is not None:
            current_left = raiz.left
            current_right = raiz.right
            if current_left is not None and current_right is not None:
                
                if current_left.value == val:
                    print(current_root.value)
                    if current_root.left.left is None and current_root.left.right is None:
                        raiz.left = None
                if current_right.value == val:
                    if current_root.right.left is None and current_root.right.right is None:
                        raiz.right = None
            self.eliminar(val,current_left)
            self.eliminar(val,current_right)

    def inOrder(self,raiz):
        #izq,root,der
        if(raiz):
            self.inOrder(raiz.left)
            print(raiz.value)
            self.inOrder(raiz.right)

    def preOrder(self,raiz):
        #root,izq,der
        if(raiz):
            print(raiz.value)
            self.inOrder(raiz.left)
            self.inOrder(raiz.right)

    def posORder(self,raiz):
        #izq,der,root
        if(raiz):
            self.inOrder(raiz.left)
            self.inOrder(raiz.right)
            print(raiz.value)





    #Funciona
    def pretty_print_tree(self, node, prefix="", is_left = True):
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


arbolBST = BST(10)
lista = [2,20,40,3,5,4,6,1,22,23,41,20]
arbolBST.meterLista(lista, arbolBST.root)
arbolBST.inOrder(arbolBST.root)

arbolBST.eliminar(41, arbolBST.root)
arbolBST.pretty_print_tree(arbolBST.root)

