#!/usr/bin/env python
import sys,tty,termios
import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt16


msg = """
Control Servo
--------------
Movimiento:
        w: 0 grados
        s: 45 grados
        a: 90 grados
	d: 180 grados
	q: to quit
"""

def obtenerTecla():
	fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
		tty.setraw(sys.stdin.fileno())
                letra = sys.stdin.read(1)
        finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return letra

def function():
	sub = rospy.Publisher('/servo_control', UInt16, queue_size=10)
	rospy.init_node('control_talker', anonymous=True)
	rate = rospy.Rate(10)
	print(msg)
	while not rospy.is_shutdown():
		letra = obtenerTecla()		
		if (letra=='w'):
			position = 0
		if (letra=='s'):
			position = 45
		if (letra=='a'):
			position = 90
		if (letra=='d'):
			position = 180
		if (letra =='q'):
			break;
		
		sub.publish(position)
		rate.sleep()
		
if __name__ == '__main__':
	try:
		function()
	except rospy.ROSInterruptException:
		pass
