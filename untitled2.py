# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 14:57:27 2022

@author: Utente
"""


import tkinter
from tkinter import *


root = Tk()

root.title("blackjack")
root.iconbitmap('C:\Users\Utente\Desktop\PYTHON-SPYDER\BJ\card-gifs')
root.geometry("900x500")
root.configure(background="green")


pFrame = Frame(root, bg="green")
pFrame.pack(pady=20)

dealerFrame = LabelFrame(pFrame, text="Dealer", bd=0)
dealerFrame.grid(row=0, column=0, padx=20, ipadx=20)

playerFrame = LabelFrame(pFrame, text="Player", bd=0)
playerFrame.grid(row=0, column=1, padx=20,)


dealerLabel = Label(dealerFrame, text='')
dealerLabel = pack(pady=20)


playerLabel = Label(dealerFrame, text='')
playerLabel = pack(pady=20)


shuffleButton = Button(root, text="shuffle")
dealButton = Button(root, text="deal")