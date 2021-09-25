from tkinter import *
from tkinter import messagebox
import random
#import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    entry_password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for char in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    entry_password.insert(0, f"{password}")
    #pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    global entry_website, entry_email, entry_password
    user_website = str(entry_website.get())
    user_email = str(entry_email.get())
    user_password = str(entry_password.get())

    if len(user_website) == 0 or len(user_email) == 0 or len(user_password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=user_website, message= f"These are the details entered: \nEmail: {user_email} \nPassword: {user_password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt.", mode="a") as txt_file:
                txt_file.write(f"{user_website} | {user_email} | {user_password}\n")
            entry_website.delete(0, END)
            entry_password.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx= 50, pady= 20)
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
button_add = Button(text= "Add", width= 36, justify= "left", command= save)
button_generate = Button(text= "Generate Password", command= generate)


# Widget Layout
canvas.grid(row= 0, column= 1)
entry_website.grid(row=1, column= 1, columnspan= 2, ipadx= 50)
entry_website.focus()
entry_email.grid(row=2, column= 1, columnspan= 2, ipadx= 50)
entry_email.insert(0, "example@email.com")
entry_password.grid(row=3, column= 1, ipadx= 35)
label_website.grid(row= 1, column= 0)
label_email.grid(row= 2, column= 0)
label_password.grid(row= 3, column= 0)
button_add.grid(row=4, column= 1, columnspan= 2, ipadx= 28)
button_generate.grid(row=3, column= 2)


window.mainloop()
