import bs4
from urllib import request

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Accept': 'text/html',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
    'DNT': '1',
}
url = "http://wxapp.zuyou77.com/web"
req = request.Request(url=url, headers=headers)
resp = request.urlopen(req, timeout=2)
html = resp.read().decode('utf8')
print(html)
bs = bs4.BeautifulSoup(html)

for e in bs.div:
    print(e)
