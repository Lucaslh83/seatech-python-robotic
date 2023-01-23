"""my_controller controller."""

from smash import Smash

destroyer = Smash()
timestep = int(destroyer.getBasicTimeStep())

while destroyer.step(timestep) != -1:
    destroyer.run()
