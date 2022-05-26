import turtle as t
from random import choice
import numpy as np
import time

# Define an action_space helper class
class action_space:
    def __init__(self, n):
        self.n = n
    def sample(self):
        num = np.random.choice(range(self.n))
        # covert 0-6 to 1-7 to avoid confusion 
        action = 1+num
        return action
    
# Define an obervation_space helper class    
class observation_space:
    def __init__(self, row, col):
        self.shape = (row, col)

class conn():
  
    def __init__(self): 
        # use the helper action_space class
        self.action_space=action_space(7)
        # use the helper observation_space class
        self.observation_space=observation_space(7,6)
        self.info=""   
        # The x-coordinates of the center of the 7 columns
        self.xs = [-300,-200,-100,0,100,200,300]
        # The y-coordinates of the center of the 6 rows
        self.ys = [-250,-150,-50,50,150,250]  
        self.showboard=False  
        self.game_piece=None 
            
    def reset(self):  
        # The X player moves first
        self.turn = "red"
        # Create a list of valid moves
        self.validinputs = [1,2,3,4,5,6,7]
        # Create a list of lists to track game pieces
        self.occupied = [list(),list(),list(),list(),list(),list(),list()]
        # Tracking the state
        self.state=np.array([[0,0,0,0,0,0],
                            [0,0,0,0,0,0],
                            [0,0,0,0,0,0],
                            [0,0,0,0,0,0],
                            [0,0,0,0,0,0],
                            [0,0,0,0,0,0],
                            [0,0,0,0,0,0]])
        self.done=False
        self.reward=0     
        return self.state        
        
    # step() function: place piece on board and update state
    def step(self, inp):
        # Remember the current game piece
        self.game_piece=[inp-1, len(self.occupied[inp-1]), self.turn]        
        # update the state: red is 1 and yellow is -1
        self.state[inp-1][len(self.occupied[inp-1])]=2*(self.turn=="red")-1       
        # Add the move to the occupied list 
        self.occupied[inp-1].append(self.turn)

        # Update the list of valid moves
        if len(self.occupied[inp-1]) == 6 and inp in self.validinputs:
            self.validinputs.remove(inp)  
        # check if the player has won the game
        if self.win_game(inp) == True:
            self.done=True
            # reward is 1 if red won; -1 if yellow won
            self.reward=2*(self.turn=="red")-1
            self.validinputs=[]
        # If all cellls are occupied and no winner, it's a tie
        elif len(self.validinputs) == 0:
            self.done=True
            self.reward=0
        else:
            # Give the turn to the other player
            if self.turn == "red":
                self.turn = "yellow"
            else:
                self.turn = "red"             
        return self.state, self.reward, self.done, self.info
                     
    # Determine if a player has won the game
    # Define a horizontal4() function to check connecting 4 horizontally
    def horizontal4(self, x, y):
        win = False
        for dif in (-3, -2, -1, 0):
            try:
                if self.occupied[x+dif][y] == self.turn\
                and self.occupied[x+dif+1][y] == self.turn\
                and self.occupied[x+dif+2][y] == self.turn\
                and self.occupied[x+dif+3][y] == self.turn\
                and  x+dif >= 0:
                    win = True            
            except IndexError:
                pass
        return win         
    # Define a vertical4() function to check connecting 4 vertically
    def vertical4(self, x, y):
        win = False
        try:
            if self.occupied[x][y] == self.turn\
            and self.occupied[x][y-1] == self.turn\
            and self.occupied[x][y-2] == self.turn\
            and self.occupied[x][y-3] == self.turn\
            and y-3 >= 0:
                win = True     
        except IndexError:
            pass
        return win   
    # Define a forward4() function to check connecting 4 diagonally in / shape
    def forward4(self, x, y):
        win = False
        for dif in (-3, -2, -1, 0):
            try:
                if self.occupied[x+dif][y+dif] == self.turn\
                and self.occupied[x+dif+1][y+dif+1] == self.turn\
                and self.occupied[x+dif+2][y+dif+2] == self.turn\
                and self.occupied[x+dif+3][y+dif+3] == self.turn\
                and x+dif >=  0 and y+dif >= 0:
                    win = True            
            except IndexError:
                pass
        return win     
    # Define a back4() function to check connecting 4 diagonally in \ shape
    def back4(self, x, y):
        win = False
        for dif in (-3, -2, -1, 0):
            try:
                if self.occupied[x+dif][y-dif] == self.turn\
                and self.occupied[x+dif+1][y-dif-1] == self.turn\
                and self.occupied[x+dif+2][y-dif-2] == self.turn\
                and self.occupied[x+dif+3][y-dif-3] == self.turn\
                and x+dif >=  0 and y-dif-3 >= 0:
                    win = True            
            except IndexError:
                pass
        return win         
    
    # Define a win_game() function to check if someone wins the game
    def win_game(self, inp):
        win = False
        x = inp-1
        y = len(self.occupied[inp-1])-1
        # Check all winning possibilities
        if self.vertical4(x,y)==True:
            win = True
        if self.horizontal4(x,y)==True:
            win = True
        if self.forward4(x,y)==True:
            win = True
        if self.back4(x,y)==True:
            win = True
        return win

    def display_board(self):
        # Set up the screen
        try:
            t.setup(730,680, 10, 70)
        except:
            t.setup(730,680, 10, 70)
        t.hideturtle()
        t.tracer(False)
        t.title("Connect Four in Turtle Graphics")
        # Draw frame
        t.pensize(5)
        t.up()
        t.goto(-350,-300)
        t.down()
        t.begin_fill()
        t.color("black", "blue")
        t.forward(700)
        t.left(90)
        t.forward(600)
        t.left(90)
        t.forward(700)
        t.left(90)
        t.forward(600)
        t.left(90)
        t.end_fill()
        t.up()
        # Write column numbers on the board
        colnum = 1
        for x in range(-300, 350, 100):
            t.goto(x,300)
            t.write(colnum,font = ('Arial',20,'normal'))
            t.goto(x,-330)
            t.write(colnum,font = ('Arial',20,'normal'))
            colnum +=  1          
        # Show white cells
        for col in range(7):
            for row in range(6):
                t.up()
                t.goto(self.xs[col],self.ys[row])
                t.dot(80,"white") 
        t.update()                  
        # Create a second turtle to show disc falling
        self.fall = t.Turtle()
        self.fall.up()
        self.fall.hideturtle()
        
    def render(self):
        if self.showboard==False:
            self.display_board()
            self.showboard=True

        if self.game_piece is not None:
            # Show the disc fall from the top
            col, row, c = self.game_piece
            if row<7:
                for i in range(6,row+1,-1):
                    self.fall.goto(self.xs[col],self.ys[i-1])
                    self.fall.dot(80,c)
                    t.update()
                    time.sleep(0.05)
                    self.fall.clear()
            # Go to the cell and place a dot of the player's color
            t.up()
            t.goto(self.xs[col],self.ys[row])
            t.dot(80,c)            
            t.update() 
        
    def close(self):
        time.sleep(1)
        try:
            t.bye()
        except t.Terminator:
            print('exit turtle')
            
            
            
            
            
            
            