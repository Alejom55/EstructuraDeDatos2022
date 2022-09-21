#implementación usando listas de python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, e):
      #agregar un elemento e a la pila
        self.stack.append(e)

    def pop(self):
      #remueve y retorna el último elemento
        if(self.is_empty()):
            raise Exception("Pila vacía...")
        return self.stack.pop()

    def top(self):
      #retornar el último el último elemento de la pila
        if(self.is_empty()):
            raise Exception("Pila vacía...")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack)==0

    def __len__(self): #dunder method
    #retorna tamaño
        return len(self.stack)

    def f(self, cadenita):
        for i in cadenita:
            print(self.stack)
            self.push(i)
            if(i==")"):
                self.pop()
                self.pop()
            
        if(len(self.stack) == 0):
            return True
        else:
            return False

pila = Stack()
cadena = "((())))"

print(pila.f(cadena))
