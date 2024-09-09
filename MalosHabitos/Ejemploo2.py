def calcular(multiplicando, multiplicador, sumando):

    producto = multiplicando * multiplicador
    resultado_final = producto + sumando

    # Imprimir resultados parciales
    print(f"El resultado de {multiplicando} * {multiplicador} es: {producto}")
    print(f"El resultado de {producto} + {sumando} es: {resultado_final}")

    return resultado_final

def principal():
    try:
        # Solicitamos al usuario que ingrese los números
        numero1 = float(input("Ingrese el primer número (multiplicando): "))
        numero2 = float(input("Ingrese el segundo número (multiplicador): "))
        numero3 = float(input("Ingrese el tercer número (sumando): "))

        # Calculamos el resultado
        resultado = calcular(numero1, numero2, numero3)

        # Mostrar el resultado final
        print(f"El resultado final es: {resultado}")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

# Llamamos a la función principal
principal()
