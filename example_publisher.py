#! /usr/bin/env python3


import rospy
from std_msgs.msg import String


if __name__=="__main__":
    count = 0
    rospy.init_node("first_publisher_node")
    pub=rospy.Publisher('helloworld', String, queue_size=10)
    # pub2=rospy.Publisher('helloworld02', String, queue_size=10)
    rate=rospy.Rate(30)
    while not rospy.is_shutdown():
        str = "hello publisher : %s " % rospy.get_time()
        pub.publish(str)
        count+=1
        # str2 = "hello publisher02 : %d " % count
        # pub2.publish(str2)
        # rate.sleep()

