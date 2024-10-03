# raise - lançando exceções (ERROS)
def NaoAceitoZero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero! ')
    return True

def deveSerIntFloat(n):
    tipoN = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'{n} deve ser inteiro ou real'
            f'{tipoN} Enviado!'
    )
    return True

def divide(n, d):
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'{n} deve ser inteiro ou real'
        )
    
    if not isinstance(d, (float, int)):
        raise TypeError(
            f'{d} deve ser inteiro ou real'
        )
    
    NaoAceitoZero(d)
    return n / d

# print(divide(8, 0))
print(divide(8, '0'))