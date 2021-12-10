#! /usr/bin/env python3

import rospy
from std_msgs.msg import String
import message_filters

def called(msg):
    rospy.loginfo("%s ", msg.data)
def called2(msg):
    rospy.loginfo("%s ", msg.data)

if __name__=="__main__":
    rospy.init_node("first_subscriber_node")
    sub=rospy.Subscriber('helloworld', String, callback=called)
    # rate=rospy.spin()
    sub=rospy.Subscriber('helloworld02', String, callback=called2)
    rate=rospy.spin()

    # rospy.init_node("first_subscriber_node")
    # info_sub = message_filters.Subscriber('helloworld', String, callback=called)
    # pose_sub = message_filters.Subscriber('helloworld02', String, callback=called2)

    # ts = message_filters.TimeSynchronizer([info_sub, pose_sub], 10)
    # ts.registerCallback(called)
    # rospy.spin()



 