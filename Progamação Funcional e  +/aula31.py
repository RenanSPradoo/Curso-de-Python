#  introdução as generator functions em python 
#* generator = (n for n in range(100000))

# def generator(n=0):
#     yield 1 #!Pausar
#     print('Continuando...')
#     yield 2 #!Pausar
#     print('Mais uma...')
#     yield 3 #!Pausar
#     print('Vou terminar! ')
#     return 'ACABOU! ' #!Vai sair no final do programa que acabou
# Toda vez que tiver um yield vai ser uma generator function

# gen = generator(n=0)
# print(next(gen))
# print(next(gen))
#? Nesse caso como tem apenas 2 função sendo chamado acima ^ vai ficar parado no yield 2 (continuando...) se chamar mais funcao vai ir até o fim Return
# print(next(gen))
# print(next(gen))


# gen = generator(n=0)
# for n in gen:
#     print(n)




def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum: #ou apenas só > que vai ser de 0 a 10
            return
        
gen = generator()
for n in gen:
    print(n)