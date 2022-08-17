#!/usr/bin/env python

import rospy
from std_msgs.msg import UInt16

def talker():
    sub = rospy.Publisher('/servo_control', UInt16, queue_size=10)
    rospy.init_node('control_talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    rospy.loginfo("Estoy publicando en el servo_control")
    while not rospy.is_shutdown():
	position = 90 
        sub.publish(position)
        rospy.loginfo("%f", position)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
