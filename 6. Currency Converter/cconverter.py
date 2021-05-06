import requests
import json

my_currency = input().lower()

dictionary = dict()

while True:
    currency_change = input().lower()
    if currency_change == '':
        break
    else:
        money = float(input())
        dict_my_currency = 'http://www.floatrates.com/daily/' + my_currency + '.json'
        dict_eur = 'http://www.floatrates.com/daily/eur.json'
        dict_usd = 'http://www.floatrates.com/daily/usd.json'

        r1 = requests.get(dict_my_currency).json()
        r2 = requests.get(dict_eur).json()
        r3 = requests.get(dict_usd).json()

        my_rate = r1[currency_change]['rate']

        if my_currency == 'eur':
            rate_eur = r3['eur']['rate']
            rate_usd = my_rate
        elif my_currency == 'usd':
            rate_eur = my_rate
            rate_usd = r2['usd']['rate']
        else:
            rate_eur = r1['eur']['rate']
            rate_usd = r1['usd']['rate']

        dictionary.update({'usd': rate_usd})
        dictionary.update({'eur': rate_eur})
        # dictionary.update({currency_change: my_rate})

        if currency_change in dictionary.keys():
            print('Checking the cache...')
            print('Oh! It is in the cache!')
            n = round(dictionary[currency_change] * money, 2)
            print('You received', n, currency_change.upper() + '.')
        elif currency_change not in dictionary:
            print('Checking the cache...')
            print('Sorry, but it is not in the cache!')
            n = round(my_rate * money, 2)
            print('You received', n, currency_change.upper() + '.')
            dictionary.update({currency_change: my_rate})
