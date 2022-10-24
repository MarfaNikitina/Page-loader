# !/usr/bin/env python3
# import os
import sys
from page_loader import download
from page_loader.cli import parse
import logging
import requests

logging.basicConfig(level=logging.INFO)


def main():
    try:
        args = parse()
        result = download(
            args.url,
            args.output
        )
        print(result)
    except requests.RequestException as error:
        logging.error(error)
        logging.info('Page not found or status_code is not 200')
        raise Exception(error)
        sys.exit(1)


if __name__ == '__main__':
    main()
