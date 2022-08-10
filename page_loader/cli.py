import argparse
import os


def parse():
    parser = argparse.ArgumentParser(
        prog='page_loader',
        description='utility that downloads a web page and data')
    parser.add_argument('url', help='')
    parser.add_argument('-o', '--output',
                        default=os.getcwd())
    return parser.parse_args()
