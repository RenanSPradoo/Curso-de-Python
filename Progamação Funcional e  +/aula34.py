try:
    print('ABRIR ARQUIVO')
    # Vai dar erro nesse try porem o finally mesmo com erro ele é Verdadeiro
    # 8 / 0
except ZeroDivisionError: #* EXCEPT SEMPRE SERÁ PARA ESPECIFICAR O PORQUE DO ERRO NESSE CASO É ZeroDivisionError
    print('DIVIVIU POR ZERO! ')
else: #? Não é muito utilizado! 
    print('NÃO DEU ERRO! ')
finally:#!Sempre sera executado mesmo que a função seja (ERRO!)
    print('FECHAR ARQUIVO')


#TODO/ Try pode ser usado com finally / try + except(pode ter quantos quiser!) / try + except + else (nesse caso o finally não iria)


#! AONDE FALA OS ERROS ( https://docs.python.org/pt-br/3/library/exceptions.html )