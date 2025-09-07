# Proyecto de Pruebas Estadísticas para los números pseudoaleatorios en Python

Este proyecto implementa tres pruebas estadísticas comunes: prueba de medias, prueba de varianza y prueba de chi-cuadrado de uniformidad. El sistema tiene una interfaz gráfica en Tkinter donde puedes generar datos aleatorios, realizar las pruebas estadísticas y visualizar los resultados en forma de gráficos y tablas.

## Componentes

1. **Generador de Números Pseudoaleatorios**: Permite generar números aleatorios para las pruebas.
2. **Pruebas Estadísticas**: Implementación de las pruebas de medias, varianza y chi-cuadrado.
3. **Interfaz Gráfica**: Permite interactuar con el sistema de manera sencilla.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado Python 3.10 o superior. También necesitarás las siguientes bibliotecas de Python:

- **numpy**: Para manejar arreglos y realizar cálculos matemáticos.
- **scipy**: Para las pruebas estadísticas (t de Student, F, chi-cuadrado).
- **matplotlib**: Para la visualización de datos (gráficos).
- **tkinter**: Para crear la interfaz gráfica de usuario (GUI).

Puedes instalar estas dependencias de la siguiente manera:

## Instalación

1. **Clonar el repositorio:**

   Si aún no tienes el repositorio, clónalo usando git:

   ```bash
   git clone https://github.com/LOLA-CHARLOT/Pruebas-estadisticas-materia-Simulacion.git
   cd proyecto-estadisticas

2. **Crear un entorno virtual (opcional, pero recomendado):**

   Es una buena práctica usar un entorno virtual para manejar las dependencias. Si usas venv para crear el entorno virtual,      puedes hacerlo con los siguientes comandos:
      python -m venv venv

   Luego, activa el entorno virtual:

* En Windows:
   ```bash
         venv\Scripts\activate
* En macOS/Linux:
        source venv/bin/activate

3. **Instalar las dependencias:**
   Con el entorno virtual activado, instala las bibliotecas necesarias usando el archivo requirements.txt:
          ```bash
         pip install -r requirements.txt
   Esto instalará todas las dependencias necesarias para el proyecto.

## Ejecución

1. **Iniciar la aplicación:**

Para iniciar la interfaz gráfica y ejecutar el proyecto, simplemente ejecuta el archivo main.py con Python:

      python main.py

Esto abrirá la interfaz gráfica donde podrás:

   * Seleccionar el generador de números pseudoaleatorios.

   * Ingresar los parámetros de entrada para las pruebas estadísticas.

   * Ver los resultados numéricos y gráficos de las pruebas realizadas.

## Uso

## Generación de datos

En la pestaña "Generador":

   1. Ingresa el tamaño de la muestra en el campo "Tamaño de muestra".
   
   2. Ingresa la semilla (si lo deseas) en el campo "Semilla".
   
   3. Haz clic en el botón Generar para generar los números pseudoaleatorios según los parámetros ingresados.
   
   4. Se mostrará un histograma con los datos generados.

## Realización de pruebas estadísticas

   1. En la pestaña "Pruebas":
   
   Puedes seleccionar una de las pruebas estadísticas (prueba de medias, varianza o chi-cuadrado).
   
   2. Haz clic en el botón Realizar prueba para ejecutar la prueba sobre los datos generados.
   
   3. Los resultados numéricos (estadística de prueba y valor p) se mostrarán en una ventana emergente.

## Funciones de las Pruebas

   1. **Prueba de Medias:**
   
      - **Prueba t de una muestra**: Compara la media de una muestra con un valor teórico.
      
      - **Prueba t para dos muestras independientes**: Compara las medias de dos muestras independientes.
   
   2. **Prueba de Varianza:**
   
      - **Prueba F**: Compara las varianzas de dos muestras para ver si son iguales.
   
   3. **Prueba de Chi-cuadrado de Uniformidad:**
   
      - **Compara las frecuencias** observadas de una variable categórica con una distribución uniforme teórica.


## Capturas de los resultados

   1. **Generadores:**
   <img width="597" height="213" alt="Generador-imagen" src="https://github.com/user-attachments/assets/9602bd23-6d70-459c-a87d-55ac7075b1bf" />

   2. **Pruebas:**
   <img width="597" height="267" alt="Pruebas-imagen" src="https://github.com/user-attachments/assets/bc0c913a-4da5-496b-a8ae-743b969b9d63" />

   3. **Histograma:**
   <img width="644" height="559" alt="Hitograma-imagen" src="https://github.com/user-attachments/assets/407b0fd7-4f29-47f8-b56c-bd6cf8f11e92" />
      
## Bitácora de lo avanzado en clases previamente

   1. **Algoritmo de cuadrados medios:**
      Generar los primeros 5 números r a partir de la semilla 5735. Se adjunta el Ejercicio1 en Files:

<img width="1337" height="546" alt="Ejercicio 1" src="https://github.com/user-attachments/assets/b7dc6cb0-aff2-4026-beb7-e61e5f834107" />


   2. **Ejemplo:**
   Generar los primeros 10 números r a partir de la semilla 5731. Se adjunta el Ejercicio2 en Files:

 <img width="1075" height="544" alt="Ejercicio2" src="https://github.com/user-attachments/assets/d7dbfcfd-347c-4c33-98cc-0eafc2e46f07" />


   3. **Algoritmo de productos medios**
   Generar los primeros 5 números r a partir de las semillas 5015 y 5734. Se adjunta el Ejercicio3 en Files:

<img width="1094" height="699" alt="Ejercicio3" src="https://github.com/user-attachments/assets/94fa6451-bcf9-4f37-970f-9ce147553f13" />
 

   4. **Algoritmo multiplicador constante**
   Generar los primeros 5 números r a partir de la semilla constante 6965 y de la variable 9803. Se adjunta el Ejercicio4 en Files:

<img width="1168" height="592" alt="Ejercicio4" src="https://github.com/user-attachments/assets/5fd4dc04-a040-41b0-8ce0-52d14851b926" />

 ## Contribuciones

Si deseas contribuir a este proyecto, por favor realiza un fork del repositorio, haz tus cambios y envía un pull request con una descripción clara de lo que has hecho. Las contribuciones son siempre bienvenidas.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## Contacto

      Si tienes alguna pregunta, no dudes en contactarme a través de GitHub o charlotmollinedo@gmail.com
