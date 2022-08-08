# !/usr/bin/env python3
import os

from page_loader.page_loader import download

# from page_loader import download
from page_loader.cli import parse


def main():
    args = parse()
    result = download(
        args.url,
        args.output
    )
    print(result)


if __name__ == '__main__':
    main()
