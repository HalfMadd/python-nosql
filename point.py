class Point: 
    def __init__(self, x, y, z = 0) :
        self.x = x
        self.y = y
        self.z = z
        
    def toString(self):
        echo = "P ("+str(self.x)+", "+str(self.y)
        # print(str(self.z))
        if(self.z != 0):
            echo += ", "+str(self.z)
        echo += ")"
        print(echo)

P = Point(2, 5)
P2 = Point(1, 3, -9)

P.toString()
P2.toString()