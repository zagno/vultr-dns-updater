#! /usr/bin/env python3

from service.dns_updater import DNSUpdaterService
from service.external_ip import ExternalIPService
from api.vultr import *

import argparse
import coloredlogs, logging

def parse_args():
    parser = argparse.ArgumentParser(description='Update Vultr DNS')

    parser.add_argument('api_key', type=str, help='Vultr API Key or Token')
    parser.add_argument('domain', type=str, help='A Domain')
    parser.add_argument('host', type=str, help='The Host to update')
    parser.add_argument('-v', '--verbose', action='count', help='Display extra info', default=0)

    arguments = parser.parse_args()

    verbose_loglevel_map = {
        0 : 20, # info
        1 : 10, # debug
    }

    arguments.verbose = verbose_loglevel_map[arguments.verbose]

    return arguments

if __name__ == '__main__':
    try:
        arguments = parse_args()
        logger    = logging.getLogger('vultr-dns-updater')

        coloredlogs.install(level=arguments.verbose, logger=logger)

        dns_updater = DNSUpdaterService(
            api=VultrAPI(arguments.api_key, arguments.domain, logger),
            external_ip_service=ExternalIPService(logger),
            logger=logger
        )

        dns_updater.update(arguments.host)

    except (Exception) as e:
        print ("A Major problem has occured somewhere: ", e)
