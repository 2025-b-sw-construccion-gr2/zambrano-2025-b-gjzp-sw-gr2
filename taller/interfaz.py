import tkinter as tk
from tkinter import messagebox

def click_boton(valor):
    # Inserta el número o signo en la pantalla
    pantalla.insert(tk.END, valor)

def limpiar():
    pantalla.delete(0, tk.END)

def calcular():
    try:
        # La función eval() procesa la cadena de texto como una operación matemática
        resultado = eval(pantalla.get())
        limpiar()
        pantalla.insert(0, resultado)
    except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir entre cero")
        limpiar()
    except Exception:
        messagebox.showerror("Error", "Entrada no válida")
        limpiar()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Interactiva")
ventana.geometry("300x400")
ventana.configure(bg="#2c3e50") # Color de fondo creativo

# Pantalla de visualización (Entry)
pantalla = tk.Entry(ventana, font=("Arial", 20), borderwidth=5, relief="flat", justify="right")
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

# Definición de botones (Texto, Fila, Columna, Color)
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('**', 4, 2), ('+', 4, 3) # ** es Potencia en Python
]

# Crear botones dinámicamente con estilos
for (texto, fila, col) in botones:
    color_btn = "#ecf0f1" if texto.isdigit() or texto == '.' else "#f39c12"
    tk.Button(ventana, text=texto, width=5, height=2, bg=color_btn, font=("Arial", 12, "bold"),
              command=lambda t=texto: click_boton(t)).grid(row=fila, column=col, padx=2, pady=2)

# Botones especiales: Limpiar y Calcular
tk.Button(ventana, text="C", width=12, height=2, bg="#e74c3c", fg="white", font=("Arial", 12, "bold"),
          command=limpiar).grid(row=5, column=0, columnspan=2, padx=2, pady=5)

tk.Button(ventana, text="=", width=12, height=2, bg="#27ae60", fg="white", font=("Arial", 12, "bold"),
          command=calcular).grid(row=5, column=2, columnspan=2, padx=2, pady=5)

ventana.mainloop()