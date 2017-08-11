class DNSUpdaterService(object):
    def __init__(self, api, external_ip_service, logger):
        self.api = api
        self.external_ip_service = external_ip_service
        self.logger = logger

    def update(self, host):
        external_ip_address = self.external_ip_service.get()
        record              = self.api.dns.find_subdomain(host)

        if external_ip_address == record['data']:
            self.logger.info('External IP has not changed')

            return

        self.logger.info('Updating External IP Address')

        response = self.api.dns.post(record, external_ip_address)
