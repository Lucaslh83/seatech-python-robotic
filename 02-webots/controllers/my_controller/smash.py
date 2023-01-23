from controller import Robot, Motor, PositionSensor

class Smash(Robot):

    __WHEEL_RADIUS =  0.1
    __LX = 0.238  # lateral distance from robot's COM to wheel [m].
    __LY = 0.285  # longitudinal distance from robot's COM to wheel [m].
    __SPEED_INCREMENT = 0.05
    __MAX_SPEED = 2.0

    def __init__(self):
        Robot.__init__(self)

        self.__back_left_motor = self.getDevice('back_left_wheel_joint')
        self.__back_right_motor = self.getDevice('back_right_wheel_joint')
        self.__front_left_motor = self.getDevice('front_left_wheel_joint')
        self.__front_right_motor = self.getDevice('front_right_wheel_joint')

        self.__back_left_sensor = self.getDevice('back_left_wheel_joint_sensor')
        self.__back_right_sensor = self.getDevice('back_right_wheel_joint_sensor')
        self.__front_left_sensor = self.getDevice('front_left_wheel_joint_sensor')
        self.__front_right_sensor = self.getDevice('front_right_wheel_joint_sensor')
        # ds.enable(timestep)

        self.__back_left_motor.setPosition(float('inf'))
        self.__back_right_motor.setPosition(float('inf'))
        self.__front_left_motor.setPosition(float('inf'))
        self.__front_right_motor.setPosition(float('inf'))

        self.__back_left_motor.setVelocity(0)
        self.__back_right_motor.setVelocity(0)
        self.__front_left_motor.setVelocity(0)
        self.__front_right_motor.setVelocity(0)

        __target = [0.0, 0.0, 0.0]
        __speed = [0.0, 0.0, 0.0, 0.0]

    def kinematic(self):
        self.__speed[0] = 1 / self.__WHEEL_RADIUS * (self.__target[0] - self.__target[1] - (LX + LY) * self.__target[2]);
        self.__speed[1] = 1 / self.__WHEEL_RADIUS * (self.__target[0] + self.__target[1] + (LX + LY) * self.__target[2]);
        self.__speed[2] = 1 / self.__WHEEL_RADIUS * (self.__target[0] + self.__target[1] - (LX + LY) * self.__target[2]);
        self.__speed[3] = 1 / self.__WHEEL_RADIUS * (self.__target[0] - self.__target[1] + (LX + LY) * self.__target[2]);

    def stop(self):
        self.__back_left_motor.setVelocity(0)
        self.__back_right_motor.setVelocity(0)
        self.__front_left_motor.setVelocity(0)
        self.__front_right_motor.setVelocity(0)

    def forward(self):
        self.__back_left_motor.setVelocity(100.0)
        self.__back_right_motor.setVelocity(100.0)
        self.__front_left_motor.setVelocity(100.0)
        self.__front_right_motor.setVelocity(100.0)

    def backward(self):
        self.__back_left_motor.setVelocity(100.0)
        self.__back_right_motor.setVelocity(100.0)
        self.__front_left_motor.setVelocity(100.0)
        self.__front_right_motor.setVelocity(100.0)

    def left_stationary(self):
        self.__back_left_motor.setVelocity(-10.0)
        self.__back_right_motor.setVelocity(10.0)
        self.__front_left_motor.setVelocity(-10.0)
        self.__front_right_motor.setVelocity(10.0)

    def right_stationary(self):
        self.__back_left_motor.setVelocity(10.0)
        self.__back_right_motor.setVelocity(-10.0)
        self.__front_left_motor.setVelocity(10.0)
        self.__front_right_motor.setVelocity(-10.0)

    def left_sideway(self):
        self.__back_left_motor.setVelocity(-20.0)
        self.__back_right_motor.setVelocity(20.0)
        self.__front_left_motor.setVelocity(20.0)
        self.__front_right_motor.setVelocity(-20.0)

    def run(self):
        self.forward()