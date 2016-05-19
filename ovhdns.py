#!/usr/bin/python
import ovh
import sys
import time

if len(sys.argv) == 2:
  if sys.argv[1] == "--init":
    client = ovh.Client()
    ck = client.new_consumer_key_request()
    ck.add_recursive_rules(ovh.API_READ_WRITE, "/domain")
    validation = ck.request()
    print "LINK: %s" % validation['validationUrl']
    raw_input("Press Enter when it's done...")
    print "ConsumerKey: %s" % validation['consumerKey']
  else:
    print "Try --init to get started"
elif len(sys.argv) == 5:
  if sys.argv[1] == "deploy_challenge":
    token = "\"" + sys.argv[4] + "\""
    ndd = sys.argv[2]
    ndd = ndd.split(".")
    if len(ndd)==2:
      subdomain = "_acme-challenge"
      basedomain = ndd[0] + "." + ndd[1]
    else:
      subdomain = "_acme-challenge." + ndd[0]
      basedomain = ndd[1] + "." + ndd[2]
    client = ovh.Client()
    id_record = client.post('/domain/zone/%s/record' % basedomain,
                            fieldType="TXT",
                            subDomain=subdomain,
                            ttl=0,
                            target=token
                            )
    target = open('.id_temp', 'w')
    target.truncate()
    target.write(str(id_record["id"]))
    target.close()
    client.post('/domain/zone/%s/refresh' % basedomain)
    time.sleep(60)
  elif sys.argv[1] == "clean_challenge":
    target = open('.id_temp', 'r')
    id_record = target.read()
    client = ovh.Client()
    ndd = sys.argv[2]
    ndd = ndd.split(".")
    if len(ndd) == 2:
      basedomain = ndd[0] + "." + ndd[1]
    else:
      basedomain = ndd[1] + "." + ndd[2]
    client.delete('/domain/zone/%s/record/%s' % (basedomain, id_record))
    client.post('/domain/zone/%s/refresh' % basedomain)
  else:
    print "Unknow action"
