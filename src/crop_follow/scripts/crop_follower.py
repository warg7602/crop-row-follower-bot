#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def crop_follower():
    rospy.init_node('crop_follower', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)

    # Create a Twist message to move the robot forward
    move_cmd = Twist()
    while not rospy.is_shutdown():
        move_cmd.linear.x = 0.5  # Move forward
        move_cmd.angular.z = 0.0  # No turning
        pub.publish(move_cmd)
        rate.sleep()

if __name__ == '__main__':
    try:
        crop_follower()
    except rospy.ROSInterruptException:
        pass
