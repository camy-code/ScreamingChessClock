# Chess Clock with Sound

## Introduction

This project implements a chess clock that screams whenever the turn changes just to ensure the players notice. The clock features timers that can be paused, swapped, and will play sounds based on when they are turned enabled.

Github [link](https://github.com/camy-code/ScreamingChessClock)




## Requirements

- The clock can be paused by pressing the "Z" key.
- Timers will switch whenever the space bar is pressed.
- If a player's time runs out, a pleasant ding sound will play, and no actions can pause the clock or swap the timers.
- Pressing the space bar while the clock is running (not paused) will swap the timers and play a scream sound.

## Making the GUI

The first step in this project was creating the graphical user interface (GUI). This was the most challenging part since I was not familiar with Tkinter. After following a tutorial to create the initial window, I encountered five main issues:

1. Resizing the window to the desired dimensions.
2. Centering the window on the screen.
3. Listening for button presses.
4. Updating displayed values.
5. Playing sound effects.

## Resizing and Centering the Window

To address the first two issues, I used the "geometry" method in Tkinter to set both the size and position of the window. Here is the code I used:

```python
import tkinter as tk

# Create the main window
root = tk.Tk()


# Time to set the width 
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate x and y coordinates to center the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the geometry of the window
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
```

## Listening for Button Presses
For handling button presses, Tkinter provides a simple method to bind key events to functions. I created functions to modify the timer values based on these events. Here is the relevant code:
```python
# pause and clock are objects

def on_key_pressSPACE(event):
    # only will click if we are not paused
    if not pause.getPause():
        clock1.click()
        clock2.click()

        

def on_key_pressZ(event):
    pause.toggle()

# Bind the key press events to their respective functions
root.bind('<z>', on_key_pressZ)
root.bind('<space>', on_key_pressSPACE)
```
## Updating Values
To ensure the displayed values are updated regularly, I implemented a method that runs every 100 milliseconds. Tkinter allows us to identify GUI components easily, making this process straightforward.
```python

def update_clock_and_text():
    # Check if paused/done
    if not pause.getPause():
        # TICK 
        clock1.tick()
        clock2.tick()
        #print(pause.getPause())
        

    # This is where we check if someone has won
    if (clock1.getSeconds() <= float(0.0)):
        clock1.loss()
        clock2.win()

        clock1.setSeconds(0)
      

    elif(clock2.getSeconds() <= float(0.0)):
        clock2.loss()
        clock1.win()       
        
        clock2.setSeconds(0)
       


    # Ensure that the colors relates to the correct state
    canvas1.config(bg=clock1.getColor())
    canvas2.config(bg=clock2.getColor())
   
    # Get some sort of color action here
    canvas1.itemconfig(val1, text=str(clock1.getClockTime()))
    canvas2.itemconfig(val2, text= str(clock2.getClockTime()))
    root.after(100, update_clock_and_text)  # Update every second (100 ms)

# Start the loop
update_clock_and_text()
```

## Playing Sound
For sound playback, I used Pygame, which is simple to work with. To play sounds, I can call the play method as shown in the example below:
```python
import pygame

# Initialize Pygame and load sound files
pygame.init()
ding = pygame.mixer.Sound('ding.wav')
scream = pygame.mixer.Sound('scream.wav')

# Example of playing the ding sound
ding.play() # This plays the audio so
```

## Logic
The logic for the clock is straightforward, involving two timers. I used a design technique that defines states for the clock, ensuring that all colors and values are synchronized correctly. For example, in the tick() method, the clock always ticks, but it only decreases the time when it is active. This design approach simplified the GUI code.
```python
    def tick(self):
        if self.seconds > 0:
            if self.state == 1: # State 1 is on
                self.seconds -= 0.1 # We change it now
```

The second way of using states was when we needed to set the correct colors for the states. This way of design helped ensure there was as little thinking done in the GUI as possible in order to help with encapsulation.
```python
 def getColor(self):

        if self.state == 0: # OFF
            self.color = "#FFA07A"
        elif self.state == 1: # ON
            self.color = "lightblue"
        elif self.state == 3: # We have not started timer
            self.color = "#D3D3D3"
        elif self.state == 4: # We have lost
            self.color = "#D97A6B"
        elif self.state == 5: # We have won
            self.color = "#7FBF7F"
        
        return self.color
```
## Future improvements and conclusion
Further improvements to this program could be to have a start menu, have the user implement custom sounds, as well as add a wider variety of sounds. As the goal of this project was to learn TKinter and get into the habit of working on projects we will leave the project as is for now.
