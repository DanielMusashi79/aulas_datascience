class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome.strip()
        self.idade = idade
        # Limpeza de dados: troca a vírgula pelo ponto e converte para decimal (float)
        self.altura = float(str(altura).replace(',','.'))
        self.peso = float(peso)
    
    def calcular_imc(self):
        # Cálculo: peso dividido pela altura ao quadrado
        imc = self.peso / (self.altura ** 2)
        return imc
    
    def apresentar_saude(self):
        valor_imc = self.calcular_imc()

        # Usando f-string com :.2f para mostrar apenas 2 casas decimais
        print(f"Relatório de {self.nome}:")
        print(f"- IMC atual: {valor_imc: .2f}")

        if valor_imc < 18.5:
            print("- Status: Abaixo do peso.")
        elif valor_imc < 25:
            print("- Status: Peso ideal (Saudável).")
        else:
            print("- Status: Acima do peso.")

    def apresentar(self):
        print(f"Olá, meu nome é: {self.nome}, tenho {self.idade} anos e tenho {self.altura}m de altura.")

p1 = Pessoa("Goku", 33, "1,75", 80)
p2 = Pessoa("Vegeta", 40, "1,65", 70)

p1.apresentar()
p2.apresentar()

p1.apresentar_saude()
p2.apresentar_saude()

print(p1.nome)