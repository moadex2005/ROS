#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback1(msg):
    rospy.loginfo("Received from pub1: %s", msg.data)

def callback2(msg):
    rospy.loginfo("Received from pub2: %s", msg.data)

if __name__ == '__main__':
    rospy.init_node('subscriber')
    rospy.Subscriber('/topic1', String, callback1)
    rospy.Subscriber('/topic2', String, callback2)
    rospy.spin()
