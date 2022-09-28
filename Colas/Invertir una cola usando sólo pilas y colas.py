def invertir(self):
        l = [None]*self.N
        n = len(l)
        for i in range(self.N):
            l[i] = self.dequeue()

        for i in range(self.N-1,-1,-1):
            self.enqueue(l[i])
