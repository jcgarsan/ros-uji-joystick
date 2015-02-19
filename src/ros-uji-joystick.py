import pygame
import sys
import time

pygame.init()
pygame.joystick.init()

print pygame.joystick.get_count()
_joystick = pygame.joystick.Joystick(0)
_joystick.init()

clock = pygame.time.Clock()

print _joystick.get_init()
print _joystick.get_id()
print _joystick.get_name()		#Logitech Logitech Extreme 3D
print _joystick.get_numaxes()
print _joystick.get_numballs()
print _joystick.get_numbuttons()
print _joystick.get_numhats()
#	print _joystick.get_hat(0)


while 1:
    for event in pygame.event.get(): # User did something
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
        if event.type == pygame.JOYAXISMOTION:
            print("Joystick JOYAXISMOTION.")

	print _joystick.get_axis(0)
	print _joystick.get_button(0)

	buttons = _joystick.get_numbuttons()
	for i in range(buttons):
		button = _joystick.get_button(i)
		print "Button {:>2} value: {}".format(i,button)

	axes = _joystick.get_numaxes()
	print "Number of axes: {}".format(axes)

	for i in range( axes ):
		axis = _joystick.get_axis( i )
		print "Axis {} value: {:>6.3f}".format(i, axis)


#	clock.tick(20)



