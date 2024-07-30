"""
args - argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

#Lembrete de desempacotamento
x , y, *_ = 1, 2, 3, 4
print(x, y, *_)
print('-' * 20)


# def soma(x + y):
#     return x + y

def soma(*args):
    total = 0
    for numero in args:
        print('Total = ',total, ' + ', numero)
        total += numero
        print('-' * 20)
    return f'{total} = resultado'

# soma(1, 2, 3, 4, 5, 6)

soma_1_2_3 = soma(1, 2, 3)
# print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
# print(soma_4_5_6)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros)
print(outra_soma)

# print(sum(numeros))
# print(*numeros)