#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64

def callbackj1(data):
    rospy.loginfo(rospy.get_caller_id() + "called j1 %f", data.data)
def callbackj2(data):
    rospy.loginfo(rospy.get_caller_id() + "called j2 %f", data.data)
def callbackj3(data):
    rospy.loginfo(rospy.get_caller_id() + "called j3 %f", data.data)
def callbackj4(data):
    rospy.loginfo(rospy.get_caller_id() + "called j4 %f", data.data)
def callbackj5(data):
    rospy.loginfo(rospy.get_caller_id() + "called j5 %f", data.data)
def callbackj6(data):
    rospy.loginfo(rospy.get_caller_id() + "called j6 %f", data.data)
def callbackj7(data):
    rospy.loginfo(rospy.get_caller_id() + "called j7 %f", data.data)
def callbackj8(data):
    rospy.loginfo(rospy.get_caller_id() + "called j8 %f", data.data)
def callbackj9(data):
    rospy.loginfo(rospy.get_caller_id() + "called j9 %f", data.data)
def callbackj10(data):
    rospy.loginfo(rospy.get_caller_id() + "called j10 %f", data.data)
def callbackg1l(data):
    rospy.loginfo(rospy.get_caller_id() + "called g1l %f", data.data)
def callbackg2l(data):
    rospy.loginfo(rospy.get_caller_id() + "called g2l %f", data.data)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('/third_assembly/j1/command', Float64, callbackj1) 
    rospy.Subscriber('/third_assembly/j2/command', Float64, callbackj2) 
    rospy.Subscriber('/third_assembly/j3/command', Float64, callbackj3) 
    rospy.Subscriber('/third_assembly/j4/command', Float64, callbackj4)
    rospy.Subscriber('/third_assembly/j5/command', Float64, callbackj5)
    rospy.Subscriber('/third_assembly/j6/command', Float64, callbackj6)
    rospy.Subscriber('/third_assembly/j7/command', Float64, callbackj7)
    rospy.Subscriber('/third_assembly/j8/command', Float64, callbackj8)
    rospy.Subscriber('/third_assembly/j9/command', Float64, callbackj9)
    rospy.Subscriber('/third_assembly/j10/command', Float64, callbackj10)
    rospy.Subscriber('/third_assembly/g1l/command', Float64, callbackg1l)
    rospy.Subscriber('/third_assembly/g2l/command', Float64, callbackg2l)

    

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()