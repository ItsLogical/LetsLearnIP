'''
Created on 30 Nov 2017
@author: LetsLearnIP.com
'''

# the class that should store coordinates
class Coordinate():

    # a coordinate can only be created with an x and y variable
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

    # to shift a coordinate
    def shift(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    # to return the coordinate as a list (instead of object)        
    def get(self):
        return self.x, self.y