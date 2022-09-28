def reversa_mitad(self):
        p = Stack()
        n = len(self.stack)
        mitad = round(n / 2)
        
        for i in range(n - 1, mitad -1 ,-1):
            p.push(self.pop())
        self.reversa()
        p.reversa()
        for k in p.stack:
            self.push(k)
        return self.stack
def reversa(self):
        p = Stack()
        n = len(self.stack)
        for i in range(n):
            p.push(self.pop())
        for k in p.stack:
            self.push(k)
        return self.stack
