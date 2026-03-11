import numpy as np

#print(arr1[3])

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

#print(arr2[1,2])

#print(f"Shape da matriz: {arr2.shape}")
#print(f"Número de elementos: {arr2.size}")
#print(f"Tipo dos elementos: {arr2.dtype}")

# Operações matemáticas
arr1 = np.array([10, 20, 30, 40, 50])

#print(arr1 + 10)

#print(arr2 * 2)

print("Média")
print(np.mean(arr1))

print("Mediana")
print(np.median(arr1))

print("Desvio padrão")
desvio_padrao = np.std(arr1)
print(desvio_padrao)

print("Variância")
variancia = np.var(arr1)
print(variancia)


arr3 = np.array([12, 75, 99, 1979, 35, 4])
print("Média")
print(np.mean(arr3))

min = np.min(arr1)
max = np.max(arr1)
print(f"Mínimo: {min}")
print(f"Máximo: {max}")