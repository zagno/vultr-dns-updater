import requests
import re

class ExternalIPService(object):
    def __init__(self, logger):
        self.logger = logger

    def get(self):

        response = requests.get('http://checkip.dyndns.org:8245/')

        html = response.content.decode('utf-8')

        external_ip = re.findall('[0-9.]+', html)[0]

        self.logger.info('External IP address is {}'.format(external_ip))

        return external_ip
