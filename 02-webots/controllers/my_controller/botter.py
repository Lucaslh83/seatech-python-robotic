class botter():
    def __init__(self,robot):
        timestep = int(robot.getBasicTimeStep())

        self._back_left_motor = robot.getDevice('back_left_wheel_joint')
        self._back_right_motor = robot.getDevice('back_right_wheel_joint')
        self._front_left_motor = robot.getDevice('front_left_wheel_joint')
        self._front_right_motor = robot.getDevice('front_right_wheel_joint')

        self._back_left_motor.setPosition(float('inf'))
        self._back_right_motor.setPosition(float('inf'))
        self._front_left_motor.setPosition(float('inf'))
        self._front_right_motor.setPosition(float('inf'))

        self._back_left_motor.setVelocity(0)
        self._back_right_motor.setVelocity(0)
        self._front_left_motor.setVelocity(0)
        self._front_right_motor.setVelocity(0)