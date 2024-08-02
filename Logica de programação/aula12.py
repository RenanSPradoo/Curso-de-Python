nome = 'Renan Prado'
altura = 1.67
peso = 100
imc = peso / (altura * altura) # peso / altura ** 2 

# f-Strings
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso},quilos e o seu IMC é:'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

