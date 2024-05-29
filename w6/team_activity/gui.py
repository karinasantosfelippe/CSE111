'''
Author: Karina Santos Felippe
Problem Statement:
    Almost all of the programs that you wrote for this course receive input from and print results to a terminal window. However, most users prefer to interact with a program through a graphical user interface (GUI) that contains icons, text fields, drop-down lists, buttons, etc. Within a GUI, the individual components (icons, text fields, etc.) are called widgets. Most libraries for creating GUIs use object oriented programming because each widget is an object with attributes and methods.
'''
# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
import math

def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Simple Calculation")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()

# The controls in a graphical user interface (GUI) are called widgets,
# and each widget is an object. Because a GUI has many widgets and
# each widget is an object, the code to make a GUI usually has many
# variables to store the many objects. Because there are so many
# variable names, programmers often adopt a naming convention to help
# a programmer keep track of all the variables. One popular naming
# convention is to type a three letter prefix in front of the names
# of all variables that store GUI widgets, according to this list:
#
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Radius:"
    lbl_radius = Label(frm_main, text="Radius (1 - 100):")

    # Create an integer entry box where the user will enter the radius.
    ent_radius = IntEntry(frm_main, width=4, lower_bound=1, upper_bound=100)

    # Create labels to display the units.
    lbl_radius_units = Label(frm_main, text="meters")

    # Create labels that will display the results.
    lbl_circle_area = Label(frm_main, width=7)
    lbl_area_units = Label(frm_main, text="meters")

    # Create status label
    lbl_status = Label(frm_main, width=10)

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_radius.grid(        row=0, column=0, padx=3, pady=3, sticky="e")
    ent_radius.grid(        row=0, column=1, padx=3, pady=3, sticky="w")
    lbl_radius_units.grid(  row=0, column=2, padx=0, pady=3, sticky="w")

    lbl_circle_area.grid(row=1, column=0, padx=3, pady=3, columnspan=2, sticky="e")
    lbl_area_units.grid( row=1, column=2, padx=0, pady=3, sticky="w")

    btn_clear.grid( row=2, column=0, padx=3, pady=3, sticky="w")
    lbl_status.grid(row=2, column=2, padx=3, pady=3, columnspan=4, sticky="e")

    # This function will be called each time the user releases a key.
    def calculate(event):
        """Compute and display the area of a circle.
        """
        try:
            # Get the radius.
            radius = ent_radius.get()

            # Compute the area.
            area = math.pi * (radius ** 2)

            # Display the area for the user to see.
            lbl_circle_area.config(text=f"{area:.2f}")
            lbl_status.config(text="")

        except ValueError:
            # When the user deletes all the digits in the age
            # entry box, clear the slowest and fastest labels.
            lbl_circle_area.config(text="")
            lbl_status.config(text="Invalid Input")


    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_radius.clear()
        lbl_circle_area.config(text="")
        lbl_status.config(text="")
        ent_radius.focus()

    # Bind the calculate function to the age entry box so
    # that the computer will call the calculate function
    # when the user changes the text in the entry box.
    ent_radius.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the age entry box.
    ent_radius.focus()


# If this file is executed like this:
# > python gui.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()