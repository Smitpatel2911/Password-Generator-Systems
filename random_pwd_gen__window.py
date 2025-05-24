import random  # for making random choices of computer number
import string # for string related operations
# window ui creation by following

from tkinter import *

# initializing the window for game
app = Tk()
app.title("Password Generator")
app.configure(bg = "#121212", padx=20, pady=20)
app.option_add("*Font",("Impact",20))

# Creating frame for the title 
title_frame = Frame(app)

# creating label for the label
title_label = Label(title_frame, text="Strong Password Generator",font=("Impact", 28), bg = "#121212", fg="#E0E0E0")

# seting title frame and in that title will be inside that frame
title_frame.pack()
title_label.pack()

# craeting frame to ask user the length
Detail_frame = Frame(app)


# Asking the 
que_label = Label(Detail_frame, text="Enter the Length Require for password : ",font=("Arial Narrow", 24), bg = "#121212", fg="#E0E0E0")
que_label.grid(column = 0, row = 1)


# Taking password length from the user
entry_length = Entry(Detail_frame, width = 2, font = ("Arial Narrow", 24), bg = "#121212", fg="#E0E0E0", )
entry_length.grid(column = 1, row = 1)

Detail_frame.configure(bg = "#121212")
Detail_frame.pack()
def generate_password():
    from tkinter import messagebox
    temp = entry_length.get()
    if temp.strip() == '':
        messagebox.showerror("Input Error", "Please enter the length of the password.")
        return
    if not temp.isdigit():
        messagebox.showerror("Input Error", "Please enter a valid number.")
        return

    pwd_len = int(temp)
    
    # deciding char for password
    char_pwd = string.ascii_letters + string.digits + string.punctuation
    
    # making to password as string
    password = ''.join(random.choice(char_pwd) for _ in range(pwd_len))
    
    entry_result.delete(0, END)
    entry_result.insert(0, password)

# Button to generate password
btn_generate = Button(app, text=" Generate Password ", command=generate_password)
btn_generate.pack(pady=10)

# Entry to show generated password
entry_result = Entry(app, width=40)
entry_result.pack(pady=10)

app.mainloop()