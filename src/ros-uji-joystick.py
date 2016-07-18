#!/usr/bin/env python
# coding:utf8

"""
@package ros-uji-joystick
@file ros-uji-joystick.py

@brief Joystick generic driver for ROS.

@author: Juan Carlos García <garciaju@uji.es>
@date 18/02/2015
"""

import pygame
import sys
import signal
import time
import rospy
from sensor_msgs.msg import Joy

# Initialize consts and vars
joy_pub = rospy.Publisher('joystick_out', Joy, queue_size=10)
rospy.init_node('ros_uji_joystick', anonymous=True)   # Initialize node
rospy.Rate(50);
pygame.init()
pygame.joystick.init()

#Debug flag: show human-readable data on terminal
DEBUG_COLUMN = False
DEBUG_ARRAY  = True

def signal_handler(signal, frame):
	print "\nClosing the program..."
	sys.exit(0)


def main():
	joy_msg = Joy()
	joy_msg.header.stamp = rospy.Time.now()
	joyId = 0
	joyDetected = False
	quitting = False
	
	signal.signal(signal.SIGINT, signal_handler)
	clock = pygame.time.Clock()

	#Search our joystick if there is more than one
	joystick = pygame.joystick.Joystick(0)
	joystick.init()

	print "\nThere are " + str(pygame.joystick.get_count()) + " joysticks detected:"
	for i in range(pygame.joystick.get_count()):
		print str(i) + ") " + pygame.joystick.Joystick(i).get_name() 
	joyId = input("Select the joystick ID: ")

	while joyId > pygame.joystick.get_count():
		joyId = input("Select the joystick ID: ")

	joystick = pygame.joystick.Joystick(joyId)
	joystick.init()


#	while joyId <= pygame.joystick.get_count() and not joyDetected:
#		if joystick.get_name() == "Logitech Logitech Extreme 3D":
#			joyDetected = True
#			print joystick.get_name() + "joystick detected"
#		else:
#			joyId += 1
#			joystick = pygame.joystick.Joystick(joyId)
#			joystick.init()



	#Get the number of axes/numbers and initialize joy_msg
	joyAxes = joystick.get_numaxes()
	joyButtons = joystick.get_numbuttons()
	joy_msg.axes = [0.0] * joyAxes
	joy_msg.buttons = [0.0] * joyButtons
	print "\nJoystick selected: " + pygame.joystick.Joystick(joyId).get_name() 
	print "Number of axes: {}".format(joyAxes)
	print "Number of buttons: {}".format(joyButtons)

	raw_input('Press "Enter" to continue...')

	#Get the data, create the message and publish it
	while not quitting and not rospy.is_shutdown():
		try:
			pygame.event.get()

			for i in range(joyAxes):
				joy_msg.axes[i] = joystick.get_axis(i)
				if DEBUG_COLUMN:
					print "Axis {} value: {:>6.3f}".format(i, joystick.get_axis(i))
			for i in range(joyButtons):
				joy_msg.buttons[i] = joystick.get_button(i)
				if DEBUG_COLUMN:
					print "Button {:>2} value: {}".format(i, joystick.get_button(i))
			print "\n"

			#Publish the data
			joy_pub.publish(joy_msg)

			clock.tick(20)

			if DEBUG_ARRAY:
				print "Axes:"
				print joy_msg.axes
				print "Buttons:"
				print joy_msg.buttons

		except (KeyboardInterrupt, SystemExit):
			quitting = True
			print "KeyboardInterrupt detected..."

if __name__ == '__main__':
	main()

