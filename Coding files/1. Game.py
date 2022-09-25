#Chloe Nguyen - Phuong Nguyen
#Final Project Main File
#May 4, 2022

from Pipeclass import *
from Birdclass import *
from buttonClass import *

#using pygame for sound effect only
import pygame
from pygame.locals import *
pygame.init()
pygame.mixer.init()
s = 'sound'

#sources of sounds: freesound.org and incompetech.filmmusic.io
flapSound = pygame.mixer.Sound(os.path.join(s, 'flapsound.wav'))
gameOver = pygame.mixer.Sound(os.path.join(s, 'gameOver.wav'))
passSound = pygame.mixer.Sound(os.path.join(s, 'pass.wav'))
hitSound = pygame.mixer.Sound(os.path.join(s, 'hit.mp3'))
music = pygame.mixer.music.load(os.path.join(s, 'music.mp3'))

def styleText(text, gwin, point, size = 14, color = "black"):
    """helper function to create style Text"""
    
    tObject = Text(point, text)
    tObject.draw(gwin)
    tObject.setStyle("bold")
    tObject.setFace("courier")
    tObject.setSize(size)
    tObject.setTextColor(color)

    return tObject

def clear(gwin):
    """sub-function to clear the window"""
    #keep the back ground image
    for item in gwin.items[1:]: 
        item.undraw()
    gwin.update()
    
def highscore(gwin):
    """sub-function to display high score"""
    
    leaders = open("Flappy Bird Leaders.txt", "r").readlines()
    
    yPos = 45

    #initiate a list of players with their scores
    highScore = []                                                          
    for line in leaders:
        line.replace("/n", "")
        user = line.split()
        name_score = (user[0], int(user[-1]))
        #append player's name and their score to the list
        highScore.append(name_score)                                       

    #sorted the list in descending order key = score                                                                      
    highScore= sorted(highScore, key=lambda tup: tup[1], reverse = True) 

    styleText("HIGH SCORE", gwin, Point(30, 52), 20)

    #display 10 highest scores
    for i in range(10):
        
        styleText(str(highScore[i][0].ljust(10, ' '))+str(highScore[i][1]), gwin, Point(30, yPos))
        yPos -= 3
    
def flappy(win, space, speed, character):
    """sub-function to handle the main game"""
    pygame.mixer.music.play(-1)
    #Create Bird object
    bird = Bird(Point(20, 20), win, 0.03, character)
    #have the position of the bird
    bottom, top, bird_x = bird.getPos()

    #check user's key
    command = win.checkKey()

    #Display Initial Score
    init_score = 0
    score_text = styleText("SCORE: "+str(init_score), win, Point(50, 55))
    

    
    cont = True     #booleran to show if the game is over or not
    xPos = 63       #inital xPos of the pipe
    
    
    while cont:     #while the game is not over 
        
        #choose a random y - position which will the the center of the space between 2 pipes
        pipeY = randrange(15, 45)
        
        #Create Pipe Object
        pipes = Pipe(xPos, pipeY, win, space, speed)

        #calculate the boundaries of the pipes
        char_height = 4 #all characters' images are 40x40 pixels
        pipe_ymin = pipes.yPos - space/2 - char_height/2
        
        pipe_ymax = pipes.yPos + space/2 + char_height/2
        
        notCollided = True #booleran to check if the bird is collided with the pipes or out of the window

        #while the pipes are moving and the bird is not collided
        while int(pipes.xPos) > -3 and notCollided:
            
            pipes.xPos = pipes.move()

            #if user press space, the bird will fly
            fall = True
            if command == "space": 
                fall = False
            if fall:
                bird.fall()
            else:
                bird.fly()
                pygame.mixer.Sound.play(flapSound) #flap sound effect

            #update user's command    
            command = win.checkKey()

            #update the bird's position
            bottom, top, bird_x = bird.getPos()

            #update the notCollided booleran
            if bird_x < pipes.xPos-pipes.width//2 or bird_x > pipes.xPos+pipes.width//2:
                #when the bird is outside the space between two pipes
                notCollided = True
            
            else:
                notCollided = bottom < pipe_ymax and top > pipe_ymin
                pygame.mixer.Sound.play(passSound) #sound effect when passing the pipes

            if bird.yPos > 58 or bird.yPos <2:
                notCollided = False
            
        
        #when it exits the inside while loop  
        if notCollided:             #if the bird is not collided
            
            cont = True             #continue the game
        else:
            
            cont = False            #game over
            pygame. mixer. music. stop()
            pygame.mixer.Sound.play(hitSound)
            sleep(0.1)
            pygame.mixer.Sound.play(gameOver) #sound effect
            over = Image(Point(30, 35), "img/over.png")
            over.draw(win)
            
            styleText("Click anywhere to continue.", win, Point(30, 27), 16)
            win.getMouse()
            over.undraw()
            return init_score       #return the player's score
            
        #update the score after each iterration
        score_text.undraw()

        #Level: easy
        if space == 9: 
            init_score += 1
        #Level: medium
        elif space == 7: 
            init_score += 2
        #Level: hard
        else: 
            init_score += 3
        score_text = styleText("SCORE: "+str(init_score), win, Point(50, 55))

        
        pipes.undraw()

def chooseLevel(win):
    """sub-function to handle user's choice of difficulty"""

    styleText("Enter player's name and choose game level:", win, Point(30, 50), 16)

    #create entry box for the user to input their name
    playerName = Entry(Point(30, 42), 20)
    playerName.draw(win)
    playerName.setText("Guest")

    #create buttons
    easy = Button(win, Point(30, 30), 10, 5, "Easy")
    medium = Button(win, Point(30, 20), 10, 5, "Medium")
    hard = Button(win, Point(30, 10), 10, 5, "Hard")

    point = win.getMouse()

    name = playerName.getText() #get the user's name
    
    while not (easy.isClick(point) or medium.isClick(point) or hard.isClick(point)):
        point = win.getMouse()

    #assign different space and speed (of the pipes) according to the level of difficulty
    if easy.isClick(point):
        space = 9
        speed = 0.05
    elif medium.isClick(point):
        space = 7
        speed = 0.04
    else:
        space = 5
        speed = 0.03

    return name, space, speed

def chooseCharacter(win):
    """sub-function to handle user's choice of character"""
    styleText("Choose the character you like", win, Point(30, 50), 16)

    squirrel = Image(Point(10, 40), "img/squirrel.png")
    bird = Image(Point(30, 40), "img/bird.png")
    fish = Image(Point(50, 40), "img/fish.png")

    squirrel.draw(win)
    bird.draw(win)
    fish.draw(win)
    #create buttons for the user's to choose
    buttonA = Button(win, Point(30, 30), 10, 5, "squirrel")
    buttonB = Button(win, Point(30, 20), 10, 5, "fish")
    buttonC = Button(win, Point(30, 10), 10, 5, "bird")

    pt = win.getMouse()

    while not (buttonA.isClick(pt) or buttonB.isClick(pt) or buttonC.isClick(pt)):
        pt = win.getMouse()

    for button in [buttonA, buttonB, buttonC]:
        if button.isClick(pt):
            return button.getLabel()
   
def main():
    """main function of the program"""
    
    window = GraphWin("Flappy Bird", 600, 600)
    window.setCoords(0, 0, 60, 60)
    
    background = Image(Point(30, 30), "img/back.png")
    
    background.draw(window)

    title = Image(Point(30, 50), "img/title.png")
    title.draw(window)
    styleText("Press <Space> for the bird to fly", window, Point(30, 40), 16)

    button1 = Button(window, Point(30, 30), 10, 5, "Start")
    button2 = Button(window, Point(30, 20), 10, 5, "High Score")
    button3 = Button(window, Point(30, 10), 10, 5, "Quit")
    
    point = window.getMouse()

    while not button3.isClick(point):                   #while the quit button is not clicked
        
        if button1.isClick(point): 
            
            clear(window) 
            
            name, space, speed = chooseLevel(window)    #get the user's name and level of difficulty

            clear(window)

            character = chooseCharacter(window) #get the user's choice of character

            clear(window)

            if character == "squirrel":
                background = Image(Point(30, 30), "img/forest.png")
                background.draw(window)
                
            if character == "fish":
                background = Image(Point(30, 30), "img/ocean.png")
                background.draw(window)
            score = flappy(window, space, speed, character)        #run the main game function
            clear(window)

            #display score and medal after the game is over
            scoreboard = Image(Point(30, 45), "img/scoreboard.png")
            scoreboard.draw(window)
            
            if score < 10:
                medal = Image(Point(20,44), "img/shit.png")
            elif score < 20:
                medal = Image(Point(20, 44), "img/bronze.png")
            elif score < 30:
                medal = Image(Point(20, 44), "img/silver.png")
            elif score >= 30:
                medal = Image(Point(20, 44), "img/gold.png")
                
            medal.draw(window)
            score_text = styleText(str(score), window, Point(40, 43), 35, "saddlebrown")

            #update the record file with the player's name and score
            with open("Flappy Bird Leaders.txt", "a") as file:
                file.write(str(name)+ "   " + str(score) + "\n")
            
            #redraw buttons
            
            button1 = Button(window, Point(30, 30), 10, 5, "Restart")
            button2 = Button(window, Point(30, 20), 10, 5, "High Score")
            button3 = Button(window, Point(30, 10), 10, 5, "Quit")
            
            
        elif button2.isClick(point):
            #display high scores
            
            clear(window)
            highscore(window)

            button1 = Button(window, Point(20, 10), 10, 5, "Restart")
            button3 = Button(window, Point(40, 10), 10, 5, "Quit")
        
        point = window.getMouse()

    #close the program 
    window.close()
    sys.exit()
        
main()
   

