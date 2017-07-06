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

2) Validate the API token and set its capacities

In the same directory as ovh.conf, run:

$ python ovhdns.py /domain/zone/example.com

This will prompt you with an URL where you will need to input your OVH account and password to enable the API token. 

The optional string given as parameter defines the Read-Write access granted to the token. /domain gives access to all DNS domains under this OVN account.
You can use /domain/zone/example.com to limit it to your example.com domain.
If no parameters are given, the script defaults to /domain (BE SURE THIS IS OK FOR YOUR USECASE.)

## Usage

Check certbot docs for it but you will need at least the following params:

```
--manual --manual-auth-hook ./manual-auth-hook.py --manual-cleanup-hook ./manual-cleanup-hook.py

```
