import tkinter as tk
import timer
import pause

import pygame

# Set the desired size for the window
window_width = 900
window_height = 600

# The following is how we deal with sound




clock1 = timer.Timer(True,1)
clock2 = timer.Timer(False,1)
pause = pause.Pause()


def on_key_pressSPACE(event, red):
    # only will click if we are not paused
    if not pause.getPause():
        clock1.click()
        clock2.click()

        

def on_key_pressZ(event):
    pause.toggle()


root = tk.Tk()
# This is the title at the top part of the page
root.title("Screaming Clock 9000")

# Time to set the width 
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate x and y coordinates to center the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the geometry of the window
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Bind the key press event (the top one is how we pass arg)
root.bind("<space>", lambda event: on_key_pressSPACE(event, "Hello"))

root.bind("<Escape>", lambda event: root.destroy())

root.bind("<z>", on_key_pressZ)

# The following is our table 

# We need to create some variables


# Create the first canvas
canvas1 = tk.Canvas(root, width=int(window_width/2)-20, height=window_height, bg=clock1.getColor())
canvas1.pack(padx=1, side=tk.LEFT)  


val1 = canvas1.create_text(((int(window_width/2)-20)/2), (window_height/2)-20, text=str(clock1.getClockTime()), fill="black", font=("Helvetica", 120))

# Create the second canvas
canvas2 = tk.Canvas(root, width=int(window_width/2)-20, height=window_height, bg=clock2.getColor())
canvas2.pack(padx=1,side=tk.RIGHT)  # Pack on the left side

val2 = canvas2.create_text(((int(window_width/2)-20)/2), (window_height/2)-20, text=str(clock2.getClockTime()), fill="black", font=("Helvetica", 120))


def update_clock_and_text():
    # Check if paused/done
    if not pause.getPause():
        # TICK 
        clock1.tick()
        clock2.tick()
        #print(pause.getPause())
        

    # This is wherer we check if someone has won
    if (clock1.getSeconds() <= float(0.0)):
        clock1.loss()
        clock2.win()

        clock1.setSeconds(0)
      

    elif(clock2.getSeconds() <= float(0.0)):
        clock2.loss()
        clock1.win()       
        
        clock2.setSeconds(0)
       


    # Lower time of 1 person
    canvas1.config(bg=clock1.getColor())
    canvas2.config(bg=clock2.getColor())
   
    # Get some sort of color action here
    canvas1.itemconfig(val1, text=str(clock1.getClockTime()))
    canvas2.itemconfig(val2, text= str(clock2.getClockTime()))
    root.after(100, update_clock_and_text)  # Update every second (100 ms)

# Start the loop
update_clock_and_text()


# Start the main event loop
root.mainloop()



# Have the colours change and have a pause func