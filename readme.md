# Use Vultr's DNS as a dynamic dns service


- `pip3 install coloredlogs`
- `./vultr-dns-updater.py {api_key} {domain} {host}`


```bash
usage: vultr-dns-updater.py [-h] [-v] api_key domain host

Update Vultr DNS

positional arguments:
  api_key        Vultr API Key or Token
  domain         A Domain
  host           The Host to update

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Display extra info
```
