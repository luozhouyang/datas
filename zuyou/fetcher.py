from concurrent.futures import ThreadPoolExecutor
from urllib import request

from zuyou.zuyou_patterns import Patterns
from .zuyou_item import Item


class Fetcher:

    def __init__(self, out_dir="/tmp/datas", threads=4):
        self.out_dir = out_dir
        self.threads = threads
        self.id_start = 700000
        self.id_end = 840000
        self.url = "http://www.89yn.com/member.asp?id="

    @staticmethod
    def _parse_line(line, type=1):
        contents = line.split("：")
        if len(contents) != 2:
            return ""
        if type == 1:
            result = Patterns.PATTERN_TYPE_1.sub("", contents[1])
            return result.strip()
        elif type == 2:
            result = Patterns.PATTERN_TYPE_ID.sub("", contents[1])
            return result.strip()
        elif type == 3:
            result = Patterns.PATTERN_TYPE_PAYMENT.sub("", contents[1])
            return result.strip()
        return ""

    def fetch_range(self, start=700000, end=840000):
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            for i in range(start, end):
                executor.submit(self.fetch_one, str(i))

    def fetch_one(self, id):
        resp = request.urlopen(url=self.url + id, timeout=3 * 1000)
        if resp.getcode() == 200:
            item = Item()
            page = resp.read().decode('gbk')
            # print(page)
            lines = page.split("\r\n")
            for l in lines:
                if not l.strip():
                    continue
                if Patterns.PATTERN_NAME.findall(l):
                    item.name = self._parse_line(l)
                if Patterns.PATTERN_ID.findall(l):
                    item.id = self._parse_line(l, type=2)
                if Patterns.PATTERN_GENDER.findall(l):
                    item.gender = self._parse_line(l)
                if Patterns.PATTERN_AGE.findall(l):
                    item.age = self._parse_line(l)
                if Patterns.PATTERN_BIRTH.findall(l):
                    item.birth = self._parse_line(l)
                if Patterns.PATTERN_CONSTELLATION.findall(l):
                    item.constellation = self._parse_line(l)
                if Patterns.PATTERN_HEIGHT.findall(l):
                    item.height = self._parse_line(l)
                if Patterns.PATTERN_WEIGHT.findall(l):
                    item.weight = self._parse_line(l)
                if Patterns.PATTERN_SIZE.findall(l):
                    item.size = self._parse_line(l)
                if Patterns.PATTERN_DEGREE.findall(l):
                    item.degree = self._parse_line(l)
                if Patterns.PATTERN_MARRIAGE.findall(l):
                    item.marriage = self._parse_line(l)
                if Patterns.PATTERN_OCCUPATIONAL.findall(l):
                    item.occupational = self._parse_line(l)
                if Patterns.PATTERN_LIVES.findall(l):
                    item.lives = self._parse_line(l)
                if Patterns.PATTERN_ORIGIN.findall(l):
                    item.origin = self._parse_line(l)
                if Patterns.PATTERN_AREA.findall(l):
                    item.area = self._parse_line(l)
                if Patterns.PATTERN_PAYMENT.findall(l):
                    item.payment = self._parse_line(l, type=3)
                if Patterns.PATTERN_SERVE_TIME.findall(l):
                    item.serve_time = self._parse_line(l)
                if Patterns.PATTERN_LANGUAGE.findall(l):
                    item.language = self._parse_line(l)
                if Patterns.PATTERN_SERVE_TYPE.findall(l):
                    item.serve_type = self._parse_line(l)
                if Patterns.PATTERN_HOBBITS.findall(l):
                    item.hobbits = self._parse_line(l)
                if Patterns.PATTERN_CHARACTERISTIC.findall(l):
                    item.character = self._parse_line(l)
                if Patterns.PATTERN_MESSAGE.findall(l):
                    item.message = self._parse_line(l)

            print(item.lives, item.occupational)


if __name__ == "__main__":
    fetcher = Fetcher()
    fetcher.fetch_range(700000, 700020)
