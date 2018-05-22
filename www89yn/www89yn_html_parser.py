import os

from www89yn.www89yn_patterns import Patterns
from www89yn.www89yn_item import Item

files = os.listdir("/home/allen/PycharmProjects/datas/www89yn_data")
infos = []


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


for f in files:
    if not f.endswith(".txt"):
        continue
    p = "/home/allen/PycharmProjects/datas/data/" + f
    if not os.path.exists(p):
        continue
    with open(p, mode="rt", encoding="utf-8") as fin:
        item = Item()
        for l in fin:
            if not l.strip():
                continue
            if Patterns.PATTERN_NAME.findall(l):
                item.name = _parse_line(l)
            if Patterns.PATTERN_ID.findall(l):
                item.id = _parse_line(l, type=2)
            if Patterns.PATTERN_GENDER.findall(l):
                item.gender = _parse_line(l)
            if Patterns.PATTERN_AGE.findall(l):
                item.age = _parse_line(l)
            if Patterns.PATTERN_BIRTH.findall(l):
                item.birth = _parse_line(l)
            if Patterns.PATTERN_CONSTELLATION.findall(l):
                item.constellation = _parse_line(l)
            if Patterns.PATTERN_HEIGHT.findall(l):
                item.height = _parse_line(l)
            if Patterns.PATTERN_WEIGHT.findall(l):
                item.weight = _parse_line(l)
            if Patterns.PATTERN_SIZE.findall(l):
                item.size = _parse_line(l)
            if Patterns.PATTERN_DEGREE.findall(l):
                item.degree = _parse_line(l)
            if Patterns.PATTERN_MARRIAGE.findall(l):
                item.marriage = _parse_line(l)
            if Patterns.PATTERN_OCCUPATIONAL.findall(l):
                item.occupational = _parse_line(l)
            if Patterns.PATTERN_LIVES.findall(l):
                item.lives = _parse_line(l)
            if Patterns.PATTERN_ORIGIN.findall(l):
                item.origin = _parse_line(l)
            if Patterns.PATTERN_AREA.findall(l):
                item.area = _parse_line(l)
            if Patterns.PATTERN_PAYMENT.findall(l):
                item.payment = _parse_line(l, type=3)
            if Patterns.PATTERN_SERVE_TIME.findall(l):
                item.serve_time = _parse_line(l)
            if Patterns.PATTERN_LANGUAGE.findall(l):
                item.language = _parse_line(l)
            if Patterns.PATTERN_SERVE_TYPE.findall(l):
                item.serve_type = _parse_line(l)
            if Patterns.PATTERN_HOBBITS.findall(l):
                item.hobbits = _parse_line(l)
            if Patterns.PATTERN_CHARACTERISTIC.findall(l):
                item.character = _parse_line(l)
            if Patterns.PATTERN_MESSAGE.findall(l):
                item.message = _parse_line(l)
        if item.id:
            # print(count)
            infos.append(item)
outdir = "/home/allen/PycharmProjects/datas/www89yn_data/"
if not os.path.exists(outdir):
    os.mkdir(outdir)
outfile = outdir + 'info.csv'
with open(outfile, mode="wt", encoding="utf-8", buffering=8192) as f:
    f.write("姓名, Id, 性别, 年龄, 生日, 星座, 身高, 体重, 体型, 学位, 婚姻," +
            "职业, 居住城市, 籍贯, 可去地区, 是否收费, 服务时间, 使用语种, 提供服务," +
            "兴趣爱好, 性格类型, 心情留言\n")
    count = 0
    for item in infos:
        count += 1
        print(count)
        line = item.name + "," + item.id + "," + item.gender + "," + item.age + "," + item.birth + "," + \
               item.constellation + "," + item.height + "," + item.weight + "," + item.size + "," + \
               item.degree + "," + item.marriage + "," + item.occupational + "," + item.lives + "," + \
               item.origin + "," + item.area + "," + item.payment + "," + item.serve_time + "," + \
               item.language + "," + item.serve_type + "," + item.hobbits + "," + item.character + "," + \
               item.message + "\n"
        f.write(line)
