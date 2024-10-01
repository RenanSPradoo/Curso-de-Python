# gerador expression, iterables e iterators 
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__
print(next(iterator))
print(next(iterator))
print(next(iterator))
# Esse prximo como não tem dentro da lista vai dar erro o ideal seria fazer um FOR para parar ele 
# print(next(iterator))
