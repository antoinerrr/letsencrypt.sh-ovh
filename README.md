# letsencrypt.sh-ovh

This script is intented to be used as hook for official letsencrypt certbot.

It's is inspired (a lot) from the work of https://ungeek.fr/letsencrypt-api-ovh/ who made it for dehydrated acme client.

## Requirements

- Python
- Curl
- OVH Python library ``pip install ovh``

## Setup

1) Get OVH API keys

See https://api.ovh.com/createToken/ and fill in `ovh.conf` with data received (copy it from demo sample before)


## Usage

Check certbot docs for it but you will need at least the following params:

```
--preferred-challenge dns --manual --manual-auth-hook ./manual-auth-hook.py --manual-cleanup-hook ./manual-cleanup-hook.py

```
