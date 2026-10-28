
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Delivery App")
window.geometry("980x700")                                                                              

# Email
email_label = tk.Label(window, text="Email")
email_label.place(x=130, y=40)

email_entry = tk.Entry(window, width=35)
email_entry.place(x=230, y=40)

# Password
password_label = tk.Label(window, text="Password")
password_label.place(x=90, y=105)

password_entry = tk.Entry(window, width=35, show="*")
password_entry.place(x=230, y=105)

# Food
food_label = tk.Label(
    window,
    text="What food would you like: Chicken sandwich, B.L.T, Veg sandwich? Or None"
)
food_label.place(x=30, y=230)

food_entry = tk.Entry(window, width=35)
food_entry.place(x=25, y=270)

food_quantity = tk.Spinbox(window, from_=0, to=2, width=25)
food_quantity.place(x=500, y=270)

# Beverage
beverage_label = tk.Label(
    window,
    text="What beverage would you like: Cola, Fanta, Orange Juice, Water or None?"
)
beverage_label.place(x=35, y=350)

beverage_entry = tk.Entry(window, width=35)
beverage_entry.place(x=25, y=390)

beverage_quantity = tk.Spinbox(window, from_=0, to=2, width=25)
beverage_quantity.place(x=500, y=390)

# Dessert
dessert_label = tk.Label(
    window,
    text="What dessert would you like: Ice Cream, Ice Lolly, Chocolate Cake or None?"
)
dessert_label.place(x=25, y=470)

dessert_entry = tk.Entry(window, width=35)
dessert_entry.place(x=25, y=510)

dessert_quantity = tk.Spinbox(window, from_=0, to=2, width=25)
dessert_quantity.place(x=500, y=510)

# Submit Order
def submit_order():
    email = email_entry.get().strip()
    password = password_entry.get()

    food = food_entry.get().strip()
    food_amount = int(food_quantity.get())

    beverage = beverage_entry.get().strip()
    beverage_amount = int(beverage_quantity.get())

    dessert = dessert_entry.get().strip()
    dessert_amount = int(dessert_quantity.get())

    message = f" You have ordered {food_amount} {food}s, {beverage_amount} {beverage}s and {dessert_amount} {dessert}s?\n Press <<OK>> to confirm" 
    messagebox.showinfo("Conformation", message)

submit_button = tk.Button(
    window,
    text="Submit Order",
    command=submit_order,
    padx=10,
    pady=5
)
submit_button.place(x=345, y=630)

window.mainloop()
