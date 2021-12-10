#! /usr/bin/env python3

import rospy
from std_msgs.msg import String

def called(msg):
    rospy.loginfo("%s ", msg.data)


if __name__=="__main__":
    rospy.init_node("first_subscriber_node")
    sub=rospy.Subscriber('helloworld', String, callback=called)
    rate=rospy.spin()


