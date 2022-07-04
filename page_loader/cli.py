import argparse


def parse():
    parser = argparse.ArgumentParser(
        prog='page_loader',
        description='')
    parser.add_argument('filepath')
    return parser.parse_args()