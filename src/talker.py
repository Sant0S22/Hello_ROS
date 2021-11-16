#!/usr/bin/env python  Obbligatoria perchè dichiara che sarà eseguito come script python

# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy #Import per scrivere nodo in python
from std_msgs.msg import String #Utilizzi un tipo di messaggio già creato che contiene stringa

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10) 
    # Chatter sarà il nome del topic , String il tipo di messaggio (è quella dei std_sgs) 
    # e queuesize il limite max di messaggi prima di essere cancellato se nessuno lo legge
    rospy.init_node('talker', anonymous=True)
    # Dichiara il nome del nodo al master , fino ad allora non comunica ancora con il master
    # Con anonymous vengono aggiunti numeri alla fine del nome che lo rendono unico
    rate = rospy.Rate(10) # 10hz
    # Indica il ratio di invio messaggi in 1 minuto combinato con sleep
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        # 3 funionalità , scrive su schermo , scrive nei log del nodo e scrive su rosout 
        pub.publish(hello_str)
        # Pubblica la stringa sul topic e con lo sleep aspetta i minuti per poi ritrasmettere
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
