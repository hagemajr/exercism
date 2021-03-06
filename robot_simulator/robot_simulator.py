NORTH = 1
EAST = 2
SOUTH = 4
WEST = 8

class Robot:
    def __init__(self,facing=1,x=0,y=0):
        self.coordinates = (x,y)
        self.bearing = facing
    
    def turn_left(self):
        if self.bearing == NORTH:
            self.bearing = WEST
        else:
            self.bearing = self.bearing >> 1 
    
    def turn_right(self):
        if self.bearing == WEST:
            self.bearing = NORTH
        else:
            self.bearing = self.bearing << 1
    
    def advance(self):
        if self.bearing == NORTH:
            x,y = self.coordinates
            y += 1
            self.coordinates = (x,y)
        elif self.bearing == SOUTH:
            x,y = self.coordinates
            y -= 1
            self.coordinates = (x,y)
        elif self.bearing == EAST:
            x,y = self.coordinates
            x += 1
            self.coordinates = (x,y)
        else:
            x,y = self.coordinates
            x -= 1
            self.coordinates = (x,y)
    
    def simulate(self,commands):
        for command in commands:
            if command == 'L':
                self.turn_left()
            elif command == 'R':
                self.turn_right()
            elif command == 'A':
                self.advance()
            else:
                raise ValueError("Invalid instruction")

#robot = Robot(4, 8, 4)
#robot.simulate("LAAARRRALLLL")
#print("{} - {}".format(robot.coordinates,robot.bearing))
#self.assertEqual(robot.coordinates, (11, 5))
#self.assertEqual(robot.bearing, NORTH)
