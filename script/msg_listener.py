#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import rospy
from std_msgs.msg import String

def callback(data):
    print( data.data )
    
def main():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", String, callback)
    rospy.spin()
        
if __name__ == '__main__':
    main()
