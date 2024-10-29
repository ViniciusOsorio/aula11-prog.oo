from veiculo import Veiculo

class Aquatico(Veiculo):
    
    _qtConves = 0
    _qtMotor = 0

    def __init__(self, vei_ano, vei_peso, vei_comb, vei_mod, aqua_conves, aqua_motores):
        super().__init__(vei_ano, vei_peso, vei_comb, vei_mod)
        self._qtConves = aqua_conves
        self._qtMotor = aqua_motores

    def info(self):
        super().info()
        print(f'Quantidade de Convéses: {self._qtConves}\nQuantidade de Motores: {self._qtMotor}')
    
    def consumo(self):
        return float(1/((self._peso*0.00002) + (self._qtMotor*0.005)))
    
    def autonomia(self):
        con = self.consumo()
        return con * self.tanque