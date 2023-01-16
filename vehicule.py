from abc import ABCMeta, abstractmethod

class UnmannedVehicule():
    _name = "DEFAULT"

    @abstractmethod
    def do_something_interesting(self):
        """"... AS YOU CAN"""

    def rename_robot(self,name):
        self._name = name
    
    @abstractmethod
    def status(self):
        """Status of the vehicule"""

class GroundVehicule():
    _speed = 0

    def do_something_ground_specific(self):
        print("GROUND COMBAT ENGAGED")

    def choose_speed(self,speed):
        self._speed = speed
        print("Speed is " + str(self._speed) + "m/s")

class AerialVehicule():
    _height = 0

    def do_something_aerial_specific(self):
        print("AERIAL COMBAT ENGAGED")

    def choose_height(self,height):
        self._height = height

class UnderseaVehicule():
    _depth = 0

    def do_something_undersea_specific(self):
        print("UNDERSEA COMBAT ENGAGED")

    def choose_depth(self,depth):
        self._depth = depth

class UGV(UnmannedVehicule,GroundVehicule,metaclass=ABCMeta):
    def do_something_interesting(self):
        print("RIDE AS FAR AS POSSIBLE")

    def status(self):
        print("UGV name is " + self._name + " and its speed is " + str(self._speed) + "m/s")

class UAV(UnmannedVehicule,AerialVehicule,metaclass=ABCMeta):
    def do_something_interesting(self):
        print("FLY AS HIGH AS YOU CAN")

    def status(self):
        print("UAV name is " + self._name + " and its height is " + str(self._height) + "m")

class UUV(UnmannedVehicule,UnderseaVehicule,metaclass=ABCMeta):
    def do_something_interesting(self):
        print("DIVE AS DEEP AS POSSIBLE")

    def status(self):
        print("UUV name is " + self._name + " and its depth is " + str(self._depth) + "m")

if __name__ == "__main__":
    ugv = UGV()
    ugv.do_something_interesting()
    ugv.do_something_ground_specific()

    uav = UAV()
    uav.do_something_interesting()
    uav.do_something_aerial_specific()
    
    uuv = UUV()
    uuv.do_something_interesting()
    uuv.do_something_undersea_specific()