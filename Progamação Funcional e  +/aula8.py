"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bomdia = criar_saudacao('Bom dia')
falar_boanoite = criar_saudacao('Bom noite')

for nome in ['Renan', 'Mafer', 'Rose']:
    print('-' * 50)
    print(falar_bomdia(nome))
    print(falar_boanoite(nome))