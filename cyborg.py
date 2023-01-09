from robot import Robot

class Human():
    
    def __init__(self,sex):
        if sex == "H":
            self.__sex = False
        elif sex =="F":
            self.__sex = True

class Cyborg(Robot, Human):
    def __init__(self,name,sex):
        Robot.__init__(self,name)
        Human.__init__(self,sex)


if __name__ == "main":
    print("test")