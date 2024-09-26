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