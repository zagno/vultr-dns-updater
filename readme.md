# Use Vultr's DNS as a dynamic dns service

### Pull and run docker image
- `docker pull zagno/vultr_dns_updater`
- `docker run zagno/vultr_dns_updater 32FSH7FDFL9 example.com www`

### Build and run docker image
- `docker build -t vultr_dns_updater  .`
- `docker run vultr_dns_updater 32FSH7FDFL9 example.com www`

### Plain old python
- `pip3 install -r requirements.txt`
- `./vultr-dns-updater.py 32FSH7FDFL9 example.com www`

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
