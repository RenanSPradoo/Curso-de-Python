lista = []
for i in range(3):
    for j in range(3):
        lista.append((i, j))

lista = [
    (i, j)
    for i in range(3)
    for j in range(3)
]

lista = [
    [(i, letra) for letra in 'Fileira']
    for i in range(3)
]
print(lista)


#! CONTEUDO DO VIDEO DO YT ABAIXO:
numeros = [1, 2, 3, 4, 5]
novos_numeros = [numeros for numeros in numeros] #Numeros para numeros em numeros
# Seria a mesa coisa que a lista de cima essa baixo
# novos_numeros = []
# for numeros in numeros:
#     novos_numeros.append(numeros)
# numeros[0] = 20
# print(novos_numeros)