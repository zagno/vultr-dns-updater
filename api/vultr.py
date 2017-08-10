import requests
from requests.auth import HTTPBasicAuth
from threading import Thread
from pprint import pprint

class VultrBaseAPI(object):
    def __init__(self, api_key, domain, logger):
        self.api_url = 'https://api.vultr.com'
        self.domain  = domain
        self.api_key = api_key
        self.logger  = logger

    def _get(self, uri):
        try:
            url = '{}{}'.format(self.api_url, uri)

            self.logger.debug('GET {}'.format(url))

            return requests.get(
                url,
                headers={'API-Key': self.api_key}
            ).json()
        except Exception as e:
            return None

    def _post(self, uri, payload = None):
        try:
            url = '{}{}'.format(self.api_url, uri)

            self.logger.debug('POST {}'.format(url))

            print(payload)

            return requests.post(
                url,
                headers={'API-Key': self.api_key},
                data=payload
            )
        except Exception:
            return None

    def get_rack_name(self):
        return self.rack

class VultrDns(VultrBaseAPI):
    def __init__(self, api_key, domain, logger):
        super().__init__(api_key, domain, logger)

    def get(self):
        return self._get('/v1/dns/records?domain={}'.format(self.domain))

    def find_subdomain(self, name):
        records = self.get()

        for record in records:
            if record['type'] != 'A':
                continue

            if record['name'] == name:
                return record

        return none

    def post(self, record, data):
        record['data'] = data
        record['domain'] = self.domain

        return self._post('/v1/dns/update_record', record)

class VultrAPI(VultrBaseAPI):
    def __init__(self, api_key, domain, logger):
        super().__init__(api_key, domain, logger)

        self.dns = VultrDns(api_key, domain, logger)

    def dns(self, name):
        return self.dns
