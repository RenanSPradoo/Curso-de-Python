"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
import random  # Importa o módulo random, que permite a geração de números aleatórios

for _ in range(10):  # Loop que se repete 100 vezes
    nove_digitos = ''  # Inicializa uma string vazia para armazenar nove dígitos aleatórios
    for i in range(9):  # Loop para gerar nove dígitos
        nove_digitos += str(random.randint(0, 9))  # Gera um dígito aleatório (0-9) e concatena à string

    contador_regressivo_1 = 10  # Inicializa o contador regressivo com 10

    resultado = 0  # Inicializa a variável resultado com 0
    for digito in nove_digitos:  # Loop através de cada dígito na string nove_digitos
        resultado += int(digito) * contador_regressivo_1  # Multiplica o dígito pelo contador e soma ao resultado
        contador_regressivo_1 -= 1  # Decrementa o contador regressivo

    digito_1 = ((resultado * 10) % 11)  # Calcula o primeiro dígito verificador
    digito_1 = digito_1 if digito_1 <= 9 else 0  # Se o dígito for maior que 9, ajusta para 0

    dez_digitos = nove_digitos + str(digito_1)  # Concatena o primeiro dígito verificador aos nove dígitos
    contador_regressivo_2 = 11  # Inicializa o contador regressivo com 11

    resultado_digito_2 = 0  # Inicializa a variável resultado_digito_2 com 0
    for digito in dez_digitos:  # Loop através de cada dígito na string dez_digitos
        resultado_digito_2 += int(digito) * contador_regressivo_2  # Multiplica o dígito pelo contador e soma ao resultado
        contador_regressivo_2 -= 1  # Decrementa o contador regressivo

    digito_2 = (resultado_digito_2 * 10) % 11  # Calcula o segundo dígito verificador
    digito_2 = digito_2 if digito_2 <= 9 else 0  # Se o dígito for maior que 9, ajusta para 0

    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'  # Formata o CPF completo com os dígitos gerados

    print(cpf_gerado_pelo_calculo)  # Imprime o CPF gerado
