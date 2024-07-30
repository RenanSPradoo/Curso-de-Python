# Constantes
RADAR_1 = 60  # Velocidade máxima do radar 1
LOCAL_1 = 100  # Local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

# Variáveis (essas variáveis devem ser definidas antes de serem usadas)
velocidade = 70  # Exemplo de velocidade do carro
local_carro = 100  # Exemplo de local do carro

# Condições
vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = (LOCAL_1 - RADAR_RANGE) <= local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

# Verificações e saídas
if vel_carro_pass_radar_1:
    print('Velocidade do carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou pelo radar 1')

if carro_multado_radar_1:
    print('Carro multado pelo radar 1')
