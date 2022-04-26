#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import rospy

def main():
    rospy.init_node("program3")
    print("program3.py 起動")
    rospy.spin()

if __name__ == '__main__':
    main()
