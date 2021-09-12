import numpy as np
import pdb
pdb.set_trace()

"""
    Punto 1:
        Con comprensión de listas calcular el máximo de cada lista de una lista de listas
"""
def maximo_list(superlista):
    maximos = [np.amax(sublista) for sublista in  superlista]
    return maximos
    
def es_primo(x):
    primo = True
    for i in range(2,x):
        if(x%i == 0):
            primo = False
    return primo

print(f'La lista de máximos es {maximo_list([[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]])}')
"""
    Punto 2:
        Con filter calcular los primos de una lista de numeros
"""
numeros =  [3, 4, 8, 5, 5, 22, 13]
primos = list(filter(es_primo, numeros))
print(f' Los numeros primos son {primos}')    
    