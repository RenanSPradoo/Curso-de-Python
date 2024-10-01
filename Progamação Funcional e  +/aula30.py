# generator - geralmente são funcoções que sabe pausar em determinado momento
# iterator -  é uma classe que precisa ter o metodo __iter__ e __next__ ("Eles trabalham com iteravel")

import sys #importa a biblioteca para ver quantos (KB,GB,TB) está usando da minha memoria

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)
lista = [n for n in range(1000)] #Iteravel
generator = (n for n in range(1000)) #generator(funcao que sabe pausar)

print(sys.getsizeof(lista)) #Vai me falar quanto de espaço está pegando da minha memoria do computador
print(sys.getsizeof(generator)) #Vai me falar quanto de espaço está pegando da minha memoria do computador

# for n in generator:
#     print(n)

#! generator seria toda vez que eu pausace o programa ele iria me enviar outro valor