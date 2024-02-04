#!/usr/bin/env python3
import rospy

from std_msgs.msg import Float64

import sys, select, termios, tty

msg =  """
Control Your Toy!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .
   ;    '    -
q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%
space key, k : force stop
anything else : stop smoothly
CTRL-C to quit

"""

moveBindings = {
        'i':(1,0),
        'o':(1,-1),
        'j':(0,1),
        'l':(0,-1),
        'u':(1,1),
        ',':(-1,0),
        '.':(-1,1),
        'm':(-1,-1),
           }

speedBindings={
        'q':(1.1,1.1),
        'z':(.9,.9),
        'w':(1.1,1),
        'x':(.9,1),
        'e':(1,1.1),
        'c':(1,.9),
          }

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

speed = 10
turn = 1

def vels(speed,turn):
    return "currently:\tspeed %s\tturn %s " % (speed,turn)

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)
    
    rospy.init_node('turtlebot_teleop')

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
    
    x = 0
    th = 0
    status = 0
    count = 0
    acc = 0.1
    target_speed = 0
    target_turn = 0
    control_speed = 0
    control_turn = 0
    try:
        print (msg)
        while(1):
            key = getKey()
            if key == 'q': 
                pub_j1.publish(2.0)
                print("j1 = 2.0")
            elif key == 'a':
                pub_j1.publish(-2.0)
                print("j1 = -2.0")
            elif key == 'w':
                pub_j2.publish(4.0)
                print("j2 = 4.0")
            elif key == 's':
                pub_j2.publish(-4.0)
                print("j2 = -4.0")
            elif key == 'e':
                pub_j3.publish(3.0)
                print("j3 = 3.0")
            elif key == 'd':
                pub_j3.publish(-3.0)
                print("j3 = -3.0")
            elif key == 'r':
                pub_j4.publish(5.0)
                print("j4 = 5.0")
            elif key == 'f':
                pub_j4.publish(-5.0)
                print("j4 = -5.0")
            elif key == 't':
                pub_j5.publish(6.0)
                print("j5 = 6.0")
            elif key == 'g':
                pub_j5.publish(-6.0)
                print("j5 = -6.0")
            elif key == 'y':
                pub_j6.publish(7.0)
                print("j6 = 7.0")
            elif key == 'h':
                pub_j6.publish(-7.0)
                print("j6 = -7.0")
            elif key == 'u':
                pub_j7.publish(8.7)
                print("j7 = 8.7")
            elif key == 'j':
                pub_j7.publish(-8.7)
                print("j7 = -8.7")
            elif key == 'i':
                pub_j8.publish(7.8)
                print("j8 = 7.8")
            elif key == 'k':
                pub_j8.publish(-7.8)
                print("j8 = -7.8")
            elif key == 'o':
                pub_j9.publish(8.9)
                print("j9 = 8.9")
            elif key == 'l':
                pub_j9.publish(-8.9)
                print("j9 = -8.9")
            elif key == 'p':
                pub_j10.publish(2.5)
                print("j10 = 2.5")
            elif key == ';' :
                pub_j10.publish(-2.5)
                print("j10 = -2.5")
            elif key == '[':
                pub_g1l.publish(5.6)
                print("g1l = 5.6")
            elif key == '/':
                pub_g1l.publish(-5.6)
                print("g1l = -5.6")
            elif key == ']':
                pub_g2l.publish(5.4)
                print("g2l = 5.4")
            elif key == '=':
                pub_g2l.publish(-5.4)
                print("g2l = -5.4")
            # else:
            #     pub_j1.publish(0.0)
            #     pub_j2.publish(0.0)
            #     pub_j3.publish(0.0)
            #     pub_j4.publish(0.0)
            #     pub_j5.publish(0.0)
            #     pub_j6.publish(0.0)
            #     pub_j7.publish(0.0)
            #     pub_j8.publish(0.0)
            #     pub_j9.publish(0.0)
            #     pub_j10.publish(0.0)
            #     pub_g1l.publish(0.0)
            #     pub_g2l.publish(0.0)


               
            # if key in moveBindings.keys():
            #     x = moveBindings[key][0]
            #     th = moveBindings[key][1]
            #     count = 0
            # elif key in speedBindings.keys():
            #     speed = speed * speedBindings[key][0]
            #     turn = turn * speedBindings[key][1]
            #     count = 0

            #     print(vels(speed,turn))
            #     if (status == 14):
            #         print(msg)
            #     status = (status + 1) % 15
            # elif key == ' ' or key == 'k' :
            #     x = 0
            #     th = 0
            #     control_speed = 0
            #     control_turn = 0
            # else:
            #     count = count + 1
            #     if count > 4:
            #         x = 0
            #         th = 0
            #     if (key == '\x03'):
            #         break

            # target_speed = speed * x
            # target_turn = turn * th

            # if target_speed > control_speed:
            #     control_speed = min( target_speed, control_speed + 0.02 )
            # elif target_speed < control_speed:
            #     control_speed = max( target_speed, control_speed - 0.02 )
            # else:
            #     control_speed = target_speed

            # if target_turn > control_turn:
            #     control_turn = min( target_turn, control_turn + 0.1 )
            # elif target_turn < control_turn:
            #     control_turn = max( target_turn, control_turn - 0.1 )
            # else:
            #     control_turn = target_turn

            # pub_right.publish(control_turn) # publish the turn command.
            # pub_left.publish(control_turn) # publish the turn command.
            # pub_move.publish(control_speed) # publish the control speed. 


    except:
        print(e)

    finally:
        pub_j1.publish(control_turn)
        pub_j2.publish(control_turn)
        pub_j3.publish(control_turn)
        pub_j4.publish(control_turn)
        pub_j5.publish(control_turn)
        pub_j6.publish(control_turn)
        pub_j7.publish(control_turn)
        pub_j8.publish(control_turn)
        pub_j9.publish(control_turn)
        pub_j10.publish(control_turn)
        pub_g1l.publish(control_turn)
        pub_g2l.publish(control_turn)
       

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
