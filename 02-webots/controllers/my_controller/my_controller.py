"""my_controller controller."""

from smash import Botter, Stalker

destroyer = Botter()
capt = Stalker()
timestep = int(destroyer.getBasicTimeStep())

while destroyer.step(timestep) != -1:
    destroyer.run()
