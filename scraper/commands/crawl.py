from scraper import engine
from scraper.spiders import fifa, cfm


def execute(args):
    if args.spider == 'cfm':
        engine_urls = [cfm.BASE_URL + f'?p={i}' for i in range(1, 11)]
        engine_func = cfm.parse
    elif args.spider == 'fifa':
        engine_urls = [fifa.START_URL]
        engine_func = fifa.parse

    engine.start(engine_urls, engine_func, args.outfile, args.format)
