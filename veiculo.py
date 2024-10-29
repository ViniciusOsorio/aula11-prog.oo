class Veiculo:

    _ano = 2024
    _peso = 0
    _tanque = 0.0    #combustivel
    _modelo = ''

    def __init__(self, vei_ano, vei_peso, vei_comb, vei_mod):
        self._ano = vei_ano
        self._peso = vei_peso
        self._tanque = vei_comb
        self._modelo = vei_mod

    @property
    def ano(self):
        return self._ano
    
    @ano.setter
    def ano(self, n_ano):
        self._ano = n_ano

    @property
    def peso(self):
        return self._peso
    
    @peso.setter
    def peso(self, n_peso):
        self._peso = n_peso

    @property
    def tanque(self):
        return self._tanque
    
    @tanque.setter
    def tanque(self, n_tanque):
        self._tanque = n_tanque

    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, n_modelo):
        self._modelo = n_modelo

    def info(self):
        return print(f'Informações do Veículo:\nModelo: {self._modelo}\nAno: {self._ano}\nPeso: {self._peso}kg\nCombustível no tanque: {self._tanque}l')