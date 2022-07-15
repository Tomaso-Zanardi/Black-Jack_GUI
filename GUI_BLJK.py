# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 14:25:18 2022

@author: Utente
"""
import time
import tkinter
from tkinter import *
import random
from PIL import Image, ImageTk
# import Black_Jack.O
root = Tk()

root.title("blackjack")
# root.iconbitmap('C:\Users\Utente\Desktop\PYTHON-SPYDER\BJ\card-gifs')
root.geometry("900x500")
root.configure(background="green")

playerPoints=0
dealerPoints=0
playerHand=[]
dealerHand=[]
def shuffle():
    suits = ['♠', '♥', '♦', '♣']
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
    global deck
    deck = []
    
    for suit in suits:
        for card in cards:
            deck.append ([suit, card, cards_values[card]])
    global playerHand, dealerHand, playerHandString, dealerHandString
    
    playerHandString = []
    playerHand = []
    dealerHandString = []
    dealerHand = []
    random.shuffle(deck)
    dealButton['state'] = 'normal'
    shuffleButton['state'] = 'disabled'
    return deck, playerHand, dealerHand, playerHandString, dealerHandString


##############################################################################
def pointIncrement(partecipant_cards):
    """
    This function is used to calculate the value of the hand of one of the players


    Parameters
    ----------
    partecipant_cards : it is a list of lists, where the formers are individual cards.

    Returns
    -------
    partecipantTotalPoints : integer
        it is the total points corresponding to the sum of all the cards individual values

    """
    partecipantTotalPoints = 0
    pp = 0

    # these loops increment the values of players' hands

    for tk in partecipant_cards:
        partecipantTotalPoints = partecipantTotalPoints + (partecipant_cards[pp])[2]
        pp = pp + 1
        
    return partecipantTotalPoints
##############################################################################



def firstdeal():

    global dealerI1,playerI1,PI1,DI1,dealerI2,playerI2,PI2,DI2, playerPoints,dealerPoints
    
    playerHand.append(deck.pop())
    playerHandString.append(str(playerHand[-1]))
    playerI1 = f'card-gifs\{playerHandString[0]}.png'
    PI1 = Image.open(playerI1)
    PI1 = ImageTk.PhotoImage(PI1)
    dealerHand.append(deck.pop())
    dealerHandString.append(str(dealerHand[-1]))
    dealerI1 = f'card-gifs\{dealerHandString[0]}.png'
    DI1 = Image.open(dealerI1)
    DI1 = ImageTk.PhotoImage(DI1)
        
    dealerLabel1.config(image = DI1)
    playerLabel1.config(image = PI1)

 
    playerHand.append(deck.pop())
    playerPoints = pointIncrement(playerHand)
    playerHandString.append(str(playerHand[-1]))
    playerI2 = f'card-gifs\{playerHandString[1]}.png'
    PI2 = Image.open(playerI2)
    PI2 = ImageTk.PhotoImage(PI2)
    dealerHand.append(deck.pop())
    dealerPoints = pointIncrement(dealerHand)
    dealerHandString.append(str(dealerHand[-1]))
    dealerI2 = f'card-gifs\ZB.png'
    DI2 = Image.open(dealerI2)
    DI2 = ImageTk.PhotoImage(DI2)
    dealerLabel2.config(image = DI2)
    playerLabel2.config(image = PI2)
    
    dealButton['state'] = 'disabled'
    hitButton['state'] = 'normal'
    stayButton['state'] = 'normal'
    return playerHand, dealerHand, playerPoints, dealerPoints



def stay():
    global dealerI3, DI3
    dealerI3 = f'card-gifs\{dealerHandString[-1]}.png'
    DI3 = Image.open(dealerI3)
    DI3 = ImageTk.PhotoImage(DI3)
    dealerLabel2.config(image = DI3)




##############################################################################
########THIS HORROR IS THE FUNCTION EXECUTED ON CLICK ON THE HIT BUTTON#######
##############################################################################

def hit():
    global dealerI3, DI3,playerI3,PI3,playerI4,PI4,playerI5,PI5,playerI6,PI6,playerI7,PI7,playerI8,PI8,playerI9,PI9,playerI10,PI10, playerPoints
    playerHand.append(deck.pop())

    
    playerHandString.append(str(playerHand[-1]))
    
    if len(playerHand) == 3:
        playerI3 = f'card-gifs\{playerHandString[-1]}.png'
        PI3 = Image.open(playerI3)
        PI3 = ImageTk.PhotoImage(PI3)        
        playerLabel3.config(image = PI3) 
        playerPoints = pointIncrement(playerHand)

        
        if playerPoints == 21:
            print("Black Jack!")
            hitButton['state'] = 'disabled'
            stayButton['state'] = 'disabled'
            return
    
        if playerPoints > 21:
            print("Dealer Wins!")
            hitButton['state'] = 'disabled'
            stayButton['state'] = 'disabled'
            return
    if len(playerHand) == 4:
        playerI4 = f'card-gifs\{playerHandString[-1]}.png'
        PI4 = Image.open(playerI4)
        PI4 = ImageTk.PhotoImage(PI4)        
        playerLabel4.config(image = PI4)
        playerPoints = pointIncrement(playerHand)

        if playerPoints == 21:
            print("Black Jack!")
            hitButton['state'] = 'disabled'
            stayButton['state'] = 'disabled'
            return
    
        if playerPoints > 21:
            print("Dealer Wins!")
            hitButton['state'] = 'disabled'
            stayButton['state'] = 'disabled'
            return
    if len(playerHand) == 5:
        playerI5 = f'card-gifs\{playerHandString[-1]}.png'
        PI5 = Image.open(playerI5)
        PI5 = ImageTk.PhotoImage(PI5)        
        playerLabel5.config(image = PI5)
        playerPoints = pointIncrement(playerHand)
        if playerPoints == 21:
            print("Black Jack!")
            hitButton['state'] = 'disabled'
            stayButton['state'] = 'disabled'
            return
    
        if playerPoints > 21:
            print("Dealer Wins!")
            hitButton['state'] = 'disabled'
            stayButton['state'] = 'disabled'
            return
    if len(playerHand) == 6:
        playerI6 = f'card-gifs\{playerHandString[-1]}.png'
        PI6 = Image.open(playerI6)
        PI6 = ImageTk.PhotoImage(PI6)        
        playerLabel6.config(image = PI6)
        playerPoints = pointIncrement(playerHand)
        if playerPoints == 21:
            print("Black Jack!")
            hitButton['state'] = 'disabled'
            stayButton['state'] = 'disabled'
            return
    
        if playerPoints > 21:
            print("Dealer Wins!")
            hitButton['state'] = 'disabled'
            stayButton['state'] = 'disabled'
            return
    if len(playerHand) == 7:
        playerI7 = f'card-gifs\{playerHandString[-1]}.png'
        PI7 = Image.open(playerI7)
        PI7 = ImageTk.PhotoImage(PI7)        
        playerLabel7.config(image = PI7)
        playerPoints = pointIncrement(playerHand)
        if playerPoints == 21:
            print("Black Jack!")
            hitButton['state'] = 'disabled'
            stayButton['state'] = 'disabled'
            return
    
        if playerPoints > 21:
            print("Dealer Wins!")
            hitButton['state'] = 'disabled'
            stayButton['state'] = 'disabled'
            return
        
    if len(playerHand) == 8:
        playerI8 = f'card-gifs\{playerHandString[-1]}.png'
        PI8 = Image.open(playerI8)
        PI8 = ImageTk.PhotoImage(PI8)        
        playerLabel8.config(image = PI8)
        playerPoints = pointIncrement(playerHand)
        if playerPoints == 21:
            print("Black Jack!")
            hitButton['state'] = 'disabled'
            stayButton['state'] = 'disabled'
            return
    
        if playerPoints > 21:
            print("Dealer Wins!")
            hitButton['state'] = 'disabled'
            stayButton['state'] = 'disabled'
            return
    if len(playerHand) == 9:
        playerI9 = f'card-gifs\{playerHandString[-1]}.png'
        PI9 = Image.open(playerI9)
        PI9 = ImageTk.PhotoImage(PI9)        
        playerLabel9.config(image = PI9)
        playerPoints = pointIncrement(playerHand)
        if playerPoints == 21:
            print("Black Jack!")
            hitButton['state'] = 'disabled'
            stayButton['state'] = 'disabled'
            return
    
        if playerPoints > 21:
            print("Dealer Wins!")
            hitButton['state'] = 'disabled'
            stayButton['state'] = 'disabled'
            return
        

    return playerHand, playerPoints

##############################################################################
##############################################################################


def newGame():
    
    global dealerFrame
    global playerFrame

    # # embedded frame to hold the card images
    dealerFrame.destroy()
    dealerFrame = LabelFrame(pFrame, text="Dealer", bd=0, bg="green", font=("Times"))
    dealerFrame.grid(row=0, column=0, padx=5, ipadx=1)
    # dealerFrame.grid(row=0, column=1, sticky='ew', rowspan=2)

    # # embedded frame to hold the card images
    playerFrame.destroy()
    playerFrame = LabelFrame(pFrame, text="Player", bd=0,bg="green", font=("Times"))
    playerFrame.grid(row=5, column=0, padx=5, ipadx=1, pady=20)
    # playerFrame.grid(row=2, column=1, sticky='ew', rowspan=2)

    # result_text.set("")

    shuffle()
    firstdeal()
    
    
# Here we just set the frames for the tkinter mainloop....boring front end stuff



# def play():
#     initial_deal()
#     mainWindow.mainloop()


# mainWindow = tkinter.Tk()



pFrame = Frame(root, bg="green")
pFrame.pack(pady=20)

##############################################################################
dealerPointVar = IntVar()
dealerPointVar.set(dealerPoints)

##############################################################################
dealerFrame = LabelFrame(pFrame, text="Dealer", bd=0, bg="green", font=("Times"))
dealerFrame.grid(row=0, column=0, padx=5, ipadx=1)

dealerpointframe = Label(pFrame, textvariable=dealerPointVar, bd=0, bg="green", font=("Times"))
dealerpointframe.grid(row=0, column=1, padx=5, ipadx=1)
##############################################################################

playerPointVar = IntVar(playerPoints)
playerPointVar.set(pointIncrement(playerHand))
##############################################################################
playerFrame = LabelFrame(pFrame, text="Player", bd=0,bg="green", font=("Times"))
playerFrame.grid(row=5, column=0, padx=5, ipadx=1, pady=20)

playerpointframe = Label(pFrame, textvariable=playerPointVar, bd=0, bg="green", font=("Times"))
playerpointframe.grid(row=5, column=1, padx=5, ipadx=1)



playerPointLabel1 = Label(playerpointframe,bg="green", text='')
playerPointLabel1.grid(row=0, column=1, padx=20, pady=20)

dealerPointLabel1 = Label(dealerpointframe,bg="green", text='')
dealerPointLabel1.grid(row=0, column=1, padx=20, pady=20)


# Message frame
message_frame = Frame(root, bg="white")
message_frame.pack(padx=20,pady=20)

message = Text(message_frame)
# message.insert(INSERT, text = "yoooooooo")
# This are the tkinter objects to store cards for the dealer

dealerLabel1 = Label(dealerFrame,bg="green", text='')
dealerLabel1.grid(row=0, column=1, padx=20, pady=20)

dealerLabel2 = Label(dealerFrame,bg="green", text='')
dealerLabel2.grid(row=0, column=2, padx=20, pady=20)

dealerLabel3 = Label(dealerFrame,bg="green", text='')
dealerLabel3.grid(row=0, column=3, padx=20, pady=20)

dealerLabel4 = Label(dealerFrame,bg="green", text='')
dealerLabel4.grid(row=0, column=4, padx=20, pady=20)

dealerLabel5 = Label(dealerFrame,bg="green", text='')
dealerLabel5.grid(row=0, column=5, padx=20, pady=20)

dealerLabel6 = Label(dealerFrame,bg="green", text='')
dealerLabel6.grid(row=0, column=6, padx=20, pady=20)

dealerLabel7 = Label(dealerFrame,bg="green", text='')
dealerLabel7.grid(row=0, column=7, padx=20, pady=20)

dealerLabel8 = Label(dealerFrame,bg="green", text='')
dealerLabel8.grid(row=0, column=8, padx=20, pady=20)

dealerLabel9 = Label(dealerFrame,bg="green", text='')
dealerLabel9.grid(row=0, column=5, padx=20, pady=20)


# This are the tkinter objects to store cards for the dealer

playerLabel1 = Label(playerFrame,bg="green", text='')
playerLabel1.grid(row=0, column=0, padx=20, pady=20)

playerLabel2 = Label(playerFrame,bg="green", text='')
playerLabel2.grid(row=0, column=1, padx=20, pady=20)

playerLabel3 = Label(playerFrame,bg="green", text='')
playerLabel3.grid(row=0, column=2, padx=20, pady=20)

playerLabel4 = Label(playerFrame,bg="green", text='')
playerLabel4.grid(row=0, column=3, padx=20, pady=20)

playerLabel5 = Label(playerFrame,bg="green", text='')
playerLabel5.grid(row=0, column=4, padx=20, pady=20)

playerLabel6 = Label(playerFrame,bg="green", text='')
playerLabel6.grid(row=0, column=5, padx=20, pady=20)

playerLabel7 = Label(playerFrame,bg="green", text='')
playerLabel7.grid(row=0, column=6, padx=20, pady=20)

playerLabel8 = Label(playerFrame,bg="green", text='')
playerLabel8.grid(row=0, column=7, padx=20, pady=20)

playerLabel9 = Label(playerFrame,bg="green", text='')
playerLabel9.grid(row=0, column=8, padx=20, pady=20)

#Button frame
button_frame = Frame(root, bg="green")
button_frame.pack(pady=20)

#shuffle button
shuffleButton = Button(button_frame, text="shuffle", command=shuffle)
shuffleButton.grid(row=0, column=0, pady=20)

#deal button
dealButton = Button(button_frame, text="Deal", state='disabled', command=firstdeal)
dealButton.grid(row=0, column=3, padx=20)

#stay button
stayButton = Button(button_frame, text="Stay", state='disabled', command=stay)
stayButton.grid(row=0, column=5, padx=20)

#stay button
hitButton = Button(button_frame, text="Hit me!", state='disabled', command=hit)
hitButton.grid(row=0, column=7, padx=20)

#new game button

newGameButton = Button(button_frame, text= " New Game", state='normal', command=newGame)
newGameButton.grid(row=0, column=9, padx=20)


root.mainloop()