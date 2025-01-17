"""
Higher order functions
funções de primeira classe
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, args):
    return funcao(args) 

print(
   executa(saudacao, 'Bom dia', 'Renan')
)
print(
    executa(saudacao, 'Bom tarde', 'Mafer')
)