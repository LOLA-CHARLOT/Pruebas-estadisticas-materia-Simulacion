import tkinter as tk
from tkinter import messagebox
from interfaz import InterfazGrafica

def main():
    root = tk.Tk()
    root.title("Pruebas Estadísticas")
    app = InterfazGrafica(root)
    root.mainloop()

if __name__ == "__main__":
    main()
