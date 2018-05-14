import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib import request

from zuyou.zuyou_patterns import Patterns
from .www89yn_item import Item


class Fetcher:

    def __init__(self, out_dir="/tmp/datas", threads=4):
        self.out_dir = out_dir
        self.threads = threads
        self.id_start = 700000
        self.id_end = 840000
        self.url = "http://www.www89yn.com/member.asp?id="
        self.results = []

    @staticmethod
    def _parse_line(line, type=1):
        contents = line.split("：")
        if len(contents) != 2:
            return ""
        if type == 1:
            result = Patterns.PATTERN_TYPE_1.sub("", contents[1])
            return result.replace(",", ";").replace("\s+", " ").strip()
        elif type == 2:
            result = Patterns.PATTERN_TYPE_ID.sub("", contents[1])
            return result.replace(",", ";").replace("\s+", " ").strip()
        elif type == 3:
            result = Patterns.PATTERN_TYPE_PAYMENT.sub("", contents[1])
            return result.replace(",", ";").replace("\s+", " ").strip()
        return ""

    def fetch_range(self, start=700000, end=840000):
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = {executor.submit(self.fetch_one, str(i)): i for i in range(start, end)}
            for future in as_completed(futures):
                count = 0
                try:
                    item = future.result()
                except Exception as exc:
                    print(exc)
                else:
                    if item:
                        print(item)
                        self.results.append(item)
                        count += 1
                        if count % 100 == 0:
                            self._write_to_file()
                            self.results.clear()

        self._write_to_file()

    def _write_to_file(self):
        import os
        import time
        if not os.path.exists(self.out_dir):
            os.makedirs(self.out_dir)
        file_path = self.out_dir + os.sep + str(int(round(time.time() * 1000))) + ".csv"
        print(file_path)
        with open(file_path, mode="a", encoding="utf-8", buffering=8192) as file:
            file.write("姓名, Id, 性别, 年龄, 生日, 星座, 身高, 体重, 体型, 学位, 婚姻," +
                       "职业, 居住城市, 籍贯, 可去地区, 是否收费, 服务时间, 使用语种, 提供服务" +
                       "兴趣爱好, 性格类型, 心情留言\n")
            for item in self.results:
                line = item.name + "," + item.id + "," + item.gender + "," + item.age + "," + item.birth + "," + \
                       item.constellation + "," + item.height + "," + item.weight + "," + item.size + "," + \
                       item.degree + "," + item.marriage + "," + item.occupational + "," + item.lives + "," + \
                       item.origin + "," + item.area + "," + item.payment + "," + item.serve_time + "," + \
                       item.language + "," + item.serve_type + "," + item.hobbits + "," + item.character + "," + \
                       item.message + "\n"
                file.write(line)

    def fetch_one(self, id):
        time.sleep(0.3000)
        resp = request.urlopen(url=self.url + id, timeout=0.5)
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
            if item.id:
                return item


if __name__ == "__main__":
    fetcher = Fetcher(out_dir="/home/allen/PycharmProjects/datas/data", threads=2)
    fetcher.fetch_range(700000, 701000)
