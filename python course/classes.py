# Classes are used to define new types to model real concepts

# first letter is capitalized!
class Point:
    def move(self):
        print("Move")
        
    def draw(self):
        print("Draw")


point1 = Point()
# now with this new object we can use the functions we have created in the Point class
point1.draw()
# we can also create variables, but each object has its own
point1.x = 10
point1.y = 20
print(point1.x)

point2 = Point()
point2.x = 15
print(point2.x)
