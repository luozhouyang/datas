import time
from urllib import request

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Accept': 'text/html',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
    'DNT': '1',
}
for id in range(162315, 167900):
    try:
        time.sleep(1)
        url = 'http://www.zuyouw.com/home/' + str(id)
        print(url)
        req = request.Request(url=url, headers=headers)
        resp = request.urlopen(req, timeout=2.0)
        if resp.getcode() != 200:
            continue
        page = resp.read().decode('utf-8')
        file = '/home/allen/PycharmProjects/datas/zuyouw_data/' + str(id) + '.html'
        with open(file, mode='wt', encoding='utf-8', buffering=8192) as f:
            f.write(page)
    except Exception as e:
        print(e)
        continue
    else:
        print(str(id))
