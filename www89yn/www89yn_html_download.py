import time
from urllib import request

for id in range(714837, 800000):
    try:
        time.sleep(1)
        resp = request.urlopen('http://www.89yn.com/member.asp?id=' + str(id), timeout=2.0)
        if resp.getcode() != 200:
            continue
        page = resp.read().decode('gbk')
        file = '/home/allen/PycharmProjects/datas/www89yn_data/' + str(id) + '.txt'
        with open(file, mode='wt', encoding='utf-8', buffering=8192) as f:
            f.write(page)
    except Exception as e:
        continue
    else:
        print(str(id))
