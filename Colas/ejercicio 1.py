class Queue:
    def __init__(self):
        self.queue = [None]*5
        self.tamanno = len(self.queue)
        self.f = None
        
    def num_elementos(self):
        cont = 0
        for n in self.queue:
            if n != None:
                cont += 1
        return cont
    
    def front(self):
        if self.frente == None:
            return 0
        else:
            return self.frente
    
    def enqueue(self, elemento):
        #agregar un elemento e a la cola
        
        if(self.num_elementos() == self.tamanno):
            return print("No hay posiciones disponibles")
        
        if self.num_elementos() == 0:
            self.f = 0 
            
        pos_disp = (self.f + self.num_elementos()) % self.tamanno
        self.queue[pos_disp] = elemento
      
    def dequeue(self):
        #remueve y retorna el primer elemento
        if(self.is_empty()):
            raise Exception("Cola vacía...")
        else:
            self.frente = (self.frente + 1) % self.tamanno
            self.queue[self.f]
  
    def first(self):
        #retornar el primer elemento de la cola
        if(self.is_empty()):
            raise Exception("Cola vacía...")
        return self.queue[0]  
  
    def is_empty(self):
        return self.num_elementos == 0 
  
    def __len__(self): #dunder method
        #retorna tamaño
        return len(self.queue)
  
cola = Queue()
print("Numero elementos: ", cola.num_elementos())
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)
cola.enqueue(4)
cola.enqueue(5)

for n in cola.queue:
    print(n)
