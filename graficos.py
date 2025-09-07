import matplotlib.pyplot as plt

def mostrar_histograma(data, title="Histograma"):
    """
    Muestra un histograma de los datos.
    """
    plt.hist(data, bins=30, edgecolor='black')
    plt.title(title)
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.show()

def mostrar_tabla_frecuencias(data, k):
    """
    Muestra la tabla de frecuencias observadas.
    """
    hist, bins = np.histogram(data, bins=k)
    frecuencias = dict(zip(range(k), hist))
    for i, freq in frecuencias.items():
        print(f"Clase {i}: {freq}")
