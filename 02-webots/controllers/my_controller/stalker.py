class stalker():
    def __init__(self,robot):
        timestep = int(robot.getBasicTimeStep())

        self._lidar1 = robot.getDevice('Sick S3001')
        self._lidar2 = robot.getDevice('Sick S3002')
        self._lidar1.enable(timestep)
        self._lidar2.enable(timestep)

        self._lidar1.enablePointCloud()
        self._lidar2.enablePointCloud()