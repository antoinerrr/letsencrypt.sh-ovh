# letsencrypt.sh-ovh

This script is intented to be used as hook for official letsencrypt certbot.

It's is inspired (a lot) from the work of https://ungeek.fr/letsencrypt-api-ovh/ who made it for dehydrated acme client.

## Requirements

- Python
- Curl
- OVH Python library ``pip install ovh``

## Setup

1) Get OVH API keys

See https://api.ovh.com/createToken/ and fill in `ovh.conf` with data received (copy it from demo sample before).  

You can leave the configuration file in the repository directory. But for using the hook scripts outside of the letsencrypt.sh-ovh directory, it could be better to move it to one of the the following locations:
- `/etc/ovh.conf`
- `~/.ovh.conf`


## Usage

Check certbot docs for it but you will need at least the following params:

```
--preferred-challenge dns --manual --manual-auth-hook ./manual-auth-hook.py --manual-cleanup-hook ./manual-cleanup-hook.py

```

## Potential issues
Dns updates can take up to 24 hours to propagate. Actually, in most cases it will take a few seconds.  
By default, the auth hook waits 10 seconds for the dns update. If this time is insufficient, you can increase it by setting a `CERTBOT_OVH_SLEEPTIME` environment variable with the intended delay:
```bash
export CERTBOT_OVH_SLEEPTIME=30
```
