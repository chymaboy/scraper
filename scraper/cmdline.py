import argparse

from scraper.commands import crawl
from scraper.commands import select
from scraper.engine import FORMAT_CSV, FORMAT_JL, SIGN_STDOUT, MONGO_DB


def parse():
    parser = argparse.ArgumentParser(prog='scraper')
    subparsers = parser.add_subparsers()

    parser_crawl = subparsers.add_parser('crawl')

    parser_crawl.add_argument('-o', '--outfile', metavar='FILE', default=SIGN_STDOUT)
    parser_crawl.add_argument('-f', '--format', default=FORMAT_CSV, choices=[FORMAT_CSV, FORMAT_JL, MONGO_DB])
    parser_crawl.add_argument('-s', '--spider', default='cfm', choices=['cfm', 'fifa'])
    parser_crawl.set_defaults(func=crawl.execute)

    parser_select = subparsers.add_parser('select')
    parser_select.add_argument('-q', '--query', default='name: k')
    parser_select.add_argument('-l', '--limit', default=10)
    parser_select.set_defaults(func=select.execute)

    args = parser.parse_args()
    args.func(args)
