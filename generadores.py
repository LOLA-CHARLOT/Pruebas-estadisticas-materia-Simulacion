import numpy as np

class Generador:
    @staticmethod
    def generar_uniforme(n, semilla=None):
        """
        Genera n números aleatorios distribuidos uniformemente.
        """
        np.random.seed(semilla)
        return np.random.uniform(0, 1, n)

    @staticmethod
    def generar_normal(n, semilla=None):
        """
        Genera n números aleatorios distribuidos normalmente.
        """
        np.random.seed(semilla)
        return np.random.normal(0, 1, n)
