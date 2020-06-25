#!/usr/bin/env python3

##
#
# A simple controller which publishes to the cmd_vel topic
#
##

import rospy
from geometry_msgs.msg import Twist

# The topic we'll use to control the robot
command_topic = '/cmd_vel'

try:
    # Initialize node and publisher
    rospy.init_node('simple_driver', anonymous=True)
    controller = rospy.Publisher(command_topic, Twist, queue_size=10)
    hz = 10  # refresh rate in Hz
    rate = rospy.Rate(hz)

    cmd_vel = Twist()

    while not rospy.is_shutdown():

        #############################################
        # Change this part to get different behavior
        #############################################

        # set the forward velocity to 1.0 m/s
        cmd_vel.linear.x = 1.0

        #############################################
       
        controller.publish(cmd_vel)
        rate.sleep()

except rospy.ROSInterruptException:
    # Quit gracefully with ^C
    pass

