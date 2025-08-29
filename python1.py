import tkinter as tk
from tkinter import messagebox

# In-memory product list
products = []

# Functions
def add_product():
    name = name_entry.get()
    try:
        price = float(price_entry.get())
        quantity = int(quantity_entry.get())
        products.append({'name': name, 'price': price, 'quantity': quantity})
        update_listbox()
        clear_fields()
    except ValueError:
        messagebox.showerror("Error", "Invalid price or quantity")

def update_product():
    selected = product_listbox.curselection()
    if selected:
        index = selected[0]
        try:
            products[index] = {
                'name': name_entry.get(),
                'price': float(price_entry.get()),
                'quantity': int(quantity_entry.get())
            }
            update_listbox()
            clear_fields()
        except ValueError:
            messagebox.showerror("Error", "Invalid price or quantity")
    else:
        messagebox.showerror("Error", "No product selected")

def delete_product():
    selected = product_listbox.curselection()
    if selected:
        del products[selected[0]]
        update_listbox()
        clear_fields()
    else:
        messagebox.showerror("Error", "No product selected")

def search_product():
    query = name_entry.get().lower()
    product_listbox.delete(0, tk.END)
    for product in products:
        if query in product['name'].lower():
            product_listbox.insert(tk.END, format_product(product))

def update_listbox():
    product_listbox.delete(0, tk.END)
    for product in products:
        product_listbox.insert(tk.END, format_product(product))

def format_product(product):
    return f"{product['name']} | Price: ${product['price']} | Qty: {product['quantity']}"

def on_select(event):
    selected = product_listbox.curselection()
    if selected:
        product = products[selected[0]]
        name_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)
        name_entry.insert(tk.END, product['name'])
        price_entry.insert(tk.END, product['price'])
        quantity_entry.insert(tk.END, product['quantity'])

def clear_fields():
    name_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Retail Management System")

# Labels and Entries
tk.Label(root, text="Product Name").grid(row=0, column=0)
tk.Label(root, text="Price").grid(row=1, column=0)
tk.Label(root, text="Quantity").grid(row=2, column=0)

name_entry = tk.Entry(root)
price_entry = tk.Entry(root)
quantity_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)
price_entry.grid(row=1, column=1)
quantity_entry.grid(row=2, column=1)

# Buttons
tk.Button(root, text="Add", command=add_product).grid(row=0, column=2)
tk.Button(root, text="Update", command=update_product).grid(row=1, column=2)
tk.Button(root, text="Delete", command=delete_product).grid(row=2, column=2)
tk.Button(root, text="Search", command=search_product).grid(row=3, column=0)
tk.Button(root, text="Show All", command=update_listbox).grid(row=3, column=1)
tk.Button(root, text="Clear", command=clear_fields).grid(row=3, column=2)

# Listbox
product_listbox = tk.Listbox(root, width=60, height=10)
product_listbox.grid(row=4, column=0, columnspan=3, pady=10)
product_listbox.bind("<<ListboxSelect>>", on_select)

# Run the app
root.mainloop()
