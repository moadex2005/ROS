#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("Turtle status: %s", msg.data)

def listener():
    rospy.init_node('status_listener', anonymous=True)
    rospy.Subscriber('/turtle_status', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
