import requests

inp_val = input()
inp_val = inp_val.lower()
www_str = 'http://www.floatrates.com/daily/' + inp_val + '.json'
r = requests.get(www_str)
print(r.json()['usd'])
print(r.json()['eur'])
