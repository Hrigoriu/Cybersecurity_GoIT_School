import urllib.request


with urllib.request.urlopen('https://www.python.org/') as f:
    print(f.read(300))

"""
b'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n\n\n<html
xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n\n<head>\n
<meta http-equiv="content-type" content="text/html; charset=utf-8" />\n
<title>Python Programming '
"""
#====================================================================================================
import requests


r = requests.get('https://api.github.com/events')
print(r.text[:300])

"""
[{"id":"16602799523","type":"DeleteEvent","actor":{"id":49699333,"login":"dependabot[bot]","display_login":"dependabot","gravatar_id":"","url":"https://api.github.com/users/dependabot[bot]","avatar_url":"https://avatars.githubusercontent.com/u/49699333?"},"repo":{"id":111928778,"name":"akigugale/tre
"""
#====================================================================================================
import requests

response = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11')
exchange_rate = response.json()
print(exchange_rate)

"""
[{'ccy': 'EUR', 'base_ccy': 'UAH', 'buy': '50.86000', 'sale': '51.54639'}, 
 {'ccy': 'USD', 'base_ccy': 'UAH', 'buy': '42.94000', 'sale': '43.47826'}]
"""
#====================================================================================================
