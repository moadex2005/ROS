#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

def circle_motion():
    rospy.init_node('circle_motion', anonymous=True)

    vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)


    status_pub = rospy.Publisher('/turtle_status', String, queue_size=10)

    rate = rospy.Rate(10) 

    vel_msg = Twist()
    vel_msg.linear.x = 1.0     
    vel_msg.angular.z = 1.0    

    while not rospy.is_shutdown():
        vel_pub.publish(vel_msg)

        status_msg = String()
        status_msg.data = "rotating"
        status_pub.publish(status_msg)

        rate.sleep()

if __name__ == '__main__':
    try:
        circle_motion()
    except rospy.ROSInterruptException:
        pass
