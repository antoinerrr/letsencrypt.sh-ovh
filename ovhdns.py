#!/usr/bin/env python
import sys
import time
import ovh

# Fix Python 2.x.
try:
    input = raw_input
except NameError:
    pass

if len(sys.argv) == 2:
    if sys.argv[1] == "--init":
        client = ovh.Client()
        ck = client.new_consumer_key_request()
        ck.add_recursive_rules(ovh.API_READ_WRITE, "/domain")
        validation = ck.request()
        print("LINK: %s" % validation['validationUrl'])
        input("Press Enter when it's done...")
        print("ConsumerKey: %s" % validation['consumerKey'])
    else:
        print("Try --init to get started")
elif len(sys.argv) == 5:
    if sys.argv[1] == "deploy_challenge":
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
    elif sys.argv[1] == "clean_challenge":
        target = open('.id_temp', 'r')
        id_record = target.read()
        client = ovh.Client()
        ndd = sys.argv[2]
        ndd = ndd.split(".")
        basedomain = ndd[len(ndd)-2] + "." + ndd[len(ndd)-1]
        client.delete('/domain/zone/%s/record/%s' % (basedomain, id_record))
        client.post('/domain/zone/%s/refresh' % basedomain)
    else:
        print("Unknow action")
