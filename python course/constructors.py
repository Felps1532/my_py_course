# a constructor is a function that gets called at the time of creating an object

class Point:
    # this is the 'constructor' function
    # 'self' represents that object.
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move(self):
        print("Move")
        
    def draw(self):
        print("Draw")
        
        
# now this point will have its x and y inicialized, by default
point = Point(10, 20)
point.x = 12
print(point.x)
 