"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61 # velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

acima_velocidade = velocidade > RADAR_1
carro_passou_radar1 = local_carro >= (LOCAL_1 + RADAR_RANGE) and (LOCAL_1 - 1)
carro_multado = acima_velocidade and carro_passou_radar1

if acima_velocidade:
    print('Carro passou da velocidade do radar 1')

if carro_passou_radar1:
    print('Carro passou radar 1')

if carro_multado:
    print('Carro multado no radar 1')
