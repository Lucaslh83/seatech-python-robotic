"""my_controller controller."""
from smash import smash

destroyer = smash()
timestep = int(destroyer.getBasicTimeStep())

while destroyer.step(timestep) != -1:
    destroyer.run()
