cmake_minimum_required(VERSION 2.8.3)
project(ros-uji-joystick)

find_package(catkin REQUIRED
	rospy
	sensor_msgs
)

catkin_package(
  CATKIN_DEPENDS
		rospy
		sensor_msgs
)

install(PROGRAMS src/ros-uji-joystick.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

