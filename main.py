from terrestre import Terrestre
from aereo import Aereo
from aquatico import Aquatico

#Veículo Terrestre
ter_roda = 4
ter_porta = 4
ter_ano = 2019
ter_modelo = 'Lexus Luthers'
ter_tanque = 87
ter_peso = 1820

#vei_ano, vei_peso, vei_comb, vei_mod, ter_rodas, ter_portas
vei_ter = Terrestre(ter_ano, ter_peso, ter_tanque, ter_modelo, ter_roda, ter_porta)

print('Veículo Terrestre:\n')
vei_ter.info()
print(f'Consumo: {vei_ter.consumo()} km/l')
print(f'Autonomia: {vei_ter.autonomia()}km por tanque')


#Veículo Aéreo
aer_motores = 2
aer_asas = 2
aer_ano = 2013
aer_modelo = 'Biplano Nimbus'
aer_tanque = 240
aer_peso = 680

#vei_ano, vei_peso, vei_comb, vei_mod, ter_rodas, ter_portas
vei_aer = Aereo(aer_ano, aer_peso, aer_tanque, aer_modelo, aer_asas, aer_motores)

print('Veículo Aéreo:\n')
vei_aer.info()
print(f'Consumo: {vei_aer.consumo()} km/l')
print(f'Autonomia: {vei_aer.autonomia()}km por tanque')


#Veículo Aquático
aqua_motores = 4
aqua_conveses = 3
aqua_ano = 2013
aqua_modelo = 'Iate Nautilus'
aqua_tanque = 240
aqua_peso = 1220

#vei_ano, vei_peso, vei_comb, vei_mod, ter_rodas, ter_portas
vei_aqua = Aquatico(aqua_ano, aqua_peso, aqua_tanque, aqua_modelo, aqua_conveses, aqua_motores)

print('Veículo Aéreo:\n')
vei_aqua.info()
print(f'Consumo: {vei_aqua.consumo()} km/l')
print(f'Autonomia: {vei_aqua.autonomia()}km por tanque')