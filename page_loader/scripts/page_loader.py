# !/usr/bin/env python3
# import os
import sys

from page_loader.page_loader import download

# from page_loader import download
from page_loader.cli import parse


def main():
    try:
        args = parse()
        result = download(
            args.url,
            args.output
        )
        print(result)
    except Exception:
        sys.exit(1)


if __name__ == '__main__':
    main()
