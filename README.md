The DISCOVER lab startup package. ~~Everything you need to know~~ A few helpful things to get started with undergraduate research.

## Prerequisits

- Ubuntu 16.04
- ROS Kinetic, with stage simulator
- Python

## Quick Start

Follow these instructions if you are already quite familiar with the ROS ecosystem. Otherwise, take a look at the wiki. 

- Fork or clone this repository, and put in your `~/catkin_ws/src`.
- Run `roslaunch discoverlab_startup start_stage_simulator` to start a simple simulator.
- Move the robot manually with `rosrun teleop_twist_keyboard teleop_twist_keyboard.py`.
- Run a script (`src/simple_driver.py`) to move the robot with `rosrun discoverlab_startup simple_driver.py`.

