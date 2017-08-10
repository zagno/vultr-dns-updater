#! /usr/bin/env python3

from service.external_ip import *
from api.vultr import *

import argparse
import coloredlogs, logging

def update_dns(api, external_ip, host):

    external_ip_address = external_ip.get()

    record     = api.dns.find_subdomain(host)
    response   = api.dns.post(record, external_ip_address)

def parse_args():
    parser = argparse.ArgumentParser(description='Update Vultr DNS')

    parser.add_argument('api_key', type=str, help='API Key or Token')
    parser.add_argument('domain', type=str, help='A Domain')
    parser.add_argument('host', type=str, help='A Host')

    return parser.parse_args()

if __name__ == '__main__':
    try:
        logger = logging.getLogger('vultr-dns-updater')
        # level  = args.v.upper() if not None else 'INFO'

        coloredlogs.install(level='DEBUG', logger=logger)

        arguments   = parse_args()
        external_ip = ExternalIPService()
        vultr       = VultrAPI(arguments.api_key, arguments.domain, logger)

        update_dns(
            api=vultr,
            external_ip=external_ip,
            host=arguments.host
        )

    except (Exception) as err:
        print ("Error: ", err)
