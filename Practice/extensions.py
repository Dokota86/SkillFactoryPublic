import requests


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: float) -> float:
        url = f'https://min-api.cryptocompare.com/data/price?fsym={base}&tsyms={quote}'
        response = requests.get(url)
        data = response.json()

        if quote.upper() not in data:
            raise APIException(f'Не удалось получить курс {base.upper()} к {quote.upper()}')

        return data[quote.upper()] * amount
