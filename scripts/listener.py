#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt16

def callback(data):
    rospy.loginfo('Valores del sensor de temperatura: %s', data.data)

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('/sensor', UInt16, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
