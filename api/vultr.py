import requests

from .exception import VultrAPIException

class VultrBaseAPI(object):
    def __init__(self, api_key, domain, logger):
        self.api_url = 'https://api.vultr.com'
        self.domain  = domain
        self.api_key = api_key
        self.logger  = logger

    def _get(self, uri):

        url = '{}{}'.format(self.api_url, uri)

        self.logger.debug('GET {}'.format(url))

        response = requests.get(
            url,
            headers={'API-Key': self.api_key}
        )

        if response.status_code >= 400:
            raise VultrAPIException(response.status_code)

        return response

    def _post(self, uri, payload = None):

        url = '{}{}'.format(self.api_url, uri)

        self.logger.debug('POST {}'.format(url))

        response = requests.post(
            url,
            headers={'API-Key': self.api_key},
            data=payload
        )

        if response.status_code >= 400:
            raise VultrAPIException(response.status_code)

        return response

class VultrDns(VultrBaseAPI):
    def __init__(self, api_key, domain, logger):
        super().__init__(api_key, domain, logger)

    def get(self):
        return self._get('/v1/dns/records?domain={}'.format(self.domain)).json()

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

        return self._post('/v1/dns/update_record', record).json()

class VultrAPI(VultrBaseAPI):
    def __init__(self, api_key, domain, logger):
        super().__init__(api_key, domain, logger)

        self.dns = VultrDns(api_key, domain, logger)

    def dns(self, name):
        return self.dns
