def combinados(cola1, cola2):
        aux = []
        n = len(cola1)
        
        cola1.invertir()
        for i in range(1, n):
            aux.append(cola1.dequeue())
            
        for i in range(1, n + len(cola2) + 2):
            print(i)
            if i % 2 == 1:
                cola1.enqueue(cola2.dequeue())
                
            elif i % 2 == 0:
                try:
                    cola1.enqueue(aux.pop())
                except:
                    continue
