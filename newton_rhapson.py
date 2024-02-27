def newton_raphson(func, x0, err=1e-10, max_iter=1000):
    iteracion = 0

    # Itera hasta alcanzar el número máximo de iteraciones
    while iteracion < max_iter:
        # Calcula el valor de la función y su derivada en el punto actual x0
        fx = func(x0)
        f_prima = derivada(x0, func)

        # Verifica si la derivada es demasiado pequeña (posible división por cero)
        if abs(f_prima) < 1e-10:
            return None, False

        # Calcula el siguiente punto utilizando el método de Newton-Raphson
        x1 = x0 - fx / f_prima

        # Verifica si la aproximación es suficientemente precisa
        if abs(x1 - x0) < err:
            return x1, True

        # Actualiza x0 con el nuevo valor calculado
        x0 = x1
        iteracion += 1

    # Devuelve None si no se alcanzó la convergencia en el número máximo de iteraciones
    return None, False

# Ejemplo de uso
def funcion_ejemplo(x):
    return x**2 - 4

def derivada(x, func):
    h = 1e-5
    return (func(x + h) - func(x - h)) / (2 * h)

resultado, convergencia = newton_raphson(funcion_ejemplo, 3)
