#!/usr/bin/env python3

import rospy
# we are going to read/turtlesim/Pose messages here
form turtlesim.msg import Pose
# for converting sadians to degrees import math module
import math

#declare constant for the angular position scales
ROTATION_SCALE = 180.0/math.pi

def pose_callback(data):
  rot_in_degrees = data.theta * ROTATION_SCALE
  x_in_cm = data.x * 100
  y_in_cm = data.y * 100
  rospy.loginfo("x is %0.2f cm, y is %0.2f cm, theta is %0.2f degrees", x_in_cm, y_in_cm, rot_in_degrees) #loginfo alternative to print function
  
  
if __name__ == '__main__':
  #initialize the node
  rospy.init_node('pos_converter', anonymous = True)
  #add a sub to read positin info from turtle1/pos
  rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
  #spin() simply keeps python from exiting until node is stopped
  rospy.spin()
  
