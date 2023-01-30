from controller import Robot
from stalker import stalker
from botter import botter

class smash(Robot):

    __WHEEL_RADIUS =  0.1
    __LX = 0.238  # lateral distance from robot's COM to wheel [m].
    __LY = 0.285  # longitudinal distance from robot's COM to wheel [m].
    __speed = [0.0, 0.0, 0.0, 0.0]
    __sens = True
    __timer = 0
    __waiter = 0

    def __init__(self):
        Robot.__init__(self)
        self.motor = botter(self)
        self.lidar = stalker(self)

    def kinematic(self, target):
        self.__speed[0] = 1 / self.__WHEEL_RADIUS * (target[0] - target[1] - (self.__LX + self.__LY) * target[2]);
        self.__speed[1] = 1 / self.__WHEEL_RADIUS * (target[0] + target[1] + (self.__LX + self.__LY) * target[2]);
        self.__speed[2] = 1 / self.__WHEEL_RADIUS * (target[0] + target[1] - (self.__LX + self.__LY) * target[2]);
        self.__speed[3] = 1 / self.__WHEEL_RADIUS * (target[0] - target[1] + (self.__LX + self.__LY) * target[2]);

        self.motor._back_left_motor.setVelocity(self.__speed[0])
        self.motor._back_right_motor.setVelocity(self.__speed[1])
        self.motor._front_left_motor.setVelocity(self.__speed[2])
        self.motor._front_right_motor.setVelocity(self.__speed[3])

    def stop(self):
        self.kinematic([0.0,0.0,0.0])

    def forward(self):
        self.kinematic([5.0,0.0,0.0])

    def backward(self):
        self.kinematic([-5.0,0.0,0.0])

    def left_sideway(self):
        self.kinematic([0.0,5.0,0.0])

    def right_sideway(self):
        self.kinematic([0.0,-5.0,0.0])

    def left_stationary(self):
        self.kinematic([0.0,0.0,5.0])

    def right_stationary(self):
        self.kinematic([0.0,0.0,-5.0])

    def run(self):
        print(self.__waiter)

        if self.__waiter == 20:
            if (self.__sens == True):
                self.forward()
            elif (self.__sens == False):
                self.backward()
        else:
            self.stop()
            self.__waiter +=1

        im1 = self.lidar._lidar1.getRangeImage()[0:540:15]
        im2 = self.lidar._lidar1.getRangeImage()[0:540:15]
        compt = im1.count(float("inf")) + im2.count(float("inf"))

        if (self.__sens == True and compt > 6 and self.__waiter == 20):
            self.__timer += 1
            if self.__timer == 20:
                self.__sens = False
                self.__timer = 0
                self.__waiter = 0
        elif (self.__sens == False and compt > 60 and self.__waiter == 20):
            self.__timer += 1
            if self.__timer == 20:
                self.__sens = True
                self.__timer = 0
                self.__waiter = 0