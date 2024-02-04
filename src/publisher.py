#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Float64

def talker():
    pub_j1 = rospy.Publisher('/third_assembly/j1/command', Float64, queue_size=10) 
    pub_j2 = rospy.Publisher('/third_assembly/j2/command', Float64, queue_size=10) 
    pub_j3 = rospy.Publisher('/third_assembly/j3/command', Float64, queue_size=10) 
    pub_j4 = rospy.Publisher('/third_assembly/j4/command', Float64, queue_size=10)
    pub_j5 = rospy.Publisher('/third_assembly/j5/command', Float64, queue_size=10)
    pub_j6 = rospy.Publisher('/third_assembly/j6/command', Float64, queue_size=10)
    pub_j7 = rospy.Publisher('/third_assembly/j7/command', Float64, queue_size=10)
    pub_j8 = rospy.Publisher('/third_assembly/j8/command', Float64, queue_size=10)
    pub_j9 = rospy.Publisher('/third_assembly/j9/command', Float64, queue_size=10)
    pub_j10 = rospy.Publisher('/third_assembly/j10/command', Float64, queue_size=10)
    pub_g1l = rospy.Publisher('/third_assembly/g1l/command', Float64, queue_size=10)
    pub_g2l = rospy.Publisher('/third_assembly/g2l/command', Float64, queue_size=10)
    
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub_j1.publish(2.0)
        pub_j2.publish(2.0)
        pub_j3.publish(2.0)
        pub_j4.publish(2.0)
        pub_j6.publish(2.0)
        pub_j7.publish(2.0)
        pub_j8.publish(2.0)
        pub_j9.publish(2.0)
        pub_j10.publish(2.0)
        pub_g1l.publish(2.0)
        pub_g2l.publish(2.0)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass