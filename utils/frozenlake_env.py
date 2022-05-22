import turtle as t
import numpy as np
import time


# Define an action_space helper class
class action_space:
    def __init__(self, n):
        self.n = n
    def sample(self):
        return np.random.choice(range(self.n))
    
# Define an obervation_space helper class    
class observation_space:
    def __init__(self, n):
        self.shape = (n,)

# Define the Frozen game environment
class Frozen():
    def __init__(self):        
        self.done=False
        self.reward=0.0
        self.info={'prob': 1.0}
        self.state=0
        self.actual_actions=[(0, -1), (1, 0), (0, 1), (-1, 0)]
        self.action_space=action_space(4)
        self.observation_space=observation_space(16)
        self.showboard=False  
        self.grid=[]
        for x in range(4):
            for y in range(4):
                self.grid.append((x,y))

    def reset(self):  
        self.state=0
        self.done=False
        self.reward=0.0
        return self.state

    def step(self, action):
        actual_action=self.actual_actions[action]
        co_or=self.grid[self.state]
        new_co_or=(actual_action[0]+co_or[0], actual_action[1]+co_or[1])
        if actual_action[0]+co_or[0]<0 or actual_action[0]+co_or[0]>3:
            new_co_or=co_or
        if actual_action[1]+co_or[1]<0 or actual_action[1]+co_or[1]>3:
            new_co_or=co_or        
        new_state=self.grid.index(new_co_or)
        if new_state==15:
            self.reward=1.0
            self.done=True
        if new_state in [5,7,11,12]:
            self.reward=-1.0
            self.done=True
        self.state=new_state
        return new_state, self.reward, self.done, self.info
 
    def display_board(self):
        try:
            t.setup(850,850, 10, 70) 
        except t.Terminator:
            t.setup(850,850, 10, 70)                       
        t.hideturtle()
        t.bgcolor("alice blue")
        t.tracer(False)
        t.title('The Frozen Lake Game')
        t.clear()
        t.pensize(3)
        for i in range(-400,600,200):  
            t.up()
            t.goto(i, -400)
            t.down()
            t.goto(i, 400)
            t.up()
            t.goto(-400,i)
            t.down()
            t.goto(400,i)
            t.up()           
        for (x,y) in [(-100,100),(300,100),(300,-100),(-300,-300)]:
            t.goto(x,y)
            t.dot(150,"light gray")
            t.color('blue')
            t.goto(x-30,y-20)
            t.write("hole",font=("Helvetica",30)) 
        self.xycor={(3, 0):(-400, -400), (2, 0):(-400, -200), 
               (1, 0):(-400, 0), (0, 0):(-400, 200), 
               (3, 1):(-200, -400), (2, 1):(-200, -200), 
               (1, 1):(-200, 0), (0, 1):(-200, 200), 
               (3, 2):(0, -400), (2, 2):(0, -200), 
               (1, 2):(0, 0), (0, 2):(0, 200), 
               (3, 3):(200, -400), (2, 3):(200, -200), 
               (1, 3):(200, 0), (0, 3):(200, 200)}
        state_grid = self.grid[self.state]
        state_xy = self.xycor[state_grid]
        t.color('blue')
        t.goto(-350,350)
        t.write("start",font=("Helvetica",30))        
        t.goto(300,-350)
        t.write("goal",font=("Helvetica",30)) 
        t.color('black')
        # Place a red dot in the current state
        self.fall = t.Turtle()
        self.fall.up()
        self.fall.hideturtle()
        self.fall.goto(state_xy[0]+100,state_xy[1]+100)
        self.fall.dot(150,"red")
        t.update()

    def render(self):
        if self.showboard==False:
            self.display_board()
            self.showboard=True        
        state_grid = self.grid[self.state]
        state_xy = self.xycor[state_grid]
        # update the current position
        self.fall.clear()
        self.fall.goto(state_xy[0]+100,state_xy[1]+100)
        self.fall.dot(150,"red")
        t.update()
    def close(self):
        time.sleep(1)
        try:
            t.bye()
        except t.Terminator:
            print('exit turtle')

