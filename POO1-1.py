from datetime import date # Importamos a ferramenta de data
class Carro:
    def __init__(self, modelo, placa, ano):
        self.modelo = modelo.strip()
        self.placa = placa.strip()
        self.ano = int(ano)

    def mostrarPlaca(self):
        print(f"O veículo {self.modelo:10} tem a placa: {self.placa}")# Calcular a idade do carro
    def calcularIdade(self):
        ano_atual = date.today().year
        idade = ano_atual - self.ano
        return idade
# Criando lista de carros
frota = [
    Carro("Fusca", "ABC-1234", 1975),
    Carro("Civic", "XYZ-5678", 2022),
    Carro("Opala", "FCK-6969", 1980),
    Carro("Chevrolet Blazer", "DBZ-2099", 1995),
]
print(f"{'MODELO':<12} | {'PLACA':<10} | {'IDADE':<10}")
print("-" * 35)

# 2. O Loop For: Processando a frota
for c in frota:
    idade = c.calcularIdade()
    status = "Antigo" if idade > 20 else "Novo"
    print(f"{c.modelo:<12} | {c.placa:<10} | {idade} anos ({status})")