# 1. Crie uma lista e use a declaração da lista frutas
frutas = ["uva", "banana", "kiwi"]
print("Lista original: ", frutas)

# 2. Aplique os princípios de Pilha, Fila e Lista
# Pilha (stack): adiciona ao final (LIFO)
frutas.append("maçã")

# Fila (queue ou deque): Adiciona/Insere em uma posição específica
# Inserir laranja no início (posição 0)(FIFO)
frutas.insert(0, "laranja")

# Lista: Adicionar normalmente
frutas.append("morango")

# 3. Laço de repetição para imprimir todos os elementos
print("\n--- Todos os elementos ---")
for fruta in frutas:
    print(fruta)

# 4. Criar condição para imprimir somente maçã e laranja
print("\n--- Apenas maçã e laranja ---")
for fruta in frutas:
    if fruta == "maçã" or fruta == "laranja":
        print(fruta)