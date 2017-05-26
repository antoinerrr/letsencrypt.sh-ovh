# letsencrypt.sh-ovh

This script is intented to be used as hook for https://github.com/lukas2511/dehydrated script, a simple letsencrypt/acme client implemented as a shell-script.

See https://ungeek.fr/letsencrypt-api-ovh/

## Requirements

- Python
- Curl
- OVH Python library ``pip install ovh``

## Setup

1) Get OVH API keys

See https://api.ovh.com/createToken/ and fill in `ovh.conf` with data received (copy it from demo sample before)

2) Create a ``run`` script with:

```
#!/usr/bin/env bash

set -eux

cp -r src/. dist/

cd dist

curl -sL -o ovhdns.py https://raw.githubusercontent.com/antoiner77/letsencrypt.sh-ovh/master/ovhdns.py

chmod +x ovhdns.py

curl -sL -o dehydrated https://raw.githubusercontent.com/lukas2511/dehydrated/v0.4.0/dehydrated

chmod +x dehydrated

./dehydrated --register --accept-terms --hook "$(pwd)/ovhdns.py"

./dehydrated --cron --accept-terms --hook "$(pwd)/ovhdns.py"
```

Make it executable ``chmod +x ./run``

3) Create a ``src`` directory with:

- **ovh.conf** : OVH API configuration (see https://github.com/antoiner77/letsencrypt.sh-ovh/blob/master/ovh.conf.demo)
- **config** : dehydrated configuration (see https://github.com/lukas2511/dehydrated/blob/v0.4.0/docs/examples/config)
- **domains.txt** : domains you want HTTPS (see https://github.com/lukas2511/dehydrated/blob/v0.4.0/docs/examples/domains.txt)

## Usage

``./run``

Certs should be in ``./dist/{DOMAIN}/`` directory.
