#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk


# main window
root = tk.Tk()
root.wm_geometry("400x225")

# create empty frame
frame_login = tk.Frame(root)
frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, stick="news")

#Activate the grid in our new frame
frame_auth.grid(row=0, column=0, stick="news")
frame_login.grid(row=0, column=0, stick="news")
frame_login.grid()

#
def login():
    frame_auth.tkraise()

#Widgets for frame_login
lbl_username = tk.Label(frame_login, text='Username:', font="Arial 13 bold")
lbl_username.pack(padx=100,pady=10)

# Text box for username
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

#Password textbox
lbl_password = tk.Label(frame_login, text='Password:', font="Arial 13 bold")
lbl_password.pack(padx=100,pady=10)

ent_password = tk.Entry(frame_login, bd=3)
ent_password.pack(pady=5)

#
button_login = tk.Button(frame_login, text="Login", font = "Arial 12 bold", command = login)
button_login.pack(pady=10)

#
lbl_authorized = tk.Label(frame_auth, text='Authorization screen', font="Arial 15 bold")
lbl_authorized.pack(padx=100,pady=10)

frame_login.tkraise()

root.mainloop()