from scraper import engine
from scraper.spiders import fifa, cfm


def execute(args):
    # engine.start([fifa.START_URL], fifa.parse, args.outfile, args.format)
    cfm_urls = [cfm.BASE_URL + f'?p={i}' for i in range(1, 11)]
    engine.start(cfm_urls, cfm.parse, args.outfile, args.format)

