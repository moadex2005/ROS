#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import math

def move_square():
    rospy.init_node("square_motion", anonymous=True)

    vel_pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    status_pub = rospy.Publisher("/motion_status", String, queue_size=10)

    rate = rospy.Rate(10)
    vel_msg = Twist()

    side_length = 2.0      
    linear_speed = 1.0     
    angular_speed = 1.0    

    for i in range(4):
        status_pub.publish("forward")
        rospy.loginfo("forward")
        vel_msg.linear.x = linear_speed
        vel_msg.angular.z = 0.0

        distance = 0
        t0 = rospy.Time.now().to_sec()
        while distance < side_length:
            vel_pub.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            distance = linear_speed * (t1 - t0)
            rate.sleep()

        status_pub.publish("rotating")
        rospy.loginfo("rotating")
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = angular_speed

        angle = 0
        t0 = rospy.Time.now().to_sec()
        while angle < math.pi/2:
            vel_pub.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            angle = angular_speed * (t1 - t0)
            rate.sleep()

    vel_msg.linear.x = 0.0
    vel_msg.angular.z = 0.0
    vel_pub.publish(vel_msg)
    status_pub.publish("stopped")
    rospy.loginfo("Square complete. Stopped.")

if __name__ == '__main__':
    try:
        move_square()
    except rospy.ROSInterruptException:
        pass
