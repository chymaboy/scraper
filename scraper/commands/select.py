from pymongo import MongoClient
from pprint import pprint


def execute(args):
    client = MongoClient('mongodb://0.tcp.ngrok.io:16849/')
    db = client.cfm_base
    d = {args.query.split(': ')[0]: args.query.split(': ')[1]}
    answer = list(db.cfm_coll.find(d))
    print('|'.join(answer[0].keys()))
    for el in answer:
        for k, v in el.items():
            print(v, end='|')
        print()
