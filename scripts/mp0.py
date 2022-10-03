#!/usr/bin/env python3

#==============================================================================
# File name          : mp0.py                                                                 
# Description        : MP0 for CS588                                                                                                                        
# Usage              : rosrun mp0 mp0.py                                                                                                                           
#==============================================================================
from __future__ import print_function

#Python Headers
import math
import os

# ROS Headers
import rospy

# GEM PACMod Headers
from std_msgs.msg import Header
from pacmod_msgs.msg import PacmodCmd, PositionWithSpeed, VehicleSpeedRpt

class Node():

	def __init__(self):

		self.rate = rospy.Rate(10)

		self.turn_pub = rospy.Publisher('/pacmod/as_rx/turn_cmd', PacmodCmd, queue_size = 1)
		# self.turn_cmd = PositionWithSpeed()
		self.turn_cmd = PacmodCmd()
		self.turn_cmd.ui16_cmd = 1
		# 2 turns left
		# 1 turns it off
		# 0 turns right

	def blinkLeft(self):
		counter = 0
		while not rospy.is_shutdown() and counter < 75000:

			# self.turn_pub.publish(self.turn_cmd)
			self.turn_cmd.ui16_cmd = 2
			self.turn_pub.publish(self.turn_cmd)
			self.rate.sleep
			counter +=1 
			print(counter)

		self.turn_cmd.ui16_cmd = 1
		self.turn_pub.publish(self.turn_cmd)
		self.rate.sleep

	def blinkRight(self):
		counter = 0
		while not rospy.is_shutdown() and counter < 75000:

			# self.turn_pub.publish(self.turn_cmd)
			self.turn_cmd.ui16_cmd = 0
			self.turn_pub.publish(self.turn_cmd)
			self.rate.sleep
			counter +=1 
			print(counter)

		self.turn_cmd.ui16_cmd = 1
		self.turn_pub.publish(self.turn_cmd)
		self.rate.sleep



	def run(self):
		self.blinkLeft()
		self.blinkRight()
		self.blinkLeft()


if __name__ == '__main__':
	rospy.init_node('sos_node', anonymous=True)
	node = Node()
	node.run()