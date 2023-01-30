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
    __WAIT_TIME = 10
    __TIMER_TIME = 20
    __init_sens = False

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
        im1 = self.lidar._lidar1.getRangeImage()[0:540:15]
        im2 = self.lidar._lidar1.getRangeImage()[0:540:15]
        compt1 = im1.count(float("inf"))
        compt2 = im2.count(float("inf"))
        compt12 = compt1 + compt2

        if self.__init_sens == False:
            if (compt1 <= compt2):
                self.__sens = True
            elif (compt2 <= compt1):
                self.__sens = False
            self.__init_sens = True

        if self.__waiter == self.__WAIT_TIME:
            if (self.__sens == True):
                self.forward()
            elif (self.__sens == False):
                self.backward()
        else:
            self.stop()
            self.__waiter +=1

        if self.__sens == True and compt12 > 60 and self.__waiter == self.__WAIT_TIME and compt2 <= compt1:
            self.__timer += 1
            if self.__timer == self.__TIMER_TIME:
                self.__sens = False
                self.__timer = 0
                self.__waiter = 0
        elif self.__sens == False and compt12 > 60 and self.__waiter == self.__WAIT_TIME and compt1 <= compt2:
            self.__timer += 1
            if self.__timer == self.__TIMER_TIME:
                self.__sens = True
                self.__timer = 0
                self.__waiter = 0