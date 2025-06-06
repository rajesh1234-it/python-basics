import tkinter as tk
from tkinter import ttk

# Conversion factors to meters
conversion_factors = {
    "Miles": 1609.34,
    "Kilometers": 1000,
    "Meters": 1,
    "Feet": 0.3048,
    "Inches": 0.0254
}

def convert():
    try:
        value = float(entry.get())
        from_unit = from_combo.get()
        to_unit = to_combo.get()

        meters = value * conversion_factors[from_unit]
        result = meters / conversion_factors[to_unit]

        result_label.config(text=f"{round(result, 4)} {to_unit}")
    except ValueError:
        result_label.config(text="Enter a valid number")

# GUI setup
window = tk.Tk()
window.title("Distance Unit Converter")
window.config(padx=30, pady=20)

# Entry
entry = tk.Entry(window, width=10)
entry.grid(row=0, column=1)
entry.focus()

# From Label & Combobox
tk.Label(window, text="From:").grid(row=0, column=0)
from_combo = ttk.Combobox(window, values=list(conversion_factors.keys()), state="readonly", width=12)
from_combo.grid(row=0, column=2)
from_combo.set("Miles")

# To Label & Combobox
tk.Label(window, text="To:").grid(row=1, column=0)
to_combo = ttk.Combobox(window, values=list(conversion_factors.keys()), state="readonly", width=12)
to_combo.grid(row=1, column=2)
to_combo.set("Kilometers")

# Convert Button
convert_button = tk.Button(window, text="Convert", command=convert)
convert_button.grid(row=2, column=0, columnspan=3, pady=10)

# Result Label
result_label = tk.Label(window, text="", font=("Arial", 14, "bold"))
result_label.grid(row=3, column=0, columnspan=3)

window.mainloop()
