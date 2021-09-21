import tkinter as tk
main_window = tk.Tk()
main_window.title("Mile to Km Converter")

# Variables
user_input = tk.StringVar
user_input = "0"
answer = tk.StringVar()
answer = "0"

# Functions
def conversion(num_miles):
    global answer
    converted = float(num_miles) * 1.609
    return str(converted)


# Create widgets for window
entry_user = tk.Entry(textvariable= user_input)
lbl_miles = tk.Label(text= "Miles")
lbl_is_equal = tk.Label(text= "is equal to")
lbl_answer = tk.Label(text= answer)
lbl_Km = tk.Label(text= "Km")
button_calculate = tk.Button(text= "Calculate", command= conversion(user_input))

# Label Placement
entry_user.grid(row= 1, column= 2)
lbl_miles.grid(row=1, column=3)
lbl_is_equal.grid(row=2, column=1)
lbl_answer.grid(row=2, column= 2)
lbl_Km.grid(row=2, column=3)
button_calculate.grid(row=3, column=2)

tk.mainloop()


