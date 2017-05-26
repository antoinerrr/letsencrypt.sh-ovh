#!/usr/bin/env python
import sys
import time
import ovh

# Fix Python 2.x.
try:
    input = raw_input
except NameError:
    pass

target = open('.id_temp', 'r')
id_record = target.read()
client = ovh.Client()
ndd = sys.argv[2]
ndd = ndd.split(".")
basedomain = ndd[len(ndd)-2] + "." + ndd[len(ndd)-1]
client.delete('/domain/zone/%s/record/%s' % (basedomain, id_record))
client.post('/domain/zone/%s/refresh' % basedomain)
