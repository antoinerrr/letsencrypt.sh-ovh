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

$ python ovhdns.py /domain/zone/_acme-challenge.example.com

This will prompt you with an URL where you will need to input your OVH account and password to enable the API token. 

The optional string given as parameter defines the Read-Write access granted to the token. /domain gives access to all DNS domains under this OVN account.
You can use /domain/zone/_acme-challenge.example.com to limit it to your example.com domain.
If no parameters are given, the script defaults to /domain (BE SURE THIS IS OK FOR YOUR USECASE.)

By default the manual-auth-hook.py script will wait for 120 seconds before allowing ACME to perform the dns challenge, this is to allow for the record to be propagated. Please lower your TTL to low enough values that the validation will not fail due no DNS caching. Don't hesitate to modify the ending "sleep(120)" line to increase the time to be well over your DNS TTL.

## Usage

Check certbot docs for it but you will need at least the following params:

```
--manual --manual-auth-hook ./manual-auth-hook.py --manual-cleanup-hook ./manual-cleanup-hook.py

```

Most people would be ok with:

```
certbot certonly -d example.com --preferred-challenges dns --manual --manual-auth-hook ./manual-auth-hook.py --manual-cleanup-hook ./manual-cleanup-hook.py

```
