# dir, hasattr e gerattr em python
#! dir, vai me mostrar todas as possibilidade que posso colocar dentro de uma string por exemplo: (string.upper())
#? hasattr chega se tem determinado objeto tem determinado nome la dentro:   if hasattr(string, 'upper'): 

string = 'Luiz'
metodo = 'upper'

# print(string)

# if hasattr(string, 'upper'):
#     print('Existe upper?')
#     print(string.upper())

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)