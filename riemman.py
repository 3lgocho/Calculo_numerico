import math

def riemann(f, a, b, n):
    # Calcula el ancho de cada subintervalo
    h = (b - a) / n
    # Inicializa la variable acumuladora para la suma de áreas
    acum = 0

    # Inicializa la variable x con el límite inferior del intervalo
    x = a

    # Itera a través de los subintervalos y aplica la regla de Riemann
    for i in range(n):
        # Calcula el área de la región rectangular y lo agrega a la acumuladora
        acum += f(x) * h

        # Actualiza la posición de x para el siguiente subintervalo
        x += h

    # Devuelve la suma acumulada de las áreas bajo la curva
    return acum

# Ejemplo de uso
def funcion_ejemplo(x):
    return x**3 - 2*x - 5

a = 0
b = 1
n = 100

resultado = riemann(funcion_ejemplo, a, b, n)

