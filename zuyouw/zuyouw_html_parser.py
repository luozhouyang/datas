import os

headline = "身　　份,用 户 名,用户　ID,性　　别,婚姻状态,年　　龄,学　　历,身　　高,月薪收入,星　　座,职　　业,所在地区,自我介绍," \
           "个性描述,相貌自评,体　　重,体　　型,魅力部位,发　　型,发　　色,脸　　型,租友类型,方便联系时间," \
           "提供的线上服务,收　　费,提供的线下租友服务,收　　费"


class Item:

    def __init__(self, identify, name, id, gender, marriage, age, education, height, incoming, constellation,
                 occupational, area, charecter, look, weight, charm, hair, hair_color, face, rent_type,
                 time, service_online, pay_online, service_offline, pay_offline, self_intro=""):
        self.identify = identify
        self.name = name
        self.id = id
        self.gender = gender
        self.marriage = marriage
        self.age = age
        self.education = education
        self.height = height
        self.incoming = incoming
        self.constellation = constellation
        self.occupational = occupational
        self.area = area
        self.charecter = charecter
        self.look = look
        self.weight = weight
        self.charm = charm
        self.hair = hair
        self.hair_color = hair_color
        self.face = face
        self.rent_type = rent_type
        self.time = time
        self.service_online = service_online
        self.pay_online = pay_online
        self.service_offline = service_offline
        self.pay_offline = pay_offline
        self.intro = self_intro

    def to_csv_line(self):
        return self.identify+","


filedir = "/home/allen/PycharmProjects/datas/zuyouw_data/"
files = os.listdir(filedir)
for f in files:
    if not f.endswith(".html"):
        continue
    with open(filedir + f, mode="rt", encoding="utf-8", buffering=8192) as fin:
        item = Item()
        while True:
            position = 0
            line = fin.readline()
            if not line:
                break
            if "infolist" in line:
                if position == 0:
                    def parse(line):
                        line = line.split("：")[1]
                        return line[:line.index("<")]


                    position += 1
                    lines = []
                    for _ in range(12):
                        lines.append(fin.readline())
                    item.identify = parse(lines[0])
                    item.name = parse(lines[1])
                    item.id = parse(lines[2])
                    item.gender = parse(lines[3])
                    item.marriage = parse(lines[4])
                    item.age = parse(lines[5])
                    item.education = parse(lines[6])
                    item.height = parse(lines[7])
                    item.incoming = parse(lines[8])
                    item.constellation = parse(lines[9])
                    item.occupational = parse(lines[10])
                    item.area = parse(lines[11])
                    continue
                elif position == 1:
                    position += 1
                    continue
                elif position == 2:
                    position += 1
                    continue
                else:
                    pass
