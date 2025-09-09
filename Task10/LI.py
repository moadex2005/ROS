#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan
import numpy as np

def callback(scan_msg):
    ranges = np.array(scan_msg.ranges)
    ranges = ranges[np.isfinite(ranges)]
    if len(ranges) > 0:
        closest = np.min(ranges)
        rospy.loginfo("%.2f" % closest)
    else:
        rospy.loginfo("inf")

def listener():
    rospy.init_node('lidar_listener', anonymous=True)
    rospy.Subscriber('/scan', LaserScan, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
