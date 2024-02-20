import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk


def plot_function():
    try:
        # Pobranie równania funkcji z pola tekstowego
        function_equation = entry_equation.get()

        # Funkcja, która oblicza wartości funkcji dla podanego zakresu x
        def funkcja(x):
            return eval(function_equation)

        # Tworzenie danych do wykresu
        x = np.linspace(-10, 10, 400)
        y = funkcja(x)

        # Czyszczenie obecnie wyświetlanego wykresu
        ax.clear()

        # Generowanie nowego wykresu
        ax.plot(x, y)
        ax.set_title('Wykres funkcji: ' + function_equation)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.grid(True)

        # Odświeżenie wykresu
        canvas.draw()

    except Exception as e:
        # Wyświetlenie komunikatu o błędzie, jeśli wystąpił problem z obliczeniami
        lbl_error.config(text=str(e))


# Tworzenie głównego okna
root = tk.Tk()
root.title("Wykres funkcji")

# Tworzenie pola tekstowego do wprowadzania równania funkcji
lbl_equation = tk.Label(root, text="Podaj równanie funkcji:")
lbl_equation.pack()
entry_equation = tk.Entry(root)
entry_equation.pack()

# Tworzenie przycisku do rysowania wykresu
btn_plot = tk.Button(root, text="Narysuj wykres", command=plot_function)
btn_plot.pack()

# Tworzenie obszaru wykresu
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Etykieta na wyświetlanie błędów
lbl_error = tk.Label(root, text="", fg="red")
lbl_error.pack()

# Uruchomienie głównej pętli aplikacji
root.mainloop()
