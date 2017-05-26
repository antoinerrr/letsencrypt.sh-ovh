#!/usr/bin/env python
import sys
import time
import ovh

# Fix Python 2.x.
try:
    input = raw_input
except NameError:
    pass

token = "\"" + sys.argv[4] + "\""
ndd = sys.argv[2]
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
target = open('.id_temp', 'w')
target.truncate()
target.write(str(id_record["id"]))
target.close()
client.post('/domain/zone/%s/refresh' % basedomain)
time.sleep(60)
