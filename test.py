import unittest
import math
from biseccion import biseccion  # Importa la función biseccion
from newton_rhapson import newton_raphson  # Importa la función newton_raphson
from riemman import riemann  # Importa la función riemann
from trapecio import trapecio

class TestAlgorithms(unittest.TestCase):

    def test_biseccion(self):
        f = lambda x: x**3 - 2*x - 5
        intervalo = [2, 3]
        Es = 0.01
        Nl = 10
        result = biseccion(f, intervalo, Es, Nl)
        self.assertAlmostEqual(result[0], 2.095703125, places=5)  # Ajuste en el valor esperado
        self.assertAlmostEqual(result[1], 0.09319664492078285, places=5)
        self.assertEqual(result[2], 10)

    def test_riemann(self):
        f = lambda x: (x**3 - (2*x)-5)
        a = 0
        b = 1
        n = 100
        result = riemann(f, a, b, n)
        self.assertAlmostEqual(result, -5.744975000000001, places=2)

    def test_trapecio(self):
        f = lambda x: ((3*x) / (x**2 + 1))
        a = 1
        b = 2
        n = 4
        result = trapecio(f, a, b, n)
        self.assertAlmostEqual(result, 1.3725844277673545, places=2)

    def test_newton_raphson(self):
        f = lambda x: x**2 - 4
        result, convergence = newton_raphson(f, 3)
        self.assertAlmostEqual(result, 2.000000000000001, places=5)
        self.assertTrue(convergence)

if __name__ == '__main__':
    unittest.main()
