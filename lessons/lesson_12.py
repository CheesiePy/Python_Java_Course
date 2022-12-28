class Person():
    pass

class Car():
    def __init__(self, foul):
        self.foul = foul
        

    def run(self):
        print("run")
        while (self.foul > 0):
            print("driving" , self.foul)
            self.foul -= 1
        print("out of foul")






class Point():
    def __init__(self, x ,y):
        
        self.x = x
        self.y = y
        self.z = 0


    def __str__(self):
        return f"( {self.x} , {self.y} )"


# point1 = Point(1,2)
# point2 = Point(3,4)
# point3 = Point(5,6)
# point4 = Point(7,8)

# point_list = [point1,point2,point3,point4]
car1 = Car(100)

car1.run()




# point3.z = 3

# [print(i) for i in point_list]


# matrix = [[i for i in range(3)] for j in range(3)]

# print(matrix)


