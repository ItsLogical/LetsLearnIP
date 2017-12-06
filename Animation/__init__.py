'''
Assignment: Animation
Created on 06 dec. 2017
@author: LetsLearnIP.com
'''

# import the GUI interface from the given library
# library documentation: https://phoenix.labs.vu.nl/doc/python/
from ipy_lib import SnakeUserInterface

# GLOBAL VARIABLES
UI_WIDTH = 24
UI_HEIGHT = 9
START_POSITION = [0,0]
START_SPEED = 24.0

# useful for debugging
def print_event(event):
    ui.print_("%s - %s\n" %(event.name, event.data));    

def update_current_position():
    global current_position
    # update the current position
    new_x = current_position[0] + 1
    new_y = current_position[1]
  
    if new_x >= UI_WIDTH:
        new_x = 0
        new_y += 1
    if new_y >= UI_HEIGHT:
        new_y = 0
        
    current_position = [new_x, new_y]

# moves the current position and updates the GUI
def do_animation_step():
    update_current_position()
    
    # update GUI
    ui.clear()
    ui.place(current_position[0], current_position[1], current_color)
    ui.show()
    
    # extra print status
    ui.clear_text()
    ui.print_("speed: %0.1f\n" %current_speed)
    ui.print_("position: %s\n" %current_position)
    ui.print_("color: %d\n" %current_color)

def process_arrow(data):
    global current_speed
    if data == 'l':
        current_speed -= 0.5
        ui.set_animation_speed(current_speed)
    if data == 'r':
        current_speed += 0.5
        ui.set_animation_speed(current_speed)

def process_alarm(data):
    if data == "refresh":
        do_animation_step()

# on g -> change color
def process_letter(data):
    global current_color
    
    if data == "g":
        if current_color == ui.WALL:
            current_color = ui.SNAKE
        elif current_color == ui.SNAKE:
            current_color = ui.WALL
         
# process all events that come in 
def process_event(event):
    # print_event(event) # Note: makes the program run slow
    if event.name == "letter":
        process_letter(event.data)
    elif event.name == "alarm":
        process_alarm(event.data)
    elif event.name == "arrow":
        process_arrow(event.data)

# START PROGRAM
# initialize the visual interface
ui = SnakeUserInterface(UI_WIDTH, UI_HEIGHT)
ui.show()

# state variables
current_color = ui.WALL
current_position = START_POSITION
current_speed = START_SPEED

# initial settings
ui.set_animation_speed(current_speed)
ui.place(current_position[0], current_position[1], current_color)

# infinite loop that parses the events
while True : 
    event = ui.get_event() # fetches the event using the built-in library function
    process_event(event) # event dispatcher
    