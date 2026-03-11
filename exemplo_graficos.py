import matplotlib.pyplot as plt

# Criando um gráfico de linha
#plt.plot([1, 3, 5], [2, 6, 7])

#plt.show()

# Dados
x = ['Maçã', 'Laranja', 'Uva', 'Banana', 'Kiwi']
y = [25, 31, 77, 109, 22]

plt.bar(x, y, color ='green')

# Adicionando rótulos
plt.xlabel('Frutas')
plt.ylabel('Quantidade')
plt.title('Quantidade de Frutas')

plt.show()