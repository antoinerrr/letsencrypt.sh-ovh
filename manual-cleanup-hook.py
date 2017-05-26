#!/usr/bin/env python
import ovh
import os

# Fix Python 2.x.
try:
    input = raw_input
except NameError:
    pass

id_record = os.environ['CERTBOT_AUTH_OUTPUT']
client = ovh.Client()
ndd = os.environ['CERTBOT_DOMAIN']
ndd = ndd.split(".")
basedomain = ndd[len(ndd)-2] + "." + ndd[len(ndd)-1]
client.delete('/domain/zone/%s/record/%s' % (basedomain, id_record))
client.post('/domain/zone/%s/refresh' % basedomain)
