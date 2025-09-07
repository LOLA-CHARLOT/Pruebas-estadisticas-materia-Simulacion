import numpy as np
from scipy import stats

class PruebaMedias:
    @staticmethod
    def prueba_t_muestra_unica(data, valor_teorico):
        """
        Prueba t para una muestra: Compara la media de la muestra con un valor teórico.
        """
        t_stat, p_value = stats.ttest_1samp(data, valor_teorico)
        return t_stat, p_value

    @staticmethod
    def prueba_t_dos_muestras(data1, data2):
        """
        Prueba t para dos muestras independientes.
        """
        t_stat, p_value = stats.ttest_ind(data1, data2)
        return t_stat, p_value


class PruebaVarianza:
    @staticmethod
    def prueba_f(data1, data2):
        """
        Prueba F para comparar las varianzas de dos muestras.
        """
        var1 = np.var(data1, ddof=1)
        var2 = np.var(data2, ddof=1)
        f_stat = var1 / var2
        return f_stat


class PruebaChiCuadrado:
    @staticmethod
    def prueba_uniformidad(observados, k):
        """
        Prueba chi-cuadrado de uniformidad.
        """
        esperado = [sum(observados) / k] * k
        chi2_stat, p_value = stats.chisquare(observados, esperado)
        return chi2_stat, p_value
