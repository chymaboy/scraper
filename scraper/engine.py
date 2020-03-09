import json
import csv
import sys
import typing
from collections import deque

import requests


SIGN_STDOUT = '-'
FORMAT_CSV = 'csv'
FORMAT_JL = 'jl'


def start(start_urls: typing.List, callback: typing.Callable, out_path: str, out_format: str):
    start_tasks = [(start_url, callback) for start_url in start_urls]
    tasks = deque(start_tasks)

    if out_path == SIGN_STDOUT:
        out_file = sys.stdout
    else:
        out_file = open(out_path, 'w', buffering=1)

    try:
        with_header = True
        while tasks:
            url, callback = tasks.popleft()
            resp = requests.get(url)

            for result in callback(resp):
                if isinstance(result, dict):
                    result['url'] = url
                    if out_format == FORMAT_CSV:
                        _write_csv(result, out_file, with_header=with_header)
                        if with_header:
                            with_header = False
                    else:
                        _write_jl(result, out_file)
                else:
                    tasks.append(result)
    finally:
        out_file.close()


def _write_jl(row, out_file):
    json.dump(row, out_file)
    out_file.write('\n')


def _write_csv(row, out_file, with_header=False):
    writer = csv.DictWriter(out_file, delimiter=',', fieldnames=row.keys())
    if with_header:
        writer.writeheader()
    writer.writerow(row)
