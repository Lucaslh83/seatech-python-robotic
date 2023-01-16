import time

class Robot():
    __name = "unnamed"
    __power = False
    __battery_level = 0
    __charging = False
    __speed = 0
    
    def __init__(self,name):
        self.__name = name

    def set_power(self,state):
        if state == "ON":
            self.__power = True
            print("Power is ON")
        elif state == "OFF":
            self.__power = False
            self.stop()
            print("Power is OFF")

    def charge(self):
        self.__charging = True
        while self.__battery_level < 100:
            time.sleep(0.01)
            self.__battery_level += 1
            print("Battery = " + str(self.__battery_level) + "%")
        self.__charging = False
    
    def set_speed(self, vit):
        if self.__power == True:
            while self.__speed != vit:
                time.sleep(0.1)
                if self.__speed < vit:
                    self.__speed += 1
                else:
                    self.__speed -= 1     
                print("Speed = " + str(self.__speed) + "km/h")

    def stop(self):
        if self.__speed > 0:
            print(self.__name + " is stopping")
        self.__speed = 0

    def get_state(self):
        print("State of " + self.__name + " : ")
        print("Power is ON")
        print("Battery = " + str(self.__battery_level) + "%")
        print("Speed = " + str(self.__speed) + "km/h")


if __name__ == "__main__":
    r = Robot(input("Name of the robot ?\n"))
    r.charge()
    r.set_power("ON")
    r.set_speed(int(input("Speed of the robot ?\n")))
    r.stop()
    r.get_state()
    r.set_power("OFF")