# Masterpiece algo

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Style
from tkinter import font
# import pymysql
import pandas as pd, os, sys, glob, codecs, pickle, time
import cv2
from matplotlib import pyplot as plt
from PIL import ImageTk


# achieved: The method does pick up the thing.
# achieved: How can we stop a recursive method from working in tkinter.
# This is the one we can make and then can this is
# Use threading to have the label constantly update so that it can be  
# canvas move tje label object from left to right.
# Try after on root as well please. Use random timings as well.

class A:

    def __init__(self, root):

        self.root = root
        self.root.geometry("400x900")
        
        self.C = not True
        self.D = not True
        self.FINAL = 10

        self.canvas_1 = Canvas(self.root, bg = "yellow")
        self.canvas_1.place(x = 1, y=1, height = 500)

        self.text_entry_variable = StringVar()
        self.text_entry_variable_2 = StringVar()



        self.label = Label(self.canvas_1, bg = "red", fg = "black", text = "HELLO")
        self.label.place(x = 1, y = 1)
        
        self.text_entry_ENTRY = Entry(self.canvas_1, bg = "blue", textvariable = self.text_entry_variable)
        self.text_entry_ENTRY.place(x = 1, y = 43)



        self.label_2 = Label(self.canvas_1, bg = "red", fg = "black", text = "HELLO")
        self.label_2.place(x = 200, y = 1)
        
        self.text_entry_ENTRY_2 = Entry(self.canvas_1, bg = "blue", textvariable = self.text_entry_variable_2)
        self.text_entry_ENTRY_2.place(x = 200, y = 43)





        self.button_1 = Button(self.canvas_1, text  ="Press me please 1.", command = self.label_method_2)
        self.button_1.place(x = 1, y = 80)

        self.button_2 = Button(self.canvas_1, text  ="Press me please 2.", command = self.label_method_3) #self.label_method_3)
        self.button_2.place(x = 200, y = 80)
        
        self.button_stop_recursive_method = Button(self.root, text = "STOP", command = lambda : self.stopping_recursive_method())
        self.button_stop_recursive_method.place(x = 1, y = 120)

        self.exit_button = Button(self.canvas_1, text = "Exit", command = root.destroy)
        self.exit_button.place(x = 1, y = 150)


        self.print_label_button = Button(self.canvas_1, text = "PRINT LABEL", command = self.print_current_label)
        self.print_label_button.place(x = 1, y = 200)


        self.moving_label = Label(self.canvas_1, text = "I move", bg = "blue")
        self.moving_label.place(x=1, y = 240)

        self.button_mover = Button(self.canvas_1, text = "MOVER", command = self.moving_method_start)
        self.button_mover.place(x= 1, y = 280 )


    def stopping_recursive_method(self):
        self.C = True
        self.D = True
        

    
    def label_method_2(self):
        if self.C == True:
            self.C = False
            return
        self.label.config(text = self.text_entry_variable.get())
        self.label.after(300, self.label_method_2)


    def label_method_3(self):
        if self.D == True:
            self.D = False
            return
        self.label_2.config(text = self.text_entry_variable_2.get())
        self.label_2.after(300, self.label_method_3)

    def print_current_label(self):
        print(self.label.cget("text"))
        print(self.label_2.cget("text"))
    
    def moving_method_start(self):
        if self.FINAL == 300:
            self.button_mover["command"] = self.moving_method_finish
            return
        else:
            self.FINAL += 5;
            self.moving_label.place(x = self.FINAL, y = 240)
            self.moving_label.after(20, self.moving_method_start)

    def moving_method_finish(self):
        if self.FINAL == 10:
            self.button_mover["command"] = self.moving_method_start
            return
        else:
            self.FINAL -= 5;
            self.moving_label.place(x = self.FINAL, y = 240)
            self.moving_label.after(20, self.moving_method_finish)


        

root = Tk()
obj = A(root)
print(obj.C)
root.mainloop()

