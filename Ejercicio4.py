# Definir el algoritmo de productos medios con dos semillas
def productos_medios_dos_semillas(seed1, seed2, n_iter=5, n_digitos=4):
    resultados = []
    semilla1 = seed1
    semilla2 = seed2
    for _ in range(n_iter):
        # Multiplicar ambas semillas
        producto = semilla1 * semilla2
        producto_str = str(producto)  # Convertir el producto a cadena de texto
        
        # Asegurarse de que siempre tengamos al menos 8 dígitos
        if len(producto_str) < 8:
            producto_str = producto_str.zfill(8)  # Rellenar con ceros a la izquierda si es necesario
        
        # Tomar los 4 dígitos centrales
        start = (len(producto_str) - 4) // 2  # Posición de inicio para extraer 4 dígitos centrales
        digitos_centrales = producto_str[start:start + 4]
        
        # Convertir los dígitos centrales a entero
        semilla2 = int(digitos_centrales)  # El resultado será la nueva semilla 2
        resultados.append(digitos_centrales)  # Guardamos como cadena para impresión
    
    return resultados

# Semillas iniciales
semilla_inicial_1 = 6965
semilla_inicial_2 = 9803
resultados = productos_medios_dos_semillas(semilla_inicial_1, semilla_inicial_2)

# Imprimir los resultados
for resultado in resultados:
    print(resultado)  # Imprime cada semilla de 4 dígitos
