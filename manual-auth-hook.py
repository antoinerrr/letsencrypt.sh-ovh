#!/usr/bin/env python
import time
import ovh
import os

# Fix Python 2.x.
try:
    input = raw_input
except NameError:
    pass

ndd = os.environ['CERTBOT_DOMAIN']
token = "\"" +  os.environ['CERTBOT_VALIDATION'] + "\""

ndd = ndd.split(".")
basedomain = ndd[len(ndd)-2] + "." + ndd[len(ndd)-1]
subdomain = "_acme-challenge"
if len(ndd) > 2:
    subdomain += "."
    for i in range(0, len(ndd)-2):
        if i == len(ndd)-3:
            subdomain += ndd[i]
        else:
            subdomain += ndd[i] + "."
client = ovh.Client()
id_record = client.post('/domain/zone/%s/record' % basedomain,
                        fieldType="TXT",
                        subDomain=subdomain,
                        ttl=0,
                        target=token)
print (str(id_record["id"]))
client.post('/domain/zone/%s/refresh' % basedomain)
# This is needed to allow for enough time to let the record propagate
# Don't hesitate to manually increase this value to be well over your record TTL
time.sleep(120)
