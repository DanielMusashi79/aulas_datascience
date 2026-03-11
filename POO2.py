class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        # Encapsular __nome/__idade
        self.__nome = nome.strip()
        self.__idade = idade
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
        print(f"Relatório de {self.__nome}:")
        print(f"- IMC atual: {valor_imc: .2f}")

        if valor_imc < 18.5:
            print("- Status: Abaixo do peso.")
        elif valor_imc < 25:
            print("- Status: Peso ideal (Saudável).")
        else:
            print("- Status: Acima do peso.")

    def apresentar(self):
        print(f"Olá, meu nome é: {self.__nome}, tenho {self.__idade} anos e tenho {self.altura}m de altura.")
    def get_nome(self):
        return self.__nome
    # Recuperar ou alterar dado encapsulado
    def set_idade(self, nova_idade):
        if nova_idade < 40:
            self.__idade = nova_idade

class Aluno(Pessoa):
    def __init__(self,nome,idade,altura,peso,matrícula):
        super().__init__(nome,idade,altura,peso)
        self.matrícula = matrícula
    def estudante(self):
        print(f"O aluno {self.get_nome()} tem a matrícula {self.matrícula}")

    def apresentar(self):
        print(f"Olá, meu nome é {super().get_nome()}, e minha matrícula é {self.matrícula}.")

aluno1 = Aluno("Kaneda", 17, "1,70", 65,"0001234567")

aluno1.estudante()
aluno1.apresentar()

#p1 = Pessoa("Goku", 33, "1,75", 80)
#p2 = Pessoa("Vegeta", 40, "1,65", 70)

#p1.apresentar()
#p2.apresentar()

#p1.apresentar_saude()
#p2.apresentar_saude()

#p1.set_idade(40)
#p1.apresentar()

#print(p1.get_nome())
#print(p2.get_nome())