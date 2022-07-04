# !/usr/bin/env python3
from page_loader import download
from page_loader.cli import parse


def main():
    args = parse()
    result = download(args)
    print(result)


if __name__ == '__main__':
    main()