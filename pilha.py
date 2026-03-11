# 1. Pilha LIFO
pilha = []
pilha.append(1)
pilha.append(2)
pilha.append(3)
pilha.append(4)
pilha.append(5)
print(pilha)
pilha.pop()
print(pilha)

# 2. Fila FIFO (Não nativo no Python)
from collections import deque
fila = deque()
fila.append(1)
fila.append(2)
fila.append(3)
fila.append(4)
fila.append(5)
fila.append(6)
print(fila)

fila.popleft()
print(fila)
