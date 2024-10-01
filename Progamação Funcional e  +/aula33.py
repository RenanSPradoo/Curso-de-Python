# # try, except, else, finally
# a = 18
# b = 0 
# c = a / b
string = 'Renan'
print(isinstance(string, str))

try:
    a = 18
    b = 0
    # print('Linha 1'[1000])
    c = a / b 
    # print(b[0]) #?Vai puxar o Exception
    print('Linha 2')
except ZeroDivisionError as e:
    # print('Dividiu por zero.')
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError ') 
    print('MSG: ', error )
    print('Nome: ', error.__class__.__name__)
except Exception: #! A maior classe do Python para verificar todos os erros (NÂO TEM OUTRO ACIMA DESSA)
    print('ERRO DESCONHECIDO! ')

print('CONTINUAR! ')

