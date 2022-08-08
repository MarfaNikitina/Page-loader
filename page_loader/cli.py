import argparse
import os


def parse():
    parser = argparse.ArgumentParser(
        prog='page_loader',
        description='')
    # parser.add_argument('file_path')
    parser.add_argument('url', help='')
    parser.add_argument('--output',
                        default=os.getcwd())
    return parser.parse_args()
