# -*- encoding: utf-8 -*-

import ovh,sys

# create a client using configuration
client = ovh.Client()

# Request RW, /domain API access
ck = client.new_consumer_key_request()
# If the user asked for a specific API access pattern, use it
if len(sys.argv) == 2:
  ck.add_recursive_rules(ovh.API_READ_WRITE, sys.argv[1])
# or default to give access to all domains (ew.)
else:
  ck.add_recursive_rules(ovh.API_READ_WRITE, "/domain")

# Request token
validation = ck.request()

print "Please visit %s to authenticate" % validation['validationUrl']
raw_input("and press Enter to continue...")

print "Btw, your 'consumerKey' is '%s'" % validation['consumerKey']

