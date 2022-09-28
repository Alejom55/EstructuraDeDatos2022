#Listas raras
def invertir(self):
        l = [None]*self.N
        n = len(l)
        for i in range(self.N):
            l[i] = self.dequeue()

        for i in range(self.N-1,-1,-1):
            self.enqueue(l[i])
        
#listas parcha3
def invertir(self):
        l = []
        for i in self.queue:
            l.append(i)
        n = len(l)
        for i in range(n-1,-1,-1):
            self.enqueue(l[i])
        for i in range(n):
            l[i] = self.dequeue()
