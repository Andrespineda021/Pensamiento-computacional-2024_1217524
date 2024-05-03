# def tipo_triangulo(a, b, c):
#     if a == b == c:
#         return "Equilátero"
#     elif a == b or a == c or b == c:
#         return "Isósceles"
#     else:
#         return "Escaleno"

# lado1 = float(input("Introduce la longitud del primer lado del triángulo: "))
# lado2 = float(input("Introduce la longitud del segundo lado del triángulo: "))
# lado3 = float(input("Introduce la longitud del tercer lado del triángulo: "))


# tipo = tipo_triangulo(lado1, lado2, lado3)

# print("El triángulo es:", tipo)




# #Ejercicio2
# import math

# def obtener_perimetro(radio):
#     return 2 * math.pi * radio

# def obtener_area(radio):
#     return math.pi * radio ** 2

# def obtener_volumen(radio):
#     return (4/3) * math.pi * radio ** 3


# radio = float(input("Ingrese el radio del círculo: "))


# perimetro = obtener_perimetro(radio)
# area = obtener_area(radio)
# volumen = obtener_volumen(radio)

# print("Perímetro de la circunferencia:", perimetro)
# print("Área de la circunferencia:", area)
# print("Volumen de la esfera:", volumen)

#ejercicio 3
def imprimir_nombre_mes(numero):
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }
    if numero in meses:
        print(meses[numero])
    else:
        print("Error: El número ingresado no es válido.")


def main():
    numero = int(input("Ingrese un número del 1 al 12: "))
    imprimir_nombre_mes(numero)


if __name__ == "__main__":
    main()
