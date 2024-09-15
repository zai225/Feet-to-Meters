import tkinter as tk
from tkinter import ttk, messagebox
from currency_converter import CurrencyConverter

c = CurrencyConverter()

# Function of currency conversion
def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()

        print(f"Coverting {amount} ftom {from_currency} to {to_currency}")
        
        converted_amount = c.convert(amount, from_currency, to_currency)
        result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    except Exception as e:
        messagebox.showerror("Conversion Error", f"Error: {e}")

root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x350")

root.configure(bg="#34495E")

title_label = tk.Label(root, text="Currency Converter", font=('Arial', 20, 'bold'), fg="white", bg="#34495E")
title_label.pack(pady=10)

amount_label = tk.Label(root, text="Enter Amount", font=('Arial', 14), fg="white", bg="#34495E")
amount_label.pack(pady=5)
amount_entry = tk.Entry(root, font=('Arial', 14), bg="#D5DBDB", fg="black")
amount_entry.pack(pady=5)

from_currency_label = tk.Label(root, text="From Currency", font=('Arial', 14), fg="white", bg="#34495E")
from_currency_label.pack(pady=5)

from_currency_var = tk.StringVar()
from_currency_combobox = ttk.Combobox(root, textvariable=from_currency_var, values=list(c.currencies), font=('Arial', 14))
from_currency_combobox.pack(pady=5)
from_currency_combobox.set('USD')

to_currency_label = tk.Label(root, text="To Currency", font=('Arial', 14), fg="white", bg="#34495E")
to_currency_label.pack(pady=5)

to_currency_var = tk.StringVar()
to_currency_combobox = ttk.Combobox(root, textvariable=to_currency_var, values=list(c.currencies), font=('Arial', 14))
to_currency_combobox.pack(pady=5)
to_currency_combobox.set('INR')

convert_button = tk.Button(root, text="Convert", font=('Arial', 14), bg="#2ECC71", fg="white", activebackground="#28B463", activeforeground="white", command=convert_currency)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="", font=('Arial', 14), fg="white", bg="#34495E")
result_label.pack(pady=5)

root.mainloop()
