from robot import Robot
from random import randint

class Human():
    
    def __init__(self,sex):
        if sex == "M":
            self.__sex = False
        elif sex =="F":
            self.__sex = True

    def eat(self,food):
        if type(food) is str:
            print(food + " assimilée")
        elif type(food) is list:
            for i in range(len(food)):
                self.eat(food[i])

    def digest(self):
        print(self.name + " a digéré")

class Cyborg(Robot, Human):
    def __init__(self,name,sex):
        Robot.__init__(self,name)
        Human.__init__(self,sex)
        self.name = name
        self.sexe = sex

    def berserk(self,val):
        if val == 0:
            print("8 morts 6 blessés je pète ma bière MA LUBULLULE!!!")


if __name__ == "__main__":
    cyborg = Cyborg('Deux Ex Machina', 'M')

    print(cyborg.name, 'sexe', cyborg.sexe)
    print('Charging battery...')
    cyborg.charge()
    cyborg.get_state()
    cyborg.eat('banana')
    cyborg.eat(['coca', 'chips'])
    cyborg.digest()
    cyborg.berserk(randint(0,1))