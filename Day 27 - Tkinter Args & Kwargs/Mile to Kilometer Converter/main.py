import tkinter as tk
main_window = tk.Tk()
main_window.title("Mile to Km Converter")


# Functions
def conversion():
    user_input = entry_user.get()
    converted = float(user_input) * 1.609
    lbl_answer.config(text=converted)


# Create widgets for window
entry_user = tk.Entry()
lbl_miles = tk.Label(text= "Miles")
lbl_is_equal = tk.Label(text= "is equal to")
lbl_answer = tk.Label(text= "0")
lbl_Km = tk.Label(text= "Km")
button_calculate = tk.Button(text= "Calculate", command= conversion)

# Label Placement
entry_user.grid(row= 1, column= 2)
lbl_miles.grid(row=1, column=3)
lbl_is_equal.grid(row=2, column=1)
lbl_answer.grid(row=2, column=2)
lbl_Km.grid(row=2, column=3)
button_calculate.grid(row=3, column=2)

tk.mainloop()


