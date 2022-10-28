import argparse
import os


def parse():
    parser = argparse.ArgumentParser(
        prog='page_loader',
        description='utility that downloads a web page and data')
    parser.add_argument('url', help='URL of the page you want to download')
    parser.add_argument('-o', '--output',
                        default=os.getcwd(),
                        help='directory where you want to save the downloaded resources')
    return parser.parse_args()
