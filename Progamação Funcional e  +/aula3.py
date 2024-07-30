"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1 #escopo do modulo

def escopo_interno():
    # global x
    x = 10 #escopo interno

    def escopo_interno_dessa_funcao():
        # global x
        x = 11 #escopo mais interno
        y = 2 #escopo mais interno
        print(x, y) #escopo mais interno

    escopo_interno_dessa_funcao()
    print(x) #escopo interno

print(x) #escopo do modulo
escopo_interno() #escopo interno
print(x) #escopo do modulo