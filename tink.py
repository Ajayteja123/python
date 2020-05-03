import tkinter as tk
from csv import DictWriter
import os
from tkinter import ttk
win = tk.Tk()
win.title("ajay")

# to create title
# their are to ways to print lable 1)pack,2)grid.By using pack we get title in middle
name_label = ttk.Label(win, text="enter the name: ")
name_label.grid(row=0, column=0, sticky=tk.W)

age_label = ttk.Label(win, text="enter your age: ")
age_label.grid(row=1, column=0, sticky=tk.W)

email_label = ttk.Label(win, text="enter your mail id: ")
email_label.grid(row=2, column=0, sticky=tk.W)

# create entry box
name_var = tk.StringVar()
name_entrybox = ttk.Entry(win, width=17, textvariable=name_var)
name_entrybox.grid(row=0, column=1)
name_entrybox.focus()

email_var = tk.StringVar()
email_entrybox = ttk.Entry(win, width=17, textvariable=email_var)
email_entrybox.grid(row=2, column=1)

age_var = tk.StringVar()
age_entrybox = ttk.Entry(win, width=17, textvariable=age_var)
age_entrybox.grid(row=1, column=1)

gender_label = tk.Label(win, text="select your gender")
gender_label.grid(row=3, column=0)

profession_label = tk.Label(win, text="select profession: ")
profession_label.grid(row=4, column=0)

# creating combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(
    win, width=14, textvariable=gender_var, state='readonly')
gender_combobox['values'] = ("male", "female", "other")
gender_combobox.current(0)
gender_combobox.grid(row=3, column=1)

# radiobutton
usertype = tk.StringVar()
radiobtn1 = ttk.Radiobutton(
    win, text='student', value='student', variable=usertype)
radiobtn1.grid(row=4, column=1)

radiobtn2 = ttk.Radiobutton(
    win, text='teacher', value='Teacher', variable=usertype)
radiobtn2.grid(row=4, column=2)


# checkbutton
check_var = tk.IntVar()
checkbtn = ttk.Checkbutton(
    win, text="i agree that above details are correct", variable=check_var)
# checkbtn.selection_handle(1)
checkbtn.grid(row=5, columnspan=3)
# button


def action():
    username = name_var.get()
    useremail = email_var.get()
    userage = age_var.get()
    gender = gender_var.get()
    profession = usertype.get()
    if check_var.get() == 0:
        agree = "Not agreed"
    else:
        agree = "agreed"
    with open('file.txt', 'a') as f:
        f.write(f"{username},{userage},{useremail},{gender},{profession},{agree}\n")
    print(f"{username} is {userage} years old and email_id  is {useremail} gender is {gender} and he/she is {profession} {agree}")
    name_entrybox.delete(0, tk.END)
    age_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)
    name_label.configure(foreground='blue')
    submit_button.configure(foreground='blue')

# def action():
#     username = name_var.get()
#     useremail = email_var.get()
#     userage = age_var.get()
#     gender = gender_var.get()
#     profession = usertype.get()
#     if check_var.get() == 0:
#         agree = "Not agreed"
#     else:
#         agree = "agreed"

#         with open('text.csv', 'a', newline='') as f:
#             dict_Writer = Dict_Writer(
#                 f, fieldnames=['username', 'useremail ', 'userage', 'gender', 'profession', 'agree'])
#             if os.start('fie.csv').st_size == 0:
#                 dict_Writer.writeheader()
#             dict_Writer.writerow({
#                 'username': username,
#                 'useremail': useremail,
#                 'userage': userage,
#                 'gender': gender,
#                 'profession': profession,
#                 'agree': agree

#             })

    name_entrybox.delete(0, tk.END)
    age_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)
    name_label.configure(foreground='blue')


submit_button = tk.Button(win, text="submit", command=action)
submit_button.grid(row=6, column=0)

win.mainloop()
