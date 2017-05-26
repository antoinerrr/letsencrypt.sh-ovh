#!/usr/bin/env python
import sys
import time
import ovh
import os

# Fix Python 2.x.
try:
    input = raw_input
except NameError:
    pass

target = open('.id_temp', 'r')
id_record = target.read()
client = ovh.Client()
ndd = os.environ['CERTBOT_DOMAIN']
ndd = ndd.split(".")
basedomain = ndd[len(ndd)-2] + "." + ndd[len(ndd)-1]
client.delete('/domain/zone/%s/record/%s' % (basedomain, id_record))
client.post('/domain/zone/%s/refresh' % basedomain)
