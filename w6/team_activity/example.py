''' Simple Dialog '''

# from tkinter.simpledialog import askinteger, askstring
# from tkinter import *
# from tkinter import messagebox
# top = Tk()

# top.geometry("100x100")
# def show_int():
#    num = askinteger("Input", "Input an Integer")
#    print(num)
# def show_str():
#    str_input = askstring("Input", "Input a String")
#    print(str_input)
   
# int_btn = Button(top, text ="Insert Integer", command = show_int)
# int_btn.place(x=20,y=50)

# string_btn = Button(top, text="Insert String", command=show_str)
# string_btn.place(x=20,y=20)

# top.mainloop()


''' File Dialog Module '''

# from tkinter.filedialog import askopenfile
# from tkinter import *

# top = Tk()

# top.geometry("100x100")
# def show():
#    filename = askopenfile()
#    print(filename)
   
# B = Button(top, text ="Click", command = show)
# B.place(x=50,y=50)

# top.mainloop()


''' Color Chooser '''
# from tkinter.colorchooser import askcolor
# from tkinter import *

# top = Tk()

# top.geometry("100x100")
# def show():
#    color = askcolor()
#    print(color)
   
# B = Button(top, text ="Click", command = show)
# B.place(x=50,y=50)

# top.mainloop()


''' Combobox Widget '''

# from tkinter import *
# from tkinter import ttk

# top = Tk()
# top.geometry("200x150")

# frame = Frame(top)
# frame.pack()

# langs = ["C", "C++", "Java",
#    "Python", "PHP"]
   
# Combo = ttk.Combobox(frame, values = langs)
# Combo.set("Pick an Option")
# Combo.pack(padx = 5, pady = 5)
# top.mainloop()


''' Progressbar '''

# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# frame= ttk.Frame(root)
# def increment():
#    progressBar.step(20)
   
# def decrement():
#    progressBar.step(-20)
   
# def display():
#    print(progressBar["value"])

# progressBar= ttk.Progressbar(frame, mode='determinate')
# progressBar.pack(padx = 10, pady = 10)

# button= ttk.Button(frame, text= "Increase", command= increment)
# button.pack(padx = 10, pady = 10, side = tk.LEFT)

# button= ttk.Button(frame, text= "Decrease", command= decrement)
# button.pack(padx = 10, pady = 10, side = tk.LEFT)
# button= ttk.Button(frame, text= "Display", command= display)
# button.pack(padx = 10, pady = 10, side = tk.LEFT)

# frame.pack(padx = 5, pady = 5)
# root.mainloop()


''' Notebook '''

# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# nb = ttk.Notebook(root)

# # Frame 1 and 2
# frame1 = ttk.Frame(nb)
# frame2 = ttk.Frame(nb)

# label1 = ttk.Label(frame1, text = "This is Window One")
# label1.pack(pady = 50, padx = 20)
# label2 = ttk.Label(frame2, text = "This is Window Two")
# label2.pack(pady = 50, padx = 20)

# frame1.pack(fill= tk.BOTH, expand=True)
# frame2.pack(fill= tk.BOTH, expand=True)
# nb.add(frame1, text = "Window 1")
# nb.add(frame2, text = "Window 2")

# frame3 = ttk.Frame(nb)
# label3 = ttk.Label(frame3, text = "This is Window Three")
# label3.pack(pady = 50, padx = 20)
# frame3.pack(fill= tk.BOTH, expand=True)
# nb.insert("end", frame3, text = "Window 3")
# nb.pack(padx = 5, pady = 5, expand = True)

# root.mainloop()


''' Treeview '''

# import tkinter as tk
# import tkinter.ttk as ttk
# from tkinter import simpledialog

# root = tk.Tk()
# data = [
#    ["Bobby",26,20000],
#    ["Harrish",31,23000],
#    ["Jaya",18,19000],
#    ["Mark",22, 20500],
# ]
# index=0
# def read_data():
#    for index, line in enumerate(data):
#       tree.insert('', tk.END, iid = index,
#          text = line[0], values = line[1:])
# columns = ("age", "salary")

# tree= ttk.Treeview(root, columns=columns ,height = 20)
# tree.pack(padx = 5, pady = 5)

# tree.heading('#0', text='Name')
# tree.heading('age', text='Age')
# tree.heading('salary', text='Salary')

# read_data()
# root.mainloop()


''' Sizegrip '''

# import tkinter as tk
# import tkinter.ttk as ttk

# root = tk.Tk()
# root.geometry("100x100")

# frame = ttk.Frame(root)
# label = ttk.Label(root, text = "Hello World")
# label.pack(padx = 5, pady = 5)
# sizegrip = ttk.Sizegrip(frame)
# sizegrip.pack(expand = True, fill = tk.BOTH, anchor = tk.SE)
# frame.pack(padx = 10, pady = 10, expand = True, fill = tk.BOTH)

# root.mainloop()


''' Separator '''

import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry("200x150")

frame = ttk.Frame(root)

label = ttk.Label(frame, text = "Hello World")
label.pack(padx = 5)

separator = ttk.Separator(frame,orient= tk.HORIZONTAL)
separator.pack(expand = True, fill = tk.X)

label = ttk.Label(frame, text = "Welcome To TutorialsPoint")
label.pack(padx = 5)

frame.pack(padx = 10, pady = 50, expand = True, fill = tk.BOTH)

root.mainloop()