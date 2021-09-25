# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.minsize(200, 200)
window.config(padx= 20, pady= 20)
window.title("Password Manager")
lock_img = PhotoImage(file= "logo.png")
canvas = Canvas(height= 200, width = 200)
canvas.create_image(100, 100, image=lock_img)

# Widget Creation
label_website = Label(text= "Website:")
label_email = Label(text= "Email/ Username:")
label_password = Label(text= "Password:")
entry_website = Entry(width= 35, justify="left")
entry_email = Entry(width= 35, justify="left")
entry_password = Entry(width= 21, justify="left")
button_add = Button(text= "Add", width= 36, justify= "left")
button_generate = Button(text= "Generate Password")


# Widget Layout
canvas.grid(row= 0, column= 1)
entry_website.grid(row=1, column= 1, columnspan= 2, ipadx= 50)
entry_email.grid(row=2, column= 1, columnspan= 2, ipadx= 50)
entry_password.grid(row=3, column= 1, ipadx= 35)
label_website.grid(row= 1, column= 0)
label_email.grid(row= 2, column= 0)
label_password.grid(row= 3, column= 0)
button_add.grid(row=4, column= 1, columnspan= 2, ipadx= 28)
button_generate.grid(row=3, column= 2)


window.mainloop()
