'''
Created on 30 Nov 2017
@author: LetsLearnIP.com
'''

# this class should be able to store a list of coordinates
# and be able to weave in another coordinate_row
class CoordinateRow():

    # we should keep a list where to store all the coordinate objects
    def __init__(self):
        self.coordinate_row = []
     
    # what should happen when we add a coordinate to this object        
    def add_coordinate(self, coordinate):
        self.coordinate_row.append(coordinate)
      
    # how to weave in another coordinate_row correctly (the hardest part of this assignment)  
    def weave_coordinate_row(self, coordinate_row):
        new_coordinate_row = coordinate_row.get()
        resulting_coordinate_row = []
        i = 0
        while i < len(new_coordinate_row):
            if (i >= len(self.coordinate_row)):
                resulting_coordinate_row.extend(new_coordinate_row[i:])
                break
            
            resulting_coordinate_row.append(self.coordinate_row[i])
            resulting_coordinate_row.append(new_coordinate_row[i])
            i += 1
        if i < len(self.coordinate_row):
            resulting_coordinate_row.extend(self.coordinate_row[i:])
            
        self.coordinate_row = resulting_coordinate_row
    
    # helper function that shifts every coordinate in the coordinate row by x,y
    def shift(self, delta_x, delta_y):
        for coordinate in self.coordinate_row:
            coordinate.shift(delta_x, delta_y)
            
    # returns the coordinate_row list (the one that is filled with coordinate objects)
    def get(self):
        return self.coordinate_row

    # returns the coordiante_row as a list (coordinate lists instead of coordinate objects)
    def get_list(self):
        list = []
        for coordinate in self.coordinate_row:
            list.append(coordinate.get())
        return list