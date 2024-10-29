from veiculo import Veiculo

class Terrestre(Veiculo):
    
    _qtRoda = 0
    _qtPorta = 0

    def __init__(self, vei_ano, vei_peso, vei_comb, vei_mod, ter_rodas, ter_portas):
        super().__init__(vei_ano, vei_peso, vei_comb, vei_mod)
        self._qtRoda = ter_rodas
        self._qtPorta = ter_portas

    def info(self):
        super().info()
        print(f'Quantidade de Rodas: {self._qtRoda}\nQuantidade de Portas: {self._qtPorta}')
    
    def consumo(self):
        return float(1/((self._peso*0.00005) + (self._qtRoda*0.005)))
    
    def autonomia(self):
        con = self.consumo()
        return con * self.tanque