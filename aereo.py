from veiculo import Veiculo

class Aereo(Veiculo):
    
    _qtAsa = 0
    _qtMotor = 0

    def __init__(self, vei_ano, vei_peso, vei_comb, vei_mod, aer_asas, aer_motores):
        super().__init__(vei_ano, vei_peso, vei_comb, vei_mod)
        self._qtAsa = aer_asas
        self._qtMotor = aer_motores

    def info(self):
        super().info()
        print(f'Quantidade de Asas: {self._qtAsa}\nQuantidade de Motores: {self._qtMotor}')
    
    def consumo(self):
        return float(1/((self._peso*0.00003) + (self._qtMotor*0.005)))
    
    def autonomia(self):
        con = self.consumo()
        return con * self.tanque