#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    rospy.init_node('publisher1')
    pub = rospy.Publisher('/topic1', String, queue_size=10)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        pub.publish("Hello from Publisher 1")
        rate.sleep()
