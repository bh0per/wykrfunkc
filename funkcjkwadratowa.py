import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def funkcja_kwadratowa(a, b, c, x):
    return a * x**2 + b * x + c

def rysuj_funkcje_kwadratowa(a, b, c):
    x = np.linspace(-10, 10, 100)
    y = funkcja_kwadratowa(a, b, c, x)

    figure, ax = plt.subplots()
    ax.plot(x, y, label=f"{a}x^2 + {b}x + {c}")
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(color='gray', linestyle='--', linewidth=0.5)
    ax.legend()
    ax.set_title('Funkcja Kwadratowa')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    return figure

def aktualizuj_wykres():
    a = float(a_entry.get())
    b = float(b_entry.get())
    c = float(c_entry.get())

    figure = rysuj_funkcje_kwadratowa(a, b, c)

    canvas = FigureCanvasTkAgg(figure, master=main_window)
    canvas_widget = canvas.get_tk_widget()

    canvas_widget.grid(row=3, column=0, columnspan=3)

# Tworzenie głównego okna
main_window = tk.Tk()
main_window.title("Wykres Funkcji Kwadratowej")

# Etykiety i pola tekstowe dla współczynników
tk.Label(main_window, text="a:").grid(row=0, column=0)
a_entry = tk.Entry(main_window)
a_entry.grid(row=0, column=1)

tk.Label(main_window, text="b:").grid(row=1, column=0)
b_entry = tk.Entry(main_window)
b_entry.grid(row=1, column=1)

tk.Label(main_window, text="c:").grid(row=2, column=0)
c_entry = tk.Entry(main_window)
c_entry.grid(row=2, column=1)

# Przycisk do aktualizacji wykresu
ttk.Button(main_window, text="Aktualizuj Wykres", command=aktualizuj_wykres).grid(row=2, column=2)

# Uruchomienie głównej pętli programu
main_window.mainloop()