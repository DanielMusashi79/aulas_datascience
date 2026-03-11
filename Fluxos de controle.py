frutas = ["Maçã", "Laranja", "Banana"]
#print(frutas)

for fruta in frutas:
    print(fruta)

num = 1
while num <= 5:
    print(num)
    num += 1

# DESAFIO
# 1. Crie uma lista e use a declaração da lista
frutas = ["uva", "banana"]
print("Lista original:", frutas)

# 2. Aplique os princípios de Pilha, Fila e Lista
# Princípio de Pilha (Stack): Adiciona ao final (LIFO)
frutas.append("maçã") 

# Princípio de Fila (Queue): Adiciona/Insere em uma posição específica
# Aqui vamos inserir a laranja no início (posição 0)
frutas.insert(0, "laranja")

# Princípio de Lista: Adicionar normalmente
frutas.append("morango")
print("Lista após manipulações:", frutas)

# 3. Utilize o laço de repetição para imprimir todos os elementos
print("\n--- Todos os elementos ---")
for fruta in frutas:
    print(fruta)

# 4. Crie uma condição para imprimir somente a maçã e a laranja
print("\n--- Apenas Maçã e Laranja ---")
for fruta in frutas:
    if fruta == "maçã" or fruta == "laranja":
        print(fruta)