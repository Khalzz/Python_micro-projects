"""
I divide my code by 3 diferent methods
//////////Section divider////////////
-----(object or logic divider)-------
-------------------------------------
the last one its just the end of the "object or logic"
"""

from colorama import Fore
import os
import random
import time

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#-----------------------------------------------------------(object card 1)-----------------------------------------------------------
class PlayerCard1:
    cardNumber = int(random.randint(1,10))  #number of card  

    # type of 10 
    tenKind = int(random.randint(1,4))  #type of card (normal,j,queen and king)
    if cardNumber == 10 and tenKind == 1:
        tenKind = 10
    elif cardNumber == 10 and tenKind == 2:
        tenKind = "J"
    elif cardNumber == 10 and tenKind == 3:
        tenKind = "Queen"
    elif cardNumber == 10 and tenKind == 4:
        tenKind = "King"

    if cardNumber == 1:
        tenkind = "Ace"

    # figure of the card
    typeCard = int(random.randint(1,4))  #heart, diamond, clover and spades 
    if typeCard == 1:
        typeCard = "hearts"
    elif typeCard == 2:
        typeCard = "diamonds"
    elif typeCard == 3:
        typeCard = "clovers"
    elif typeCard == 4:
        typeCard = "spades"

    if cardNumber == 10:
        card = (str(tenKind) + " of " + typeCard)
    else:
        card = (str(cardNumber) + " of " + typeCard)
#-------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------(object card 2)-----------------------------------------------------------
class PlayerCard2:
    cardNumber = int(random.randint(1,10))  #number of card  

    # type of 10 
    tenKind = int(random.randint(1,4))  #type of card (normal,j,queen and king)
    if cardNumber == 10 and tenKind == 1:
        tenKind = "10"
    elif cardNumber == 10 and tenKind == 2:
        tenKind = "J"
    elif cardNumber == 10 and tenKind == 3:
        tenKind = "Queen"
    elif cardNumber == 10 and tenKind == 4:
        tenKind = "King"
    
    if cardNumber == 1:
        tenkind = "Ace"

    # figure of the card
    typeCard = int(random.randint(1,4))  #heart, diamond, clover and spades 
    if typeCard == 1:
        typeCard = "hearts"
    elif typeCard == 2:
        typeCard = "diamonds"
    elif typeCard == 3:
        typeCard = "clovers"
    elif typeCard == 4:
        typeCard = "spades"

    if cardNumber == 10:
        card = (str(tenKind) + " of " + typeCard)
    else:
        card = (str(cardNumber) + " of " + typeCard)
#-------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------(object card 3)-----------------------------------------------------------
class PlayerCard3:
    cardNumber = int(random.randint(1,10))  #number of card  

    # type of 10 
    tenKind = int(random.randint(1,4))  #type of card (normal,j,queen and king)
    if cardNumber == 10 and tenKind == 1:
        tenKind = 10
    elif cardNumber == 10 and tenKind == 2:
        tenKind = "J"
    elif cardNumber == 10 and tenKind == 3:
        tenKind = "Queen"
    elif cardNumber == 10 and tenKind == 4:
        tenKind = "King"

    if cardNumber == 1:
        tenkind = "Ace"

    # figure of the card
    typeCard = int(random.randint(1,4))  #heart, diamond, clover and spades 
    if typeCard == 1:
        typeCard = "hearts"
    elif typeCard == 2:
        typeCard = "diamonds"
    elif typeCard == 3:
        typeCard = "clovers"
    elif typeCard == 4:
        typeCard = "spades"

    if cardNumber == 10:
        card = (str(tenKind) + " of " + typeCard)
    else:
        card = (str(cardNumber) + " of " + typeCard)
#-------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------(object card 4)-----------------------------------------------------------
class PlayerCard4:
    cardNumber = int(random.randint(1,10))  #number of card  

    # type of 10 
    tenKind = int(random.randint(1,4))  #type of card (normal,j,queen and king)
    if cardNumber == 10 and tenKind == 1:
        tenKind = "10"
    elif cardNumber == 10 and tenKind == 2:
        tenKind = "J"
    elif cardNumber == 10 and tenKind == 3:
        tenKind = "Queen"
    elif cardNumber == 10 and tenKind == 4:
        tenKind = "King"
    
    if cardNumber == 1:
        tenkind = "Ace"

    # figure of the card
    typeCard = int(random.randint(1,4))  #heart, diamond, clover and spades 
    if typeCard == 1:
        typeCard = "hearts"
    elif typeCard == 2:
        typeCard = "diamonds"
    elif typeCard == 3:
        typeCard = "clovers"
    elif typeCard == 4:
        typeCard = "spades"

    if cardNumber == 10:
        card = (str(tenKind) + " of " + typeCard)
    else:
        card = (str(cardNumber) + " of " + typeCard)
#-------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------(object card 5)-----------------------------------------------------------
class PlayerPrivCard:
    cardNumber = int(random.randint(1,10))  #number of card  

    # type of 10 
    tenKind = int(random.randint(1,4))  #type of card (normal,j,queen and king)
    if cardNumber == 10 and tenKind == 1:
        tenKind = 10
    elif cardNumber == 10 and tenKind == 2:
        tenKind = "J"
    elif cardNumber == 10 and tenKind == 3:
        tenKind = "Queen"
    elif cardNumber == 10 and tenKind == 4:
        tenKind = "King"

    if cardNumber == 1:
        tenkind = "Ace"

    # figure of the card
    typeCard = int(random.randint(1,4))  #heart, diamond, clover and spades 
    if typeCard == 1:
        typeCard = "hearts"
    elif typeCard == 2:
        typeCard = "diamonds"
    elif typeCard == 3:
        typeCard = "clovers"
    elif typeCard == 4:
        typeCard = "spades"

    if cardNumber == 10:
        card = (str(tenKind) + " of " + typeCard)
    else:
        card = (str(cardNumber) + " of " + typeCard)
#-------------------------------------------------------------------------------------------------------------------------------------

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#----------------------------------------------------(object dealer card 1)-----------------------------------------------------------
class DealerCard1:
    cardNumber = int(random.randint(1,10))  #number of card  

    # type of 10 
    tenKind = int(random.randint(1,4))  #type of card (normal,j,queen and king)
    if cardNumber == 10 and tenKind == 1:
        tenKind = "10"
    elif cardNumber == 10 and tenKind == 2:
        tenKind = "J"
    elif cardNumber == 10 and tenKind == 3:
        tenKind = "Queen"
    elif cardNumber == 10 and tenKind == 4:
        tenKind = "King"
    
    if cardNumber == 1:
        tenkind = "Ace"

    # figure of the card
    typeCard = int(random.randint(1,4))  #heart, diamond, clover and spades 
    if typeCard == 1:
        typeCard = "hearts"
    elif typeCard == 2:
        typeCard = "diamonds"
    elif typeCard == 3:
        typeCard = "clovers"
    elif typeCard == 4:
        typeCard = "spades"

    if cardNumber == 10:
        card = (str(tenKind) + " of " + typeCard)
    else:
        card = (str(cardNumber) + " of " + typeCard)
#-------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------(object dealer card 2)-----------------------------------------------------------
class DealerCard2:
    cardNumber = int(random.randint(1,10))  #number of card  

    # type of 10 
    tenKind = int(random.randint(1,4))  #type of card (normal,j,queen and king)
    if cardNumber == 10 and tenKind == 1:
        tenKind = "10"
    elif cardNumber == 10 and tenKind == 2:
        tenKind = "J"
    elif cardNumber == 10 and tenKind == 3:
        tenKind = "Queen"
    elif cardNumber == 10 and tenKind == 4:
        tenKind = "King"
    
    if cardNumber == 1:
        tenkind = "Ace"

    # figure of the card
    typeCard = int(random.randint(1,4))  #heart, diamond, clover and spades 
    if typeCard == 1:
        typeCard = "hearts"
    elif typeCard == 2:
        typeCard = "diamonds"
    elif typeCard == 3:
        typeCard = "clovers"
    elif typeCard == 4:
        typeCard = "spades"

    if cardNumber == 10:
        card = (str(tenKind) + " of " + typeCard)
    else:
        card = (str(cardNumber) + " of " + typeCard)
#-------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------(object dealer card 3)-----------------------------------------------------------
class DealerCard3:
    cardNumber = int(random.randint(1,10))  #number of card  

    # type of 10 
    tenKind = int(random.randint(1,4))  #type of card (normal,j,queen and king)
    if cardNumber == 10 and tenKind == 1:
        tenKind = 10
    elif cardNumber == 10 and tenKind == 2:
        tenKind = "J"
    elif cardNumber == 10 and tenKind == 3:
        tenKind = "Queen"
    elif cardNumber == 10 and tenKind == 4:
        tenKind = "King"

    if cardNumber == 1:
        tenkind = "Ace"

    # figure of the card
    typeCard = int(random.randint(1,4))  #heart, diamond, clover and spades 
    if typeCard == 1:
        typeCard = "hearts"
    elif typeCard == 2:
        typeCard = "diamonds"
    elif typeCard == 3:
        typeCard = "clovers"
    elif typeCard == 4:
        typeCard = "spades"

    if cardNumber == 10:
        card = (str(tenKind) + " of " + typeCard)
    else:
        card = (str(cardNumber) + " of " + typeCard)
#-------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------(object dealer card 4)-----------------------------------------------------------
class DealerCard4:
    cardNumber = int(random.randint(1,10))  #number of card  

    # type of 10 
    tenKind = int(random.randint(1,4))  #type of card (normal,j,queen and king)
    if cardNumber == 10 and tenKind == 1:
        tenKind = "10"
    elif cardNumber == 10 and tenKind == 2:
        tenKind = "J"
    elif cardNumber == 10 and tenKind == 3:
        tenKind = "Queen"
    elif cardNumber == 10 and tenKind == 4:
        tenKind = "King"
    
    if cardNumber == 1:
        tenkind = "Ace"

    # figure of the card
    typeCard = int(random.randint(1,4))  #heart, diamond, clover and spades 
    if typeCard == 1:
        typeCard = "hearts"
    elif typeCard == 2:
        typeCard = "diamonds"
    elif typeCard == 3:
        typeCard = "clovers"
    elif typeCard == 4:
        typeCard = "spades"

    if cardNumber == 10:
        card = (str(tenKind) + " of " + typeCard)
    else:
        card = (str(cardNumber) + " of " + typeCard)
#-------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------(object dealer card 5)-----------------------------------------------------------
class DealerPrivCard:
    cardNumber = int(random.randint(1,10))  #number of card  

    # type of 10 
    tenKind = int(random.randint(1,4))  #type of card (normal,j,queen and king)
    if cardNumber == 10 and tenKind == 1:
        tenKind = 10
    elif cardNumber == 10 and tenKind == 2:
        tenKind = "J"
    elif cardNumber == 10 and tenKind == 3:
        tenKind = "Queen"
    elif cardNumber == 10 and tenKind == 4:
        tenKind = "King"

    if cardNumber == 1:
        tenkind = "Ace"

    # figure of the card
    typeCard = int(random.randint(1,4))  #heart, diamond, clover and spades 
    if typeCard == 1:
        typeCard = "hearts"
    elif typeCard == 2:
        typeCard = "diamonds"
    elif typeCard == 3:
        typeCard = "clovers"
    elif typeCard == 4:
        typeCard = "spades"

    if cardNumber == 10:
        card = (str(tenKind) + " of " + typeCard)
    else:
        card = (str(cardNumber) + " of " + typeCard)
#-------------------------------------------------------------------------------------------------------------------------------------

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#--------------------------------------------------------(function delete terminal)---------------------------------------------------
def deleteConsole():
    if os.name == "posix":
        os.system ("clear")
    elif os.name =="nt" or os.name == "ce" or os.name == "dos":
        os.system ("cls")
#-------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------(function main menu)------------------------------------------------------
def mainMenu():
    deleteConsole()
    print("Welcome to my Black jack terminal game :3")
    time.sleep(0.5)
    print("<<(1)play>>")
    time.sleep(0.5)
    print("<<(2)instructions>>")
    time.sleep(0.5)
    selectmenu=int(input("select your option: "))

    if selectmenu==1:
        deleteConsole()
        play()
    elif selectmenu==2:
        deleteConsole()
        rules0()
    else:
        deleteConsole()
        print("this option is not valid")
        mainMenu()
#-------------------------------------------------------------------------------------------------------------------------------------            

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#-----------------------------------------------------------(function rules 3)--------------------------------------------------------
def rules2():
    deleteConsole()
    print("if your hand is higher than your opponent")
    print(Fore.CYAN + "you win" + Fore.RESET)
    print("if your hand its lower than your opponent or greater than 21")
    print(Fore.RED + "you lose" + Fore.RESET)
    print("another tip: the card as equals to 1 but if you have a 10 this card equals to 11")
    print("<<(1) back >>--------------------------------------------<<(2) main menu >>")
    opcion=int(input("select your option:"))
    if opcion==1:
        deleteConsole()
        rules1()
    elif opcion==2:
        deleteConsole()
        mainMenu()
    else:
        deleteConsole()
        print("this option is not valid")
        time.sleep(0.8)
        rules2()
#-------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------(function rules 2)--------------------------------------------------------
def rules1():
    deleteConsole()
    print("when you have that two cards you gonna have two options")
    print("---------------------------------------------------------------------------")
    time.sleep(0.5)

    #with "Fore.CYAN" i can change the "print" color and in the end with "Fore.RESET" i come back the color to other "prints"
    print(Fore.CYAN + "<<(1) play>>\n<<(2) get one more card>>" + Fore.RESET)

    time.sleep(0.5)
    print("---------------------------------------------------------------------------")
    print("the first option turns upside your card and play ")
    print("the second one gives you another card by frontside and add it to your hand")
    print("<<(1) back >>-------------------------------------------------<<(2) next >>")
    opcion=int(input("select your option:"))
    if opcion==1:
        deleteConsole()
        rules0()
    elif opcion==2:
        deleteConsole()
        rules2()
    else:
        deleteConsole()
        print("this option is not valid")
        time.sleep(0.8)
        rules1()
#-------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------(funcion rules 1)---------------------------------------------------------
def rules0():
    deleteConsole()
    print("this game its fully aleatory, you can´t select a level")
    print("this game have 1 principal rules")
    print("---------------------------------------------------------------------------")
    time.sleep(0.5)

    #with "Fore.CYAN" i can change the "print" color and in the end with "Fore.RESET" i come back the color to other "prints"
    print(Fore.CYAN +"1) the player with the highest card wins\n2) if you have more than 21 you lose" + Fore.RESET)

    time.sleep(0.5)
    print("---------------------------------------------------------------------------")
    print("when the the game starts you gonna have 2 cards")
    print("a card by frontside and a card by backside")
    print("---------------------------------------------------------------<<(1) next>>")
    opcion=int(input("select your option:"))
    if opcion==1:
        deleteConsole()
        rules1()
    else:
        deleteConsole()
        print("this option is not valid")
        time.sleep(0.8)
        rules0()
#-------------------------------------------------------------------------------------------------------------------------------------

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#-----------------------------------------------------------(function play 2 cards)---------------------------------------------------
def play():
    deleteConsole()
    time.sleep(0.5)
    print("the cards are being dealt")
    time.sleep(0.5)
    print("your cards are:")
    time.sleep(0.3)
    print(PlayerCard1.card)
    time.sleep(0.3)
    print("and a unknown card")
    print("---------------------------------------------------------------------------")
    print(Fore.CYAN + "<<(1) play>>\n<<(2) get one more card>>")
    opcion = int(input("what do you want to do:"))
    if opcion == 1:
        deleteConsole()
        time.sleep(0.5)
        print("your cards are: " + PlayerCard1.card + " and " + PlayerPrivCard.card)
        time.sleep(0.5)
        logic1()
    elif opcion == 2:
        play2()
    else:
        play()
#-------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------(logic play 2 cards)------------------------------------------------------
def logic1():

    cardsPlayer = int(PlayerCard1.cardNumber + PlayerPrivCard.cardNumber)
    cardsDealer = int(DealerCard1.cardNumber + DealerPrivCard.cardNumber)
    print("the dealer cards are:")
    print(DealerCard1.card)
    time.sleep(0.5)
    print(DealerCard2.card)
    time.sleep(0.5)
    print(DealerPrivCard.card)
    time.sleep(0.5)

    if PlayerCard1.cardNumber == 10 and PlayerPrivCard.cardNumber == 1:
        cardsPlayer = 21
    elif PlayerCard1.cardNumber == 1 and PlayerPrivCard.cardNumber == 10:
        cardsPlayer = 21
    if cardsPlayer > cardsDealer and cardsPlayer <= 21 :
        YouWin()
        #you win

    elif cardsPlayer < cardsDealer and cardsPlayer <= 21 :
        YouWin()
        #you win

    elif cardsPlayer == 21 and cardsDealer < 21:
        YouWin()
        #you win

    elif cardsPlayer == 21 and cardsDealer > 21:
        YouWin()
        #you win

    elif cardsPlayer > cardsDealer and cardsPlayer > 21:
        YouLoose()
        #you loose

    elif cardsPlayer < cardsDealer and cardsPlayer < 21:
        YouLoose()
        #you loose
    
    if DealerCard1.cardNumber == 10 and DealerPrivCard.cardNumber == 1:
        cardsDealer = 21
    elif DealerCard1.cardNumber == 1 and DealerPrivCard.cardNumber == 10:
        cardsDealer = 21

    elif cardsPlayer == cardsDealer:
        GameDraw()
        #game draw
#-------------------------------------------------------------------------------------------------------------------------------------

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#-----------------------------------------------------------(function play 3 cards)---------------------------------------------------
def play2():
    deleteConsole()
    time.sleep(0.5)
    print("the cards are being dealt")
    time.sleep(0.5)
    print("your cards are:")
    time.sleep(0.3)
    print(PlayerCard1.card)
    time.sleep(0.3)
    print(PlayerCard2.card)
    time.sleep(0.3)
    print("and a unknown card")
    print("---------------------------------------------------------------------------")
    print(Fore.CYAN + "<<(1) play>>\n<<(2) get one more card>>")
    opcion = int(input("what do you want to do:"))
    if opcion == 1:
        deleteConsole()
        print("your cards are:")
        print(PlayerCard1.card)
        time.sleep(0.5)
        print(PlayerCard2.card)
        time.sleep(0.5)
        print(PlayerPrivCard.card)
        time.sleep(0.5)
        logic2()
    elif opcion == 2:
        play3()
    else:
        play2()
#-------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------(logic play 3 cards)------------------------------------------------------
def logic2():

    cardsPlayer = int(PlayerCard1.cardNumber + PlayerCard2.cardNumber + PlayerPrivCard.cardNumber)
    cardsDealer = int(DealerCard1.cardNumber + DealerCard2.cardNumber)
    dealerElection = random.randint(1,2)

    if dealerElection == 1:
        cardsDealer = int(DealerCard1.cardNumber + DealerCard2.cardNumber + DealerPrivCard.cardNumber)
        print("the dealer cards are:")
        print(DealerCard1.card)
        time.sleep(0.5)
        print(DealerCard2.card)
        time.sleep(0.5)
        print(DealerPrivCard.card)
        time.sleep(0.5)
    else:
        cardsDealer = cardsDealer
        print("the dealer cards are:")
        print(DealerCard1.card)
        time.sleep(0.5)
        print(DealerPrivCard.card)
        time.sleep(0.5)
        if DealerCard1.cardNumber == 10 and DealerPrivCard.cardNumber == 1:
            cardsPlayer = 21
        elif DealerCard1.cardNumber == 1 and DealerPrivCard.cardNumber == 10:
            cardsPlayer = 21

    if cardsPlayer > cardsDealer and cardsPlayer <= 21 :
        YouWin()
        #you win

    elif cardsPlayer < cardsDealer and cardsPlayer <= 21 :
        YouWin()
        #you win

    elif cardsPlayer == 21 and cardsDealer < 21:
        YouWin()
        #you win

    elif cardsPlayer == 21 and cardsDealer > 21:
        YouWin()
        #you win

    elif cardsPlayer > cardsDealer and cardsPlayer > 21:
        YouLoose()
        #you loose

    elif cardsPlayer < cardsDealer and cardsPlayer < 21:
        YouLoose()
        #you loose

    elif cardsPlayer == cardsDealer:
        GameDraw()
        #game draw
#-------------------------------------------------------------------------------------------------------------------------------------

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#-----------------------------------------------------------(function play 4 cards)---------------------------------------------------
def play3():
    deleteConsole()
    time.sleep(0.5)
    print("the cards are being dealt")
    time.sleep(0.5)
    print("your cards are:")
    time.sleep(0.3)
    print(PlayerCard1.card)
    time.sleep(0.3)
    print(PlayerCard2.card)
    time.sleep(0.3)
    print(PlayerCard3.card)
    time.sleep(0.3)
    print("and a unknown card")
    print("---------------------------------------------------------------------------")
    print(Fore.CYAN + "<<(1) play>>\n<<(2) get one more card>>")
    opcion = int(input("what do you want to do:"))
    if opcion == 1:
        deleteConsole()
        print("your cards are:")
        print(PlayerCard1.card)
        time.sleep(0.5)
        print(PlayerCard2.card)
        time.sleep(0.5)
        print(PlayerCard3.card)
        time.sleep(0.5)
        print(PlayerPrivCard.card)
        time.sleep(0.5)
        logic3
    elif opcion == 2:
        play4()
    else:
        play3()
#-------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------(logic play 4 cards)------------------------------------------------------
def logic3():
    
    cardsPlayer = int(PlayerCard1.cardNumber + PlayerCard2.cardNumber + PlayerCard3.cardNumber + PlayerPrivCard.cardNumber)
    cardsDealer = int(DealerCard1.cardNumber + DealerCard2.cardNumber + DealerPrivCard.cardNumber)
    dealerElection = random.randint(1,2)

    if dealerElection == 1:
        cardsDealer = int(DealerCard1.cardNumber + DealerCard2.cardNumber + DealerCard3.cardNumber + DealerPrivCard.cardNumber)
        print("the dealer cards are:")
        print(DealerCard1.card)
        time.sleep(0.5)
        print(DealerCard2.card)
        time.sleep(0.5)
        print(DealerCard3.card)
        time.sleep(0.5)
        print(DealerPrivCard.card)
        time.sleep(0.5)
    else:
        cardsDealer = cardsDealer
        print("the dealer cards are:")
        print(DealerCard1.card)
        time.sleep(0.5)
        print(DealerCard2.card)
        time.sleep(0.5)
        print(DealerPrivCard.card)
        time.sleep(0.5)

    if cardsPlayer > cardsDealer and cardsPlayer <= 21 :
        YouWin()
        #you win

    elif cardsPlayer < cardsDealer and cardsPlayer <= 21 :
        YouWin()
        #you win

    elif cardsPlayer == 21 and cardsDealer < 21:
        YouWin()
        #you win

    elif cardsPlayer == 21 and cardsDealer > 21:
        YouWin()
        #you win

    elif cardsPlayer > cardsDealer and cardsPlayer > 21:
        YouLoose()
        #you loose

    elif cardsPlayer < cardsDealer and cardsPlayer < 21:
        YouLoose()
        #you loose

    elif cardsPlayer == cardsDealer:
        GameDraw()
        #game draw
#-------------------------------------------------------------------------------------------------------------------------------------

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#-----------------------------------------------------------(function play 5 cards)---------------------------------------------------
def play4():
    deleteConsole()
    time.sleep(0.5)
    print("the cards are being dealt")
    time.sleep(0.5)
    print("your cards are:")
    time.sleep(0.3)
    print(PlayerCard1.card)
    time.sleep(0.3)
    print(PlayerCard2.card)
    time.sleep(0.3)
    print(PlayerCard3.card)
    time.sleep(0.3)
    print(PlayerCard4.card)
    time.sleep(0.3)
    print("and a unknown card")
    print("---------------------------------------------------------------------------")
    print(Fore.CYAN + "<<(1) play>>")
    opcion = int(input("what do you want to do:"))
    if opcion == 1:
        deleteConsole()
        print("your cards are:")
        print(PlayerCard1.card)
        time.sleep(0.5)
        print(PlayerCard2.card)
        time.sleep(0.5)
        print(PlayerCard3.card)
        time.sleep(0.5)
        print(PlayerCard4.card)
        time.sleep(0.5)
        print(PlayerPrivCard.card)
        time.sleep(0.5)
        logic4()
    else:
        play4()
        print("you cant have more than 5 cards")
#-------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------(logic play 5 cards)------------------------------------------------------
def logic4():
    
    cardsPlayer = int(PlayerCard1.cardNumber + PlayerCard2.cardNumber + PlayerCard3.cardNumber + PlayerCard4.cardNumber + PlayerPrivCard.cardNumber)
    cardsDealer = int(DealerCard1.cardNumber + DealerCard2.cardNumber + DealerCard3.cardNumber + DealerPrivCard.cardNumber)
    dealerElection = random.randint(1,2)

    if dealerElection == 1:
        cardsDealer = int(DealerCard1.cardNumber + DealerCard2.cardNumber + DealerCard3.cardNumber + DealerCard4.cardNumber + DealerPrivCard.cardNumber)
        print("the dealer cards are:")
        print(DealerCard1.card)
        time.sleep(0.5)
        print(DealerCard2.card)
        time.sleep(0.5)
        print(DealerCard3.card)
        time.sleep(0.5)
        print(DealerCard4.card)
        time.sleep(0.5)
        print(DealerPrivCard.card)
        time.sleep(0.5)
    else:
        cardsDealer = cardsDealer
        print("the dealer cards are:")
        print(DealerCard1.card)
        time.sleep(0.5)
        print(DealerCard2.card)
        time.sleep(0.5)
        print(DealerCard3.card)
        time.sleep(0.5)
        print(DealerPrivCard.card)
        time.sleep(0.5)

    if cardsPlayer > cardsDealer and cardsPlayer <= 21:
        YouWin()
        #you win

    elif cardsPlayer < cardsDealer and cardsPlayer <= 21 :
        YouWin()
        #you win

    elif cardsPlayer == 21 and cardsDealer < 21:
        YouWin()
        #you win

    elif cardsPlayer == 21 and cardsDealer > 21:
        YouWin()
        #you win

    elif cardsPlayer > cardsDealer and cardsPlayer > 21:
        YouLoose()
        #you loose

    elif cardsPlayer < cardsDealer and cardsPlayer < 21:
        YouLoose()
        #you loose

    elif cardsPlayer == cardsDealer:
        GameDraw()
        #game draw

#-------------------------------------------------------------------------------------------------------------------------------------

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#-----------------------------------------------------------(logic of end state)------------------------------------------------------

def YouWin():
    print(Fore.GREEN + "YOU WIN 0W0!!!")
    print("congratulations, you are the best")
    print("<<(1) play again>>\n<<(2) go to menu>>\n<<(3) exit>>")
    opcion = int(input("select your option:"))

    if opcion == 1:
        play()
    elif opcion == 2:
        mainMenu()
    elif opcion == 3:
        exit()

def YouLoose():
    print(Fore.RED + "YOU LOOSE :C!!!")
    print("sorry, the next time maybe you win uwu")
    print("<<(1) play again>>\n<<(2) go to menu>>\n<<(3) exit>>")
    opcion = int(input("select your option:"))

    if opcion == 1:
        play()
    elif opcion == 2:
        mainMenu()
    elif opcion == 3:
        exit()

def GameDraw():
    print(Fore.YELLOW + "GAME DRAW :0!!!")
    print("OMG a draw, try again and beat him 0w0")
    print("<<(1) play again>>\n<<(2) go to menu>>\n<<(3) exit>>")
    opcion = int(input("select your option:"))

    if opcion == 1:
        play()
    elif opcion == 2:
        mainMenu()
    elif opcion == 3:
        exit()
#-------------------------------------------------------------------------------------------------------------------------------------

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#-----------------------------------------------------------(the game starts)---------------------------------------------------------
mainMenu()
#-------------------------------------------------------------------------------------------------------------------------------------
