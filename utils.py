from customtkinter import *

def errorLogin(message):
    err = CTkToplevel()
    err.title("Error")
    err.geometry("100x100")
    err.minsize(300, 100)
    err.config(bg="white")
    CTkLabel(err, text=message, font=('sans rerif', 12)).pack()
    CTkButton(err, font=('sans rerif', 12), border_color="red", fg_color="black",
              hover_color="red", corner_radius=12, border_width=2, text="Ok", height=40, command=err.destroy).pack(pady=10)

def LoginCorrecto(message):
    err = CTkToplevel()
    err.title("Exito")
    err.geometry("100x100")
    err.minsize(300, 100)
    err.config(bg="white")
    CTkLabel(err, text=message, font=('sans rerif', 12)).pack()
    CTkButton(err, font=('sans rerif', 12), border_color="green", fg_color="black",
              hover_color="green", corner_radius=12, border_width=2, text="Ok", height=40, command=err.destroy).pack()