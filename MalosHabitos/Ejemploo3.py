# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(largo, ancho):
    """
    Calcula el área de un rectángulo dado el largo y el ancho.
    """
    area = largo * ancho
    return area


# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dado la base y la altura.
    """
    area = 0.5 * base * altura
    return area


# Función principal
def main():
    try:
        # Entrada de datos para el área del rectángulo
        largo = float(input("Ingrese el largo del rectángulo: "))
        ancho = float(input("Ingrese el ancho del rectángulo: "))

        # Cálculo y desglosado del área del rectángulo
        area_rectangulo = calcular_area_rectangulo(largo, ancho)
        print(f"El área del rectángulo ({largo} * {ancho}) es: {area_rectangulo}")

        # Entrada de datos para el área del triángulo
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))

        # Cálculo y desglosado del área del triángulo
        area_triangulo = calcular_area_triangulo(base, altura)
        print(f"El área del triángulo (0.5 * {base} * {altura}) es: {area_triangulo}")

    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")


# Llamamos a la función principal
main()
