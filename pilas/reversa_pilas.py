def reversa(self):
        p = Stack()
        n = len(self.stack)
        for i in range(n):
            p.push(self.pop())
        for k in p.stack:
            self.push(k)
