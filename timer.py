import pygame

pygame.mixer.init()
ding = pygame.mixer.Sound("ding.wav")
scream = pygame.mixer.Sound("scream.wav")

class Timer:
    # The followin is state designed class. Here are the states so you don't forget!
    # State 0: It is not the clocks turn
    # State 1 It is the clock turn, now TICK!
    # State 2, -- Unused state --
    # State 3 This is the start phase
    # State 4 This means we LOST
    # State 5 This means we WON


    def __init__(self,isFirst, minute) -> None:
        self.isFirst = isFirst # This corresponds to 
        self.state = 3
        self.color = "grey"
        self.seconds = float(int(minute) * 60)

        #self.seconds = minute


    def win(self):
        if self.state != 5:
            ding.play()
            
        self.state = 5

    def loss(self):
        self.state = 4

    # Set mode
    def click(self):
        if self.state == 3:
            if self.isFirst == True:
                self.state = 1
            else:
                self.state = 0 # This means we are off for now

        elif self.state == 5:
            self.state = 5

        elif self.state == 4:
            self.state = 4

        elif self.state == 4:
            self.state = 4 # 4 means we are done

        else:
            self.state = 1- self.state 
            scream.play()
            # This is a big brain toggle
    
    # Def tick (will tick by 0.1 sec)(only ticks when state == 1 )
    def getColor(self):

        if self.state == 0:
            self.color = "#FFA07A"
        elif self.state == 1:
            self.color = "lightblue"
        elif self.state == 3:
            self.color = "#D3D3D3"
        elif self.state == 4:
            self.color = "#D97A6B"
        elif self.state == 5:
            self.color = "#7FBF7F"
        
        return self.color
    
    def setColor(self):
        self.color = "grey" # This needs to be changed
       

    def getState(self):
        return self.state
    
    def tick(self):
        if self.seconds > 0:
            if self.state == 1:
                self.seconds -= 0.1 # We change it now

    def getSeconds(self):
        return round(self.seconds,2)
    

    def getClockTime(self):
        minutes = int(self.seconds // 60)

        # Calculate seconds
        seconds = int(self.seconds % 60)
        if seconds < 10:
            seconds = f"0{seconds}"

        # Calculate milliseconds
        ms100 = int((self.seconds % 1) * 10)
        return f"{minutes}:{seconds}.{ms100}"
    
    def setSeconds(self, num):
        self.seconds = num
        
            