#IDENTIFICADOR DE NUMEROS PRIMOS 1.1

import tkinter as tk
from tkinter import messagebox
from variables import es_primo, numeros_primos_hasta

def verificar_primo(): #La función verificar_primo() se ejecuta cuando se hace clic en el botón "Verificar". Obtiene el número ingresado en el campo de entrada (entry_numero) y realiza las siguientes acciones
    try:
        numero = int(entry_numero.get())
        if numero < 0:
            messagebox.showerror("Error", "Ingrese un número positivo")
            return

        if es_primo(numero): # Verifica si el número ingresado es negativo. Si es así, muestra un mensaje de error y retorna.
            resultado.config(text=f"{numero} es un número primo")
        else:
            resultado.config(text=f"{numero} no es un número primo")

        primos_rango = numeros_primos_hasta(numero) #Llama a la función numeros_primos_hasta(numero) para obtener todos los números primos hasta el número ingresado. Actualiza el texto de las etiquetas primos_label y cantidad_label con los números primos encontrados y su cantidad respectivamente.
        cantidad_primos = len(primos_rango)
        primos_label.config(text=f"Números primos hasta {numero}: {primos_rango}")
        cantidad_label.config(text=f"Cantidad de números primos: {cantidad_primos}")

    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido")

#Configuracion de la interfaz gráfica utilizando la biblioteca Tkinter.

window = tk.Tk()
window.title("IDENTIFICADOR DE NUMEROS PRIMOS 1.1")

#Etiqueta para mostrar el texto "Ingrese un número:" y un campo de entrada para que el usuario ingrese un número.

label_numero = tk.Label(window, text="Ingrese un número:")
label_numero.pack() 

entry_numero = tk.Entry(window)
entry_numero.pack()

#Crea un botón "Verificar" que llama a la función verificar_primo() cuando se hace clic en él.

boton_verificar = tk.Button(window, text="Verificar", command=verificar_primo)
boton_verificar.pack()

#Crea etiquetas para mostrar el resultado de la verificación 

resultado = tk.Label(window, text="")
resultado.pack()

primos_label = tk.Label(window, text="")
primos_label.pack()

cantidad_label = tk.Label(window, text="")
cantidad_label.pack()

#Inicia el bucle principal de la interfaz gráfica.

window.mainloop()