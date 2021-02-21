import requests
import json
from config_data import dict_of_currency




class ConvertionExcepyion(Exception):
    pass


class Converter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        try:
            quote_tick = dict_of_currency[quote.lower()]
        except KeyError:
            raise ConvertionExcepyion(f'не удалось обработать валюту {quote}')
        try:
            base_tick = dict_of_currency[base.lower()]
        except KeyError:
            raise ConvertionExcepyion(f'не удалось обработать валюту {base}')
        try:
            amount_tick = float(amount)
        except ValueError:
            raise ConvertionExcepyion(f'вы введи неправильно количество валюты {amount}')
        if quote == base:
            raise ConvertionExcepyion(f'Вы ввели две одинаковые валюты {base}, пожалуйста введите разные')

        r = requests.get(f'https://api.exchangeratesapi.io/latest?base={quote_tick}')
        total_base = json.loads(r.content)['rates'][base_tick]
        text = f'за {amount} {quote} получите {round(total_base * amount_tick, 4)} {base}'

        return text