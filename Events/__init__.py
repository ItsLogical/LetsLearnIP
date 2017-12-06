'''
Assignment: Events
Created on 06 dec. 2017
@author: LetsLearnIP.com
'''

# import the GUI interface from the given library
# library documentation: https://phoenix.labs.vu.nl/doc/python/
from ipy_lib import SnakeUserInterface

# GLOBAL VARIABLES
UI_WIDTH = 40
UI_HEIGHT = 30

def print_event(event):
    ui.print_("%s - %s\n" %(event.name, event.data));

# onSpace -> clear the ui
def process_other(data):
    if data == "space":
        ui.clear()
        ui.show()

# split the data on space, and return the coordinates as integers
def get_coordinates_from_data(data):
    data = data.split()
    return int(data[0]), int(data[1])


# onClick -> place a block on the spot
def process_click(data):
    x,y = get_coordinates_from_data(data)
    ui.place(x, y, ui.WALL)
    ui.show()
    
# process all events that come in 
def process_event(event):
    print_event(event) # Note: makes the program run slow
    if event.name == "click" :
        process_click(event.data)
    elif event.name == "other":
        process_other(event.data)

# START PROGRAM
# initialize the visual interface
ui = SnakeUserInterface(UI_WIDTH, UI_HEIGHT)
ui.show()

# infinite loop that parses the events
while True : 
    event = ui.get_event() # fetches the event using the built-in library function
    process_event(event) # event dispatcher
    