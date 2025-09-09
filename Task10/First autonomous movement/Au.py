#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def move_forward():
    rospy.init_node('move_forward_node', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    vel_msg.linear.x = 0.1
    vel_msg.angular.z = 0.0

    duration = rospy.Duration(3)
    start_time = rospy.Time.now()

    rate = rospy.Rate(10)  
    while rospy.Time.now() - start_time < duration:
        pub.publish(vel_msg)
        rate.sleep()

    vel_msg.linear.x = 0.0
    pub.publish(vel_msg)

if __name__ == '__main__':
    try:
        move_forward()
    except rospy.ROSInterruptException:
        pass
