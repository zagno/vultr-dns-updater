import requests
import re

class ExternalIPService(object):
    def get(self):
        response = requests.get('http://checkip.dyndns.org:8245/')

        html = response.content.decode('utf-8')

        external_ip = re.findall('[0-9.]+', html)[0]

        return external_ip
