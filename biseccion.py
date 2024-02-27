import math as mt

def biseccion(f, intervalo, Es, Nl):
    a, b = intervalo
    Ea = 100  # Error aproximado relativo.
    i = 1  # Contador del número de iteraciones
    M_previa = 0  # Punto medio previo
    M_actual = (a + b) / 2  # Inicialización de M_actual
    
    while i < Nl and Ea > Es:
        M_previa = M_actual
        M_actual = (a + b) / 2
        
        if f(M_actual) * f(b) < 0:
            a = M_actual
        else:
            b = M_actual
        
        if i > 1:
            Ea = abs((M_actual - M_previa) / M_actual) * 100
        
        i += 1
    
    return M_actual, Ea, i

if __name__ == "__main__":
    f = lambda x: x**3 - 2*x - 5
    
    intervalo = [2, 3]
    Es = 0.01
    Nl = 10

    results = biseccion(f, intervalo, Es, Nl)
    print("El punto aproximado es", results[0], "con un margen de error de", results[1], "alcanzado en", results[2], "iteraciones")
