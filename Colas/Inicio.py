#implementación usando listas de python
class Queue:
    def __init__(self):
        self.N = 5 #tamaño de la cola
        self.n = 0 #cant. elementos
        self.queue = [None]*self.N
        self.pos_dis = 0
        self.f = None
    
    def print_queue(self):
        print(self.queue)

    def enqueue(self, e):
        if(self.n == self.N):
            return "Grave..."
        if(self.n == 0 and self.f is None):
            self.f = 0
        self.pos_dis = (self.f+self.n)%self.N #nueva posición disp
        self.n += 1 #cantidad de elementos
        self.queue[self.pos_dis] = e

    def dequeue(self):
        if(self.n==0):
            raise Exception("Grave...")
        value = self.queue[self.f] #guardando lo que voy a eliminar
        self.queue[self.f] = None
        self.f = (self.f+1)%self.N
        self.n -= 1
        return value

    def is_empty(self):
        return len(self.queue) == 0

    def __len__(self): #dunder method
        #retorna tamaño
        return len(self.queue)

#inicio chill
class Queue:
    def __init__(self):
        self.queue = []   
    def print_queue(self):
        print(self.queue)
    def enqueue(self, e):
        #agregar un elemento e a la cola
        self.queue.append(e)  
    def dequeue(self):
        #remueve y retorna el primer elemento
        if(self.is_empty()):
            raise Exception("Cola vacía...")
        return self.queue.pop(0)  
    def first(self):
        #retornar el primer elemento de la cola
        if(self.is_empty()):
            raise Exception("Cola vacía...")
        return self.queue[0]  
    def is_empty(self):
        return len(self.queue)==0 
    def __len__(self): #dunder method
        #retorna tamaño
        return len(self.queue)
