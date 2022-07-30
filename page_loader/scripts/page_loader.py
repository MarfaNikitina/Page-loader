# !/usr/bin/env python3
from page_loader.page_loader import download
from page_loader.cli import parse


def main():
    args = parse()
    result = download(
        args.output,
        args.page_name,
        args.file_path
    )
    print(result)


if __name__ == '__main__':
    main()