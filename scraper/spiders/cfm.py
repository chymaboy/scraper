import requests
from parsel import Selector


BASE_URL = 'https://cheese.formice.com/transformice/ranking/tribes/'


def parse(resp: requests.Response):
    sel = Selector(resp.text)

    tribe_css = 'td a::attr(href)'
    tasks = [(url, parse_tribe) for url in sel.css(tribe_css).getall()]

    return tasks


def parse_tribe(resp: requests.Response):
    sel = Selector(resp.text)

    tribe = {'name': sel.css('.card-body a::text').get()}

    metrics = ['Rounds played', 'Cheese gathered', 'Cheese gathered first', 'Bootcamp', 'Mice saved',
               'Mice saved (hard)', 'Mice saved (divine)', 'Cheese gathered as shaman']

    indexes = [1, 3, 6, 9, 12, 15, 18, 21]

    tds = sel.css('td::text').getall()

    for name, ind in zip(metrics, indexes):
        val_str = tds[ind]
        tribe[name] = int(val_str.replace(',', ''))

    return [tribe]
