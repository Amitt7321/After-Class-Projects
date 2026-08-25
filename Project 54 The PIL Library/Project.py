from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()
window.title("My Photo Album")
window.geometry("450x400")
window.config(bg="burlywood")

title_label = Label(
    window,
    text="My Photo Album",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="lightblue",
    width=25
)
title_label.pack(pady=15)

image_file = Image.open("3d-cute-cartoon-boy-going-260nw-2705851119.webp")
image_file = image_file.resize((300, 200))
 
photo = ImageTk.PhotoImage(image_file)
 
image_label = Label(window, image=photo, bg="burlywood")
image_label.pack(pady=10)

def show_reaction():
    messagebox.showinfo(
        "Photo Reaction",
        "This is a beautiful memory!"
    )

def open_photo_details():
    details_window = Toplevel(window)
    details_window.title("Photo Details")
    details_window.geometry("350x250")
    details_window.config(bg="cream")
 
    heading = Label(
        details_window,
        text="Photo Details",
        font=("Arial", 16, "bold"),
        bg="cream",
        fg="white"
    )
    heading.pack(pady=15)
 
    details = Label(
        details_window,
        text="Photo Name: My Favourite Memory/n"
             "Category: Personal Album/n"
             "Description: A special photo saved in my album.",
        font=("Arial", 11),
        bg="cream",
        justify="left"
    )
    details.pack(pady=10)
 
    close_button = Button(
        details_window,
        text="Close",
        bg="lightpink",
        fg="white",
        command=details_window.destroy
    )
    close_button.pack(pady=15)

reaction_button = Button(
    window,
    text="React to Photo",
    font=("Arial", 12, "bold"),
    bg="Orange",
    fg="yellow",
    command=show_reaction
)
reaction_button.pack(pady=10)
 
details_button = Button(
    window,
    text="View Photo Details",
    font=("Arial", 12, "bold"),
    bg="lightgreen",
    fg="green",
    command=open_photo_details
)
details_button.pack(pady=10)

window.mainloop()