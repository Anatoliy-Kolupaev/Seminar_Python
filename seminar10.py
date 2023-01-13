# Получить информацию о текущих курсах валют при помощи requests и bs4.
# API для получения курса через requests www.cbr-xml-daily.ru
import requests as rq
import xmltodict
import bs4 as bs



def currency(curr):
    s = rq.get('http://www.cbr.ru/scripts/XML_daily.asp')

    dct = xmltodict.parse(s.text)['ValCurs']['Valute']
    rate = 0.0
    for val in dct:
        if val['CharCode'] == curr:
            rate = float(val["Value"].replace(',', '.')) / int(val["Nominal"])
            print(
                f'Курс валюты {curr} на текущий день: \n{val["Name"]} - {rate}')
    return rate


rate1 = currency('USD')
rate2 = currency('EUR')
rate3 = currency('CNY')

