from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    list_of_letters = [random.choice(letters) for char in range(random.randint(8, 10))]
    list_of_symbols = [random.choice(symbols) for char in range(random.randint(2, 4))]
    list_of_numbers = [random.choice(numbers) for char in range(random.randint(2, 4))]

    password_list = list_of_numbers + list_of_symbols + list_of_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title='Ooops', message="Please don't miss any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f'These are the details entered: \n Email: {email}\n Password: {password} \n Is it ok to save?')
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

#Window
window = Tk()
window.config(padx=50,pady=50)
window.title('Password Manager')

#Logo
canvas = Canvas(width=200,height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100,100, image=logo)
canvas.grid(column=1,row=0)

#Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

#Inputs
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(END, 'sherkhan@email.com')

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

#Buttons
generate_password = Button(text='Generate Password', command=generate_password)
generate_password.grid(column=2, row=3)

add_button = Button(text='Add',width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)





window.mainloop()