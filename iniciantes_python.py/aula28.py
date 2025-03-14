"""
 CONSTANTE = "Variáveis" que não vão mudar
 Muitas condições no mesmo if (ruim)
     <- Contagem de complexidade (ruim)
 """
"""
velocidade = 91  # velocidade atual do carro
local_carro = 200  # local em que o carro está na estrada
 
RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

if velocidade > RADAR_1:
    print("velocidade do radar 1")

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)and \
    velocidade > RADAR_1:
    print("Carro multado no radar 1")
else:
    print("Não é radar 1")

# Exemplo de como fazer o mesmo código de cima de forma mais limpa
# e mais fácil de entender
RADAR_2 = 80  # velocidade máxima do radar 2
LOCAL_2 = 200  # local onde o radar 2 está
RADAR_RANGE = 1  # A distância onde o radar pega

if (velocidade > RADAR_1 and
    local_carro >= (LOCAL_1 - RADAR_RANGE) and
    local_carro <= (LOCAL_1 + RADAR_RANGE)):
    print("Carro multado no radar 1")
elif (velocidade > RADAR_2 and
    local_carro >= (LOCAL_2 - RADAR_RANGE) and
    local_carro <= (LOCAL_2 + RADAR_RANGE)):
    print("Carro multado no radar 2")
else:
    print("Não é radar 1 ou 2")
"""

velocidade = 62  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

car_passkm_1 = velocidade > RADAR_1 
carro_pass_radar1 = local_carro >= LOCAL_1 - RADAR_RANGE
posição = local_carro <= LOCAL_1 + RADAR_RANGE
carro_multado = carro_pass_radar1 and car_passkm_1

if car_passkm_1:
    print("Passou o radar 1")
if carro_pass_radar1:
    print("Passou na posição do radar 1")
if carro_multado and posição:
    print("Carro multado no radar 1")