# Definir el algoritmo de cuadrados medios
def cuadrados_medios(seed, n_iter=10):
    resultados = []
    semilla = seed
    for _ in range(n_iter):
        cuadrado = semilla ** 2  # Elevar al cuadrado
        cuadrado_str = str(cuadrado)  # Convertir el cuadrado a cadena para manipular los dígitos
        
        # Rellenar con ceros a la izquierda si tiene menos de 8 dígitos
        if len(cuadrado_str) < 8:
            cuadrado_str = cuadrado_str.zfill(8)

        # Tomar los 4 dígitos centrales
        start = (len(cuadrado_str) - 4) // 2
        digitos_centrales = cuadrado_str[start:start + 4]
        
        # El nuevo número será el valor de los dígitos centrales
        semilla = int(digitos_centrales)  # Convertir a entero para la próxima iteración
        resultados.append(digitos_centrales)  # Guardar como cadena para la impresión

    return resultados

# Semilla inicial es 5735
semilla_inicial = 5731
resultados = cuadrados_medios(semilla_inicial)

# Imprimir los resultados de forma correcta
for resultado in resultados:
    print(f"{resultado:04}")  # Siempre imprimimos como 4 dígitos, rellenando si es necesario
