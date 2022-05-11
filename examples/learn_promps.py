import numpy as np
import matplotlib.pyplot as plt

from typing import List
from romi.groups import Group
from romi.trajectory import NamedTrajectory
from romi.movement_primitives import ClassicSpace, ProbabilisticMovementPrimitives, LearnTrajectory


# movement generator
def sinusoid(t, freq, phase, amplitude, dt):
    x = amplitude * np.sin(t * freq + phase) + np.random.normal() * dt * 0.02
    y = amplitude * np.cos(t * freq + phase) + np.random.normal() * dt * 0.02
    return {'x': x, 'y': y}


def plot_dataset(trajectories: List[NamedTrajectory], title="Dataset"):
    fig, axs = plt.subplots(2, 1)
    for trajectory in trajectories:
        duration = trajectory.duration
        values = trajectory.get_dict_values()
        axs[0].plot(np.cumsum(duration), values["x"])
        axs[1].plot(np.cumsum(duration), values["y"])

    axs[0].set_ylabel("x")
    axs[1].set_ylabel("y")
    axs[1].set_xlabel("t")
    plt.suptitle(title)
    plt.show()


####################
# Generate Dataset #
####################


duration = 5
n_samples = 50
dt = duration/n_samples
dataset = []
for i in range(10):
    trajectory = NamedTrajectory("x", "y")
    freq = np.random.normal(1., 0.1)
    phase = np.random.normal(0.1, 0.1)
    amplitude = np.random.normal(0.1, 0.1)
    for t in np.linspace(0, duration, n_samples):
        trajectory.notify(dt, **sinusoid(t, freq, phase, amplitude, dt))
    dataset.append(trajectory)

#####################
# Visualize Dataset #
#####################


plot_dataset(dataset)


#####################
# Learn ProMPs      #
#####################


xy_group = Group("2D space", ["x", "y"])
space = ClassicSpace(xy_group, n_features=10)

movement_primitives = []
for trajectory in dataset:
    movement_primitives.append(LearnTrajectory(space, trajectory))

promps = ProbabilisticMovementPrimitives(space, movement_primitives)


#######################
# Generate Movements  #
#######################
new_dataset = []
for _ in range(20):
    mp = promps.sample_movement()
    new_dataset.append(mp.get_full_trajectory(10, 5))

########################
# Visualize Movements  #
########################

plot_dataset(new_dataset, title="Samples from ProMPs")





