import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from generadores import Generador
from pruebas import PruebaMedias, PruebaVarianza, PruebaChiCuadrado
from graficos import mostrar_histograma, mostrar_tabla_frecuencias

class InterfazGrafica:
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x400")
        
        # Configuración de pestañas
        self.tab_control = ttk.Notebook(master)
        self.tab_generador = ttk.Frame(self.tab_control)
        self.tab_pruebas = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_generador, text="Generador")
        self.tab_control.add(self.tab_pruebas, text="Pruebas")
        self.tab_control.pack(expand=1, fill="both")
        
        # Pestaña Generador
        self.n_label = tk.Label(self.tab_generador, text="Tamaño de muestra:")
        self.n_label.grid(row=0, column=0)
        self.n_entry = tk.Entry(self.tab_generador)
        self.n_entry.grid(row=0, column=1)
        
        self.semilla_label = tk.Label(self.tab_generador, text="Semilla:")
        self.semilla_label.grid(row=1, column=0)
        self.semilla_entry = tk.Entry(self.tab_generador)
        self.semilla_entry.grid(row=1, column=1)
        
        self.generar_button = tk.Button(self.tab_generador, text="Generar", command=self.generar)
        self.generar_button.grid(row=2, column=0, columnspan=2)
        
        # Pestaña Pruebas
        self.test_button = tk.Button(self.tab_pruebas, text="Realizar prueba", command=self.realizar_prueba)
        self.test_button.grid(row=0, column=0)
    
    def generar(self):
        # Lógica para generar los datos
        try:
            n = int(self.n_entry.get())
            semilla = int(self.semilla_entry.get())
            datos = Generador.generar_uniforme(n, semilla)
            mostrar_histograma(datos)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def realizar_prueba(self):
        # Realizar la prueba, aquí es un ejemplo de prueba de medias
        n = int(self.n_entry.get())
        datos = Generador.generar_uniforme(n)
        t_stat, p_value = PruebaMedias.prueba_t_muestra_unica(datos, 0.5)
        messagebox.showinfo("Resultados", f"T-stat: {t_stat}, p-value: {p_value}")
