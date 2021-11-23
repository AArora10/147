#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 17:15:11 2021

@author: Anisa
"""


from tkinter import * 
from tkmacosx import *

root = Tk()
root.title("Name")
root.geometry("400x400")
root.configure(background = 'blue')

enter_word = Entry(root)
enter_word.place(relx = 0.5, rely = 0.4,  anchor = CENTER)
name = Label(root, text = "name in ascii :", bg = "pink", fg = "black")
label2 = Label(root, text = " encrypted name =  ",bg = "black", fg = "pink")

def ascaiConverter():
    input = str(enter_word.get())
    for letter in input: 
        name["text"] += str(ord(letter))+ " "
        ascii = int(ord(letter))
        encrypted = ascii - 1
        label2["text"] + str(chr(encrypted))
        
        
        
btn = Button(root, text = "SHOW ENCRYPTED NAME", command = ascaiConverter, bg = "pink", fg = "black")
btn.place(relx = 0.5, rely = 0.5,  anchor = CENTER)
name.place(relx = 0.5, rely = 0.6, anchor = CENTER)
label2.place(relx = 0.5, rely = 0.7, anchor = CENTER)

root.mainloop()