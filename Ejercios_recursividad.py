# 1) Defina una funcion recursiva que reciba una lista para determinar cuantos numeros hay en ella
l = [1,69,37,45,52,7,8]

def f(lista):
    if lista == []:
        return 0 
    else:
        lista.pop()
        return f(lista) + 1
        
print("Cantidad de elementos:", f(l))



# 2) Defina una funcion recursiva que reciba una lista para determinar cuantos numeros pares hay en ella
l = [1,2,3,4,5,6,8,10,12,11]

def f(lista):
    if lista == []:
        return 0
    elif lista[0] % 2 == 0:
        lista.pop(0)
        return f(lista) + 1
    else:
        lista.pop(0)
        return f(lista)
        
print("Cantidad de pares:", f(l))



""" 3) Defina una función recursiva que reciba un string de números separados por coma, por ejemplo "1,2,3, 4,5" 
       y devuelva la productoria de estos números. Tenga en cuenta el caso en que hay y no hay espacios entre los números y las comas."""

numeros = "1,2,3, 4,5"

def f(string):
    if string == "":
        return 0
    else: 
