class ShapeInterface:
    def draw(self):
        pass


class Circle(ShapeInterface):
    def draw(self):
        print("circle.draw")



class Square(ShapeInterface):
    def draw(self):
        print("square.draw")



class ShapeFactory:
    @staticmethod
    def getShape(type):
        if type == 'circle':
            return Circle()
        if type == 'square':
            return Square()
        assert 0,'Could not find shape '+type



f = ShapeFactory()
s = f.getShape('square')
s.draw()

f = ShapeFactory()
s = f.getShape('circle')
s.draw()

# In Factory pattern, we create object without exposing the 
# creation logic to the client and 
# refer to newly created object using a common interface.