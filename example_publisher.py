#!/usr/bin/env python3


import rospy
from std_msgs.msg import String


if __name__=="__main__":
    rospy.init_node("first_publisher_node")
    pub=rospy.Publisher('helloworld', String, queue_size=10)
    rate=rospy.Rate(30)
    while True:
        str = "hello_pub : %s " % rospy.get_time()
        pub.publish(str)
        rate.sleep()

