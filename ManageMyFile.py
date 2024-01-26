print ("bust!")
print ("I'm tweakin")
print ("I'm geekin")

import os
from tkinter import Tk, Label, Entry, Button, Listbox, Scrollbar
from threading import Thread

def create_file():
    file_name = file_name_entry.get()
    try:
        with open(file_name, 'w') as file:
            result_label.config(text=f"File '{file_name}' created successfully.")
            refresh_file_list(file_listbox)
    except IOError:
        result_label.config(text=f"Failed to create the file '{file_name}'.")

def delete_file():
    selected_file = file_listbox.get(file_listbox.curselection())
    try:
        os.remove(selected_file)
        result_label.config(text=f"File '{selected_file}' deleted successfully.")
        refresh_file_list(file_listbox)
    except FileNotFoundError:
        result_label.config(text=f"The file '{selected_file}' does not exist.")
    except PermissionError:
        result_label.config(text=f"You do not have permission to delete the file '{selected_file}'.")

def rename_file():
    selected_file = file_listbox.get(file_listbox.curselection())
    new_name = new_name_entry.get()
    try:
        os.rename(selected_file, new_name)
        result_label.config(text=f"File '{selected_file}' renamed to '{new_name}' successfully.")
        refresh_file_list(file_listbox)
    except FileNotFoundError:
        result_label.config(text=f"The file '{selected_file}' does not exist.")
    except PermissionError:
        result_label.config(text=f"You do not have permission to rename the file '{selected_file}'.")

def refresh_file_list(listbox):
    listbox.delete(0, "end")
    files = os.listdir()
    for file in files:
        listbox.insert("end", file)

def open_gui():
    # Create the GUI window
    window = Tk()
    window.title("ManageMyFile")
    window.geometry("400x300")  # Set the size of the window (width x height)
    window.configure(bg="lightgray")  # Set the background color of the window

    # Create and position the GUI elements
    file_name_label = Label(window, text="File Name:", bg="lightgray")
    file_name_label.pack()
    file_name_entry = Entry(window)
    file_name_entry.pack()

    new_name_label = Label(window, text="New Name:", bg="lightgray")
    new_name_label.pack()
    new_name_entry = Entry(window)
    new_name_entry.pack()

    create_button = Button(window, text="Create", command=create_file)
    create_button.pack()

    delete_button = Button(window, text="Delete", command=delete_file)
    delete_button.pack()

    rename_button = Button(window, text="Rename", command=rename_file)
    rename_button.pack()

    file_list_label = Label(window, text="Files:", bg="lightgray")
    file_list_label.pack()

    file_listbox = Listbox(window, selectbackground="lightblue")
    file_listbox.pack(fill="both", expand=True)

    scrollbar = Scrollbar(window)
    scrollbar.pack(side="right", fill="y")

    file_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=file_listbox.yview)

    refresh_file_list(file_listbox)

    result_label = Label(window, text="", bg="lightgray")
    result_label.pack()

    # Start the GUI event loop
    window.mainloop()

# Create and start a new thread to run the GUI
gui_thread = Thread(target=open_gui)
gui_thread.start()