#Chloe Nguyen - Phuong Ha Nguyen
#COM 110 - Project 5 Black Jack
#April 19, 2022
#Black Jack Game 

from BlackJack import *
from buttonClass import *
from dealerBursted import *

def clear(gwin):
#sub-function to clear the window
    for item in gwin.items[:]:
        item.undraw()
    gwin.update()
    
def recursion(gwin, fname, button1, button2):
#sub-function to enable the user to run the program again and again
    
    button1.deactivate() #deactivate Hit and Stand function
    button2.deactivate()

    #draw continue and quit buttons
    buttonCont = Button(gwin, Point(250, 725), 100, 50, "Continue")
    buttonQuit = Button(gwin, Point(550, 725), 100, 50, "Quit")

    buttonCont.activate()
    buttonQuit.activate()

    pt = gwin.getMouse()
    
    while not (buttonCont.isClick(pt) or buttonQuit.isClick(pt)):
        pt = gwin.getMouse()
        
    if buttonQuit.isClick(pt):
        gwin.close()
        return
 
    while buttonCont.isClick(pt):
        gwin.close()
        fname(False) #run the function again 

        return   
    
def drawScore(gwin, xPos, yPos, score):
    #sub-function to draw the player and dealer score 
    scoreText = Text(Point(xPos, yPos), "Total: "+ str(score))
    scoreText.draw(gwin)
    scoreText.setTextColor("white")
    scoreText.setSize(18)
    scoreText.setFace("courier")
    scoreText.setStyle("bold italic")

    return scoreText

def intro(win1):
    #intro function
    intro = Image(Point(400,400), "intro_image.gif")
    intro.draw(win1)
    gameName = Text(Point(200,200), 'Black Jack')
    gameName.setSize(36)
    gameName.setTextColor('firebrick2')
    gameName.setStyle("bold italic")
    gameName.setFace("courier")
    gameName.draw(win1)
    

    Quit = Button(win1, Point(180,500), 100, 50, "Quit")
    rule = Button(win1, Point(180,420), 100, 50, "Rules")
    start = Button(win1, Point(180,340), 100, 50, "Start")

    pt = win1.getMouse()
    while not Quit.isClick(pt):
        if start.isClick(pt):
            clear(win1) #clear the window and exit the loop to start playing
            break
        elif rule.isClick(pt):
            rules(win1) #run the rules function
            
        pt = win1.getMouse()
        
    if Quit.isClick(pt):
        win1.close()
        sys.exit() #exiting the program

def rules(win2):
    #helper function to draw the rules of the game
    win2 = GraphWin('Black Jack Rules', 400, 400)
    Image(Point(100,100),"rulebackground.gif").draw(win2)
    win2.setCoords(0, 0, 200, 200)

    title = Text(Point(100, 175), 'Rules')
    title.setSize(30)
    title.setFace("courier")
    title.setTextColor('yellow1')
    title.setStyle('bold italic')
    title.draw(win2)

    line1 = Text(Point(100, 150), '- All number cards has face value')
    line1.setTextColor('SkyBlue1')
    line1.setSize(12)
    line1.setFace("courier")
    line1.draw(win2)
    line2 = Text(Point(100, 135), '- Jack - Queen - King has the value of 10')
    line2.setTextColor('SkyBlue1')
    line2.setSize(12)
    line2.setFace("courier")
    line2.draw(win2)
    line3 = Text(Point(100, 115), '- An Ace has the value of either 1 or 11,\nwhichever is better for owner of the hand')
    line3.setTextColor('SkyBlue1')
    line3.setSize(12)
    line3.setFace("courier")
    line3.draw(win2)
    line4 = Text(Point(100, 90), "- Try to get 21 or as close to 21 as possible.\nDon't go over 21, otherwise you will be 'BUSTED'")
    line4.setTextColor('SkyBlue1')
    line4.setSize(12)
    line4.setFace("courier")
    line4.draw(win2)
    line5 = Text(Point(100, 70), "- Click 'Hit' to draw one more card")
    line5.setTextColor('SkyBlue1')
    line5.setSize(12)
    line5.setFace("courier")
    line5.draw(win2)
    line6 = Text(Point(100, 40), "- Click 'Stand' to stop drawing card \nand start the dealer play\n\n\nClick anywhere to close the window")
    line6.setTextColor('SkyBlue1')
    line6.setSize(12)
    line6.setFace("courier")
    line6.draw(win2)
    win2.getMouse()
    win2.close()


def playerBusted(currentScore, gwin):
    cardList = [1,2,3,4,5,6,7,8,9,10,10,10,10]

    busted = 0
    total = 13 #total chances

    for i in range(len(cardList)):
        if currentScore + cardList[i] > 21:
            busted += 1
    
    bustedProb = round(busted/total, 2)

    playerConsult = Text(Point(400, 680), "The probability that you get busted if hitting another card is " + str(bustedProb*100) +" %")
    playerConsult.setTextColor("white")
    playerConsult.setFace("courier")
    playerConsult.setStyle("italic")
    playerConsult.draw(gwin)

    return playerConsult

def main(check): #main function
    #open the main window
    mainwin = GraphWin("Black Jack", 800, 800)
    
    #intro and rules
    if check:
        intro(mainwin)

    Image(Point(400,400), "playbackground.gif").draw(mainwin) 
    blackjack = BlackJack([],[])

    #initial positions for dealer's and player's cards
    initX_player = 500
    initY_player = 600
    initX_dealer = 200
    initY_dealer = 200

    #start dealing initial cards 
    blackjack.playerHand, blackjack.dealerHand, xposD, xposP = \
    blackjack.initDeal(mainwin, initX_dealer, initY_dealer, initX_player, initY_player)

    #evaluate player's and dealer's hand 
    dealerScore = blackjack.dealerHand[1].value()
    dealerBustedProb = DealerBustedProb(10000, dealerScore)
    dealerConsult = Text(Point(300,300), "The probability of dealer being busted is " + str(dealerBustedProb.getBustedProb())+"%")
    dealerConsult.setTextColor("white")
    dealerConsult.setFace("courier")
    dealerConsult.setStyle("italic")
    dealerConsult.draw(mainwin)

    if dealerScore ==1:
        dealerScore = 11

    #print out the probability of dealer being busted for the player's reference
    
    playerScore = blackjack.evaluateHand(blackjack.playerHand)
    
    d = Text(Point(70, 165), "Dealer")
    d.draw(mainwin)
    d.setSize(23)
    d.setTextColor("white")
    d.setFace("courier")
    d.setStyle("bold")
    t = Text(Point(380, 565), "Player")
    t.draw(mainwin)
    t.setSize(23)
    t.setTextColor("white")
    t.setFace("courier")
    t.setStyle("bold")

    #draw player's and dealer's initial score
    scoreP = drawScore(mainwin, 380, 600, playerScore)
    scoreD = drawScore(mainwin, 70, 200, dealerScore)
    
    #evaluate the probabiliy of getting busted for the player and dealer

    current_player_consult = playerBusted(playerScore, mainwin)

    #draw hit and stand button
    buttonHit = Button(mainwin, Point(250, 400), 100, 50, "Hit")
    buttonStand = Button(mainwin, Point(550, 400), 100, 50, "Stand")

    buttonHit.activate()
    buttonStand.activate() 

    point = mainwin.getMouse()

    while not (buttonHit.isClick(point) or buttonStand.isClick(point)):
        point = mainwin.getMouse()
    
    scoreP.undraw()
    
    while buttonHit.isClick(point):
        #when user clicks hit, deal them a new card
        blackjack.playerHand, xposP = blackjack.hit(mainwin, xposP, initY_player)

        #updating player's score
        playerScore = blackjack.evaluateHand(blackjack.playerHand)
        scoreText = drawScore(mainwin, 380, 600, playerScore)

        current_player_consult.undraw()
        current_player_consult = playerBusted(playerScore, mainwin)
        
        if playerScore > 21: #if the player busted

            current_player_consult.undraw()
            text = Text(Point(400, 85), "You busted! Dealer won!")
            text.draw(mainwin)
            text.setSize(35)
            text.setTextColor("firebrick2")
            text.setStyle("bold")
            text.setFace("courier")
            
            recursion(mainwin, main, buttonHit, buttonStand)
            return
        else:
            point = mainwin.getMouse() #keep updating user's click
            scoreText.undraw()

    while not buttonStand.isClick(point): 
        point = mainwin.getMouse()

    current_player_consult.undraw()
    #evaluate player's final hand
    playerScore = blackjack.evaluateHand(blackjack.playerHand)
    drawScore(mainwin, 380, 600, playerScore)

    #dealer starts playing
    scoreD.undraw()
    blackjack.faceDown.undraw()
    dealerCard1 = blackjack.dealerHand[0]
    dealerCard1.drawCard(mainwin, initX_dealer, initY_dealer)
    
    dealerScore = blackjack.dealerPlays(mainwin, xposD, initY_dealer)
    drawScore(mainwin, 75, 200, dealerScore)

    #draw the result
    if dealerScore > 21:
        text = Text(Point(400, 85), "Dealer busted! You won!")
        text.draw(mainwin)
        text.setSize(35)
        text.setTextColor("firebrick2")
        text.setStyle("bold")
        text.setFace("courier")
    elif dealerScore > playerScore:
        text = Text(Point(400, 85), "You lose!")
        text.draw(mainwin)
        text.setSize(35)
        text.setTextColor("firebrick2")
        text.setStyle("bold")
        text.setFace("courier")
    elif dealerScore < playerScore:
        text = Text(Point(400, 85), "You won!")
        text.draw(mainwin)
        text.setSize(35)
        text.setTextColor("firebrick2")
        text.setStyle("bold")
        text.setFace("courier")
        
    else:
        text = Text(Point(400, 85), "It is a stand-off!")
        text.draw(mainwin)
        text.setSize(35)
        text.setTextColor("firebrick2")
        text.setStyle("bold")
        text.setFace("courier")

    recursion(mainwin, main, buttonHit, buttonStand)
    
main(True)
