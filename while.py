i = 0
while i <= 10:
    print(i, end='')
    i += 2

inicio = int(input("Digite o número inicial do intervalo: "))
fim = int(input("Digite o número final do intervalo: "))

print(f"\nBuscando números pares entre {inicio} e {fim}")

# 1. Utilizar 'for' para iterar no intervalo
# Usar 'fim + 1' porque o range não inclui o último número por padrão.
for numero in range(inicio, fim +1):
# O programa deve imprimir todos os números pares
# Verificamos se o resto da divisão por 2 é zero.
    if numero % 2 == 0:
        print(numero)