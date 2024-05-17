# # ejercicio 1
# # Lista de precios
# precios = [50, 75, 46, 22, 80, 65, 8]

# # Obtener el menor y el mayor precio utilizando min() y max()
# menor_precio = min(precios)
# mayor_precio = max(precios)

# # Mostrar resultados
# print("El precio más bajo es:", menor_precio)
# print("El precio más alto es:", mayor_precio)

# # ejercicio 3
# def contar_numero(lista, numero):
#     return lista.count(numero)

# def main():
#     lista_numeros = []

#     n = int(input("¿Cuántos números quieres agregar a la lista? "))
#     for i in range(n):
#         numero = int(input("Ingrese el número {}: ".format(i+1)))
#         lista_numeros.append(numero)

#     numero_buscar = int(input("Ingrese el número que desea buscar: "))

#     cantidad = contar_numero(lista_numeros, numero_buscar)
#     print("El número {} aparece {} veces en la lista.".format(numero_buscar, cantidad))

# if __name__ == "__main__":
#     main()


import random

# Inicializar el vector
vector = []

# Ingresar 100 elementos aleatorios en el vector
for _ in range(100):
    vector.append(random.randint(1, 500))  # Números aleatorios del 1 al 500

# Mostrar todos los pares primero
print("Pares:")
for num in vector:
    if num % 2 == 0:
        print(num)

# Mostrar todos los impares luego
print("Impares:")
for num in vector:
    if num % 2 != 0:
        print(num)