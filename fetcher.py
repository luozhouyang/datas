import re
from urllib import request

# <li>可去地区：<span>待议 </span></li>
# <li>是否收费：<span>收费<FONT COLOR=#888888>..</FONT></span></li>
# <li>服务时间：<span>待议 </span></li>
# <li>使用语种：<span>普通话  </span></li>
# <li>提供服务：<span>待议</span></li>
# <li>兴趣爱好：<span>聊天, 赚钱 </span></li>
# <li>性格类型：<span>阳光, 活泼可爱 </span></li>
# <li>心情留言：<span>找工作  </span></li>

PATTERN_AREA = re.compile("可去地区")
PATTERN_PAYMENT = re.compile("是否收费")
PATTERN_SERVE_TIME = re.compile("服务时间")
PATTERN_LANGUAGE = re.compile("使用语种")
PATTERN_SERVE_TYPE = re.compile("提供服务")
PATTERN_HOBBITS = re.compile("兴趣爱好")
PATTERN_CHARACTERISTIC = re.compile("性格类型")
PATTERN_MESSAGE = re.compile("心情留言")

# <li class="li539"><span>昵　　称：鑫大宝</span> </li>
# <li class="li539"><SPAN>Ｉ　　Ｄ：</SPAN>700002&nbsp;&nbsp;
# <!--诚意 登陆时间-->
# 诚意:22<IMG alt="" src="imageszny/images/cy2.gif" align="absMiddle">
#
# </li>
# </li>
# <li class="li265"><SPAN>性　　别：</SPAN>女</li>
# <li class="li265"><SPAN>年　　龄：</SPAN>24岁</li>
# <li class="li265"><SPAN>出生年月：</SPAN>1987-8-19</li>
# <li class="li265"><SPAN>星　　座：</SPAN>狮子</li>
# <li class="li265"><SPAN>身　　高：</SPAN>162CM</li>
# <li class="li265"><SPAN>体　　重：</SPAN>55KG</li>
# <li class="li265"><SPAN>体　　形：</SPAN>匀称</li>
# <li class="li265"><SPAN>学　　历：</SPAN>中专</li>
# <li class="li265"><SPAN>婚　　姻：</SPAN>未婚</li>
# <li class="li265"><SPAN>职　　业：</SPAN>医生</li>
# <li class="li265"><SPAN>居住城市：</SPAN>黑龙江&nbsp;哈尔滨
# </li>
# <li class="li265"><SPAN>籍　　贯：</SPAN>山东</li>
# <li class="li265"><SPAN>注册日期：</SPAN>VIP会员可见</li>
# <li class="li265"><SPAN>登陆日期：</SPAN>VIP会员可见</li>
# </ul>

PATTERN_NAME = re.compile("昵　　称")
PATTERN_ID = re.compile("Ｉ　　Ｄ")
PATTERN_GENDER = re.compile("性　　别")
PATTERN_AGE = re.compile("年　　龄")
PATTERN_BIRTH = re.compile("出生年月")
PATTERN_CONSTELLATION = re.compile("星　　座")
PATTERN_HEIGHT = re.compile("身　　高")
PATTERN_WEIGHT = re.compile("体　　重")
PATTERN_SIZE = re.compile("体　　形")
PATTERN_DEGREE = re.compile("学　　历")
PATTERN_MARRIAGE = re.compile("婚　　姻")
PATTERN_OCCUPATIONAL = re.compile("职　　业")
PATTERN_LIVES = re.compile("居住城市")
PATTERN_ORIGIN = re.compile("籍　　贯")

PATTERN_CHARS = re.compile("[a-zA-Z<>/&;\"=#.]")
PATTERN_265 = re.compile("265")
PATTERN_888888 = re.compile("888888")


class Item:

    def __init__(self, name="", id="", gender="", age="", birth="", constellation="",
                 height="", weight="", size="", degree="", marriage="", occupational="",
                 lives="", origin="", area="", payment="", serve_time="", language="",
                 serve_type="", hobbits="", characteristic="", message=""):
        self.name = name
        self.id = id
        self.gender = gender
        self.age = age
        self.birth = birth
        self.constellation = constellation
        self.height = height
        self.weight = weight
        self.size = size
        self.degree = degree
        self.marriage = marriage
        self.occupational = occupational
        self.lives = lives
        self.origin = origin
        self.area = area
        self.payment = payment
        self.serve_time = serve_time
        self.language = language
        self.serve_type = serve_type
        self.hobbits = hobbits
        self.character = characteristic
        self.message = message

    def __str__(self):
        return "name={},id={},gender={},age={},birth={},constellation={},height={},weight={}," \
               "size={},degree={},marriage={},occupational={},lives={},origin={},area={},payment={}," \
               "serve_time={},language={},serve_type={},hobbits={},characteristic={},message={}" \
            .format(self.name, self.id, self.gender, self.age, self.birth, self.constellation,
                    self.height, self.weight, self.size, self.degree, self.marriage, self.occupational,
                    self.lives, self.origin, self.area, self.payment, self.serve_time, self.language,
                    self.serve_type, self.hobbits, self.character, self.message)


class Fetcher:

    def __init__(self, out_dir="/tmp/zuyou", threads=4):
        self.out_dir = out_dir
        self.threads = threads
        self.id_start = 700000
        self.id_end = 840000
        self.url = "http://www.89yn.com/member.asp?id="

    def parse(self, line):
        line = PATTERN_CHARS.sub("", line)
        line = PATTERN_265.sub("", line)
        line = PATTERN_888888.sub("", line)
        contents = line.split("：")
        if len(contents) != 2:
            return ""
        return contents[1].strip()

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
                if PATTERN_NAME.findall(l):
                    item.name = self.parse(l)
                if PATTERN_ID.findall(l):
                    item.id = self.parse(l)
                if PATTERN_GENDER.findall(l):
                    item.gender = self.parse(l)
                if PATTERN_AGE.findall(l):
                    item.age = self.parse(l)
                if PATTERN_BIRTH.findall(l):
                    item.birth = self.parse(l)
                if PATTERN_CONSTELLATION.findall(l):
                    item.constellation = self.parse(l)
                if PATTERN_HEIGHT.findall(l):
                    item.height = self.parse(l)
                if PATTERN_WEIGHT.findall(l):
                    item.weight = self.parse(l)
                if PATTERN_SIZE.findall(l):
                    item.size = self.parse(l)
                if PATTERN_DEGREE.findall(l):
                    item.degree = self.parse(l)
                if PATTERN_MARRIAGE.findall(l):
                    item.marriage = self.parse(l)
                if PATTERN_OCCUPATIONAL.findall(l):
                    item.occupational = self.parse(l)
                if PATTERN_LIVES.findall(l):
                    item.lives = self.parse(l)
                if PATTERN_ORIGIN.findall(l):
                    item.origin = self.parse(l)
                if PATTERN_AREA.findall(l):
                    item.area = self.parse(l)
                if PATTERN_PAYMENT.findall(l):
                    item.payment = self.parse(l)
                if PATTERN_SERVE_TIME.findall(l):
                    item.serve_time = self.parse(l)
                if PATTERN_LANGUAGE.findall(l):
                    item.language = self.parse(l)
                if PATTERN_SERVE_TYPE.findall(l):
                    item.serve_type = self.parse(l)
                if PATTERN_HOBBITS.findall(l):
                    item.hobbits = self.parse(l)
                if PATTERN_CHARACTERISTIC.findall(l):
                    item.character = self.parse(l)
                if PATTERN_MESSAGE.findall(l):
                    item.message = self.parse(l)

            print(item)


if __name__ == "__main__":
    fetcher = Fetcher()
    fetcher.fetch_one("700002")
