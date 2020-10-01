#!/usr/bin/env python

import pycurl,json

# posts text to slack

def post_to_slack(hostname, IPaddr, text_body):
    c=pycurl.Curl()
    c.setopt(pycurl.URL,'https://hooks.slack.com/services/API_OR_OTHER_TOKEN_HERE')
    c.setopt(pycurl.HTTPHEADER,['Accept:application/json'])
    data=json.dumps({"text":"`%s` ipaddr `%s`: %s" % (hostname, IPaddr, text_body) })
    c.setopt(pycurl.POST,1)
    c.setopt(pycurl.POSTFIELDS,data)
    c.perform()
    c.close()

