from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
#import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)
    #pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }


    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent= 4)
            finally:
                entry_website.delete(0, END)
                entry_password.delete(0, END)

def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            website_key = entry_website.get()
            website_password = data[website_key]["password"]
    except FileNotFoundError:
        messagebox.showinfo(title= "Oops", message= "There are no passwords saved.")

    except KeyError as website:
        messagebox.showinfo(title= "Oops", message= f"No details for {website} exist.")
    else:
        messagebox.showinfo(title= f"{website_key}", message=f"Website: {website_key} \nPassword: {website_password}")
    finally:
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
entry_website = Entry(width= 21, justify="left")
entry_email = Entry(width= 35, justify="left")
entry_password = Entry(width= 21, justify="left")
button_search = Button(text= "Search", command= find_password)
button_add = Button(text= "Add", width= 36, justify= "left", command= save)
button_generate = Button(text= "Generate Password", command= generate)


# Widget Layout
canvas.grid(row= 0, column= 1)
entry_website.grid(row=1, column= 1, columnspan= 1, ipadx= 35)
entry_website.focus()
entry_email.grid(row=2, column= 1, columnspan= 2, ipadx= 50)
entry_email.insert(0, "example@email.com")
entry_password.grid(row=3, column= 1, ipadx= 35)
label_website.grid(row= 1, column= 0)
label_email.grid(row= 2, column= 0)
label_password.grid(row= 3, column= 0)
button_search.grid(row=1, column= 2, ipadx= 33)
button_add.grid(row=4, column= 1, columnspan= 2, ipadx= 28)
button_add.grid(row=4, column= 1, columnspan= 2, ipadx= 28)
button_generate.grid(row=3, column= 2)


window.mainloop()