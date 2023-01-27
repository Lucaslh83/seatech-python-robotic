from controller import Robot, Lidar

class Botter(Robot):

    __WHEEL_RADIUS =  0.1
    __LX = 0.238  # lateral distance from robot's COM to wheel [m].
    __LY = 0.285  # longitudinal distance from robot's COM to wheel [m].
    __speed = [0.0, 0.0, 0.0, 0.0]

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

        self.__back_left_motor.setPosition(float('inf'))
        self.__back_right_motor.setPosition(float('inf'))
        self.__front_left_motor.setPosition(float('inf'))
        self.__front_right_motor.setPosition(float('inf'))

        self.__back_left_motor.setVelocity(0)
        self.__back_right_motor.setVelocity(0)
        self.__front_left_motor.setVelocity(0)
        self.__front_right_motor.setVelocity(0)

        

    def kinematic(self, target):
        self.__speed[0] = 1 / self.__WHEEL_RADIUS * (target[0] - target[1] - (self.__LX + self.__LY) * target[2]);
        self.__speed[1] = 1 / self.__WHEEL_RADIUS * (target[0] + target[1] + (self.__LX + self.__LY) * target[2]);
        self.__speed[2] = 1 / self.__WHEEL_RADIUS * (target[0] + target[1] - (self.__LX + self.__LY) * target[2]);
        self.__speed[3] = 1 / self.__WHEEL_RADIUS * (target[0] - target[1] + (self.__LX + self.__LY) * target[2]);

        self.__back_left_motor.setVelocity(self.__speed[0])
        self.__back_right_motor.setVelocity(self.__speed[1])
        self.__front_left_motor.setVelocity(self.__speed[2])
        self.__front_right_motor.setVelocity(self.__speed[3])

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
        self.left_sideway()

class Stalker(Lidar):
    def __init__(self):
        Lidar.__init__(self)
        timestep = int(Botter.getBasicTimeStep())

        lidar1 = Robot.getLidar('Sick S3001')
        lidar2 = Robot.getLidar('Sick S3002')
        lidar1.enable(timestep)
        lidar2.enable(timestep)