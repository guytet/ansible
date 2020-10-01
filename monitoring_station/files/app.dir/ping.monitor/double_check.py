#!/usr/bin/env python

import time,os
from post_to_slack import post_to_slack

"""
 accepts host values from ping.monitor.py that did not repsond to ping,
 and do not exist in' downed_hosts_dict'
 waits n seconds as defined in time.sleep(), re-pings, if fails -
 calls post_to_slack and passes host values with the required body text. 
"""

def double_check( pinged_host_name, pinged_host_ip ):
 time.sleep(240)                                 # wait to exclude reboot in process, before alerting
 result = os.system('ping -c1 "{1}" > /dev/null 2>&1'.format(pinged_host_name, pinged_host_ip))

 if result !=0:
  post_to_slack(pinged_host_name, pinged_host_ip, text_body)

text_body = '''
does not echo reply to ping request, 
ping checks on this host are now disabled for 30 minutes
'''
