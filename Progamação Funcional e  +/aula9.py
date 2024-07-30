"""
Exercicios
Crie funções que duplicam, triplicam e quadruplicam o numero recebido como parâmetro
"""
 # Funções definidas
def duplica(numero):
    return numero * 2
def triplica(numero):
    return numero * 3
def quadruplica(numero):
    return numero * 4
# # Testando as funções
num = 5
print(f'O dobro de {num} é {duplica(num)}')
print(f'O triplo de {num} é {triplica(num)}')
print(f'O quádruplo de {num} é {quadruplica(num)}')

# def criar_multiplicador(multiplicador):
#     def multiplicar(numero):
#         return numero * multiplicador
#     return multiplicar

# duplicar = criar_multiplicador(2)
# triplicar = criar_multiplicador(3)
# quadruplicar = criar_multiplicador(4)
# print(duplicar(2))
# print(triplicar(2))
# print(quadruplicar(2))