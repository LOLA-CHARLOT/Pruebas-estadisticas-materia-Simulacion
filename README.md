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

Es una buena práctica usar un entorno virtual para manejar las dependencias. Si usas venv para crear el entorno virtual, puedes hacerlo con los siguientes comandos:

python -m venv venv





Crear un entorno virtual (opcional, pero recomendado):

Es una buena práctica usar un entorno virtual para manejar las dependencias. Si usas venv para crear el entorno virtual, puedes hacerlo con los siguientes comandos:

python -m venv venv


Luego, activa el entorno virtual:

En Windows:

venv\Scripts\activate


En macOS/Linux:

source venv/bin/activate


Instalar las dependencias:

Con el entorno virtual activado, instala las bibliotecas necesarias usando el archivo requirements.txt:

pip install -r requirements.txt


Esto instalará todas las dependencias necesarias para el proyecto.

Ejecución

Iniciar la aplicación:

Para iniciar la interfaz gráfica y ejecutar el proyecto, simplemente ejecuta el archivo main.py con Python:

python main.py


Esto abrirá la interfaz gráfica donde podrás:

Seleccionar el generador de números pseudoaleatorios.

Ingresar los parámetros de entrada para las pruebas estadísticas.

Ver los resultados numéricos y gráficos de las pruebas realizadas.

Uso
Generación de Datos

En la pestaña "Generador":

Ingresa el tamaño de la muestra en el campo "Tamaño de muestra".

Ingresa la semilla (si lo deseas) en el campo "Semilla".

Haz clic en el botón Generar para generar los números pseudoaleatorios según los parámetros ingresados.

Se mostrará un histograma con los datos generados.

Realización de Pruebas Estadísticas

En la pestaña "Pruebas":

Puedes seleccionar una de las pruebas estadísticas (prueba de medias, varianza o chi-cuadrado).

Haz clic en el botón Realizar prueba para ejecutar la prueba sobre los datos generados.

Los resultados numéricos (estadística de prueba y valor p) se mostrarán en una ventana emergente.

Funciones de las Pruebas

Prueba de Medias:

Prueba t de una muestra: Compara la media de una muestra con un valor teórico.

Prueba t para dos muestras independientes: Compara las medias de dos muestras independientes.

Prueba de Varianza:

Prueba F: Compara las varianzas de dos muestras para ver si son iguales.

Prueba de Chi-cuadrado de Uniformidad:

Compara las frecuencias observadas de una variable categórica con una distribución uniforme teórica.

Contribuciones

Si deseas contribuir a este proyecto, por favor realiza un fork del repositorio, haz tus cambios y envía un pull request con una descripción clara de lo que has hecho. Las contribuciones son siempre bienvenidas.

Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

Contacto

Si tienes alguna pregunta, no dudes en contactarme a través de GitHub o tu-email@dominio.com
.


### Explicación de las secciones agregadas:

1. **Requisitos**: Se describe la versión mínima de Python que se necesita y las bibliotecas necesarias (numpy, scipy, matplotlib, tkinter).
   
2. **Instalación**: Se explica cómo clonar el repositorio, crear un entorno virtual y cómo instalar las dependencias usando `pip`.

3. **Ejecución**: Se indican los pasos para ejecutar el archivo `main.py` y cómo interactuar con la interfaz gráfica para realizar las pruebas estadísticas y visualizar los resultados.

4. **Uso**: Descripción básica de cómo utilizar las funcionalidades principales del sistema: generación de datos y realización de pruebas estadísticas.

---
