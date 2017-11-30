''' 
Assignment: Pirate
Created on 30 nov. 2017
@author: LetsLearnIP.com 
'''

from coordinate import Coordinate
from coordinate_row import CoordinateRow

# this function takes in a coordinate_row as string
# and converts it to an actual coordinate_row object filled with coordinate objects
def create_coordinate_row(coordinate_row_string):
    # create new object of type CoordinateRow
    coordinate_row = CoordinateRow()
    # split so we get a list of coordinate strings
    coordinate_strings = coordinate_row_string.split()

    # loop over the coordinate strings
    for coordinate_string in coordinate_strings:
        # convert the coordinate string to coordinate object and add it to the coordinate_row object
        coordinate_row.add_coordinate(create_coordinate(coordinate_string))
    
    # return a coordinate_row object that is filled with coordinate objects
    return coordinate_row

# this function takes in a coordinate as string
# and converts it to an actual coordinate object
def create_coordinate(raw_coordinate):
    # split the coordinate into 2 numbers
    raw_coordinate_list = raw_coordinate.split(",")
    # create coordinate object
    coordinate = Coordinate(raw_coordinate_list[0], raw_coordinate_list[1])
    # return the coordinate object
    return coordinate
    
# opens the input file as READ-ONLY
inputFile = open('input.txt', 'r')
# reads the actual content of the file and stores it in input 
input = inputFile.read() 

# in this list, we will store all of the coordinate_row objects
coordinate_rows = [] 
# as given in the assignment the coordinate_rows are separated by '='
# therefore we split on '=' to get a list of every coordinate_row (as string)
coordinate_row_strings = input.split("=") 
# since we now have a coordinate_row list, we can loop over each of these items
for coordinate_row_string in coordinate_row_strings:
    # convert the coordinate_row strings to coordinate_row objects
    coordinate_rows.append(create_coordinate_row(coordinate_row_string))

# now we have all the coordinate_row objects
# we have access to the functions we created in the coordinate_row class
# and using these, we can easily weave multiple rows together

# keep a resulting coordinate_row (starts as an empty coordinate_row)
result = CoordinateRow()

# loop over all other coordinate_rows and weave them into result
for coordinate_row in coordinate_rows:
    # use the weave_coordinate_row function that we defined in the coordinate_row class
    result.weave_coordinate_row(coordinate_row)
    
# all coordinates should be shifted by (1,0) 
result.shift(1,0)

# print the resulting list
# we cannot print result directly, because it will then print the object
# whereas it should print the list of coordinates 
print result.getList()