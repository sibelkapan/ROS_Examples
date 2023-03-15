#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import sys

robot_x = 0.0

def pose_callback(pose):
	global robot_x
	rospy.loginfo("Robot x = %f\n", pose.x)
	robot_x = pose.x

def turtle_circle(linear_velocity, angle, distance):

	global robot_x

	rospy.init_node('turtlesim', anonymous=True)
	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	
	rate = rospy.Rate(10)

	vel = Twist()
	while not rospy.is_shutdown():
		vel.linear.x = linear_velocity
		vel.linear.y = 0
		vel.linear.z = 0
		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = angle
		
		if(robot_x >= distance):
			rospy.loginfo("Robot reached the destination")
			rospy.logwarn("stopting robot")
			break
		#rospy.loginfo("Radius = %f", radius)
		pub.publish(vel)
		rate.sleep()

if __name__ == '__main__':
	try:
		turtle_circle(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
	except rospy.ROSInterruptException:
		pass