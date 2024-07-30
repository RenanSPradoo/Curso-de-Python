"""
Retorno de valores das funções (return)
"""

def soma(x, y):
    if x > 10:
        return 10, 20 #pode ser uma Tupla também 
    return x + y

soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(11, 55))
