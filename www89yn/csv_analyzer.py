import csv
from collections import Counter, OrderedDict

import jieba

from .csv_image_generator import ImageGenerator
from .csv_table_printer import TablePrinter
from .csv_xlsx_saver import XLSXSaver

jieba.load_userdict("/home/allen/PycharmProjects/datas/jieba_dict.txt")


class Analyzer:

    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.has_parse_file = False
        self.ages_dict = None
        self.ages_men_dict = None
        self.ages_women_dict = None
        self.genders_dict = None
        self.educations_dict = None
        self.educations_men_dict = None
        self.educations_women_dict = None
        self.service_types_dict = None
        self.service_types_men_dict = None
        self.service_types_women_dict = None
        self.origin_dict = None
        self.origin_men_dict = None
        self.origin_women_dict = None
        self.lives_dict = None
        self.lives_men_dict = None
        self.lives_women_dict = None

    def parse_csv_file(self):
        ages = []
        ages_men = []
        ages_women = []
        genders = []
        educations = []
        educations_men = []
        educations_women = []
        origins = []
        origins_men = []
        origins_women = []
        service_types = []
        service_types_men = []
        service_types_women = []
        lives = []
        lives_men = []
        lives_women = []

        def callback(row):
            age = str(row[3].replace('岁', ''))
            gender = row[2].strip()
            education = row[9].strip()
            live_cities = []
            for r in jieba.cut(row[12], cut_all=True):
                live_cities.append(r)
            if len(live_cities) == 0:
                live_cities.append('其它')
            first = live_cities[0].strip()
            if first:
                if len(first) >= 2:
                    live = live_cities[0].strip()
                    if live == '马来':
                        live = '马来西亚'
                else:
                    live = '其他'
            else:
                live = '其他'
            origin = row[13].strip()
            services_tmp = row[18].strip().split(";")
            services = []
            for v in services_tmp:
                if v.strip():
                    services.append(v.strip())
            ages.append(age)
            educations.append(education)
            origins.append(origin)
            service_types.extend(services)
            lives.append(live)
            if gender == "男":
                ages_men.append(age)
                educations_men.append(education)
                origins_men.append(origin)
                service_types_men.extend(services)
                lives_men.append(live)
            elif gender == "女":
                ages_women.append(age)
                educations_women.append(education)
                origins_women.append(origin)
                service_types_women.extend(services)
                lives_women.append(live)
            genders.append(gender)

        self._read_csv_file(callback)

        self.ages_dict = OrderedDict(sorted(Counter(ages).items()))
        self.ages_men_dict = OrderedDict(sorted(Counter(ages_men).items()))
        self.ages_women_dict = OrderedDict(sorted(Counter(ages_women).items()))
        self.genders_dict = OrderedDict(sorted(Counter(genders).items()))
        self.educations_dict = OrderedDict(sorted(Counter(educations).items()))
        self.educations_men_dict = OrderedDict(sorted(Counter(educations_men).items()))
        self.educations_women_dict = OrderedDict(sorted(Counter(educations_women).items()))
        self.service_types_dict = OrderedDict(sorted(Counter(service_types).items()))
        self.service_types_men_dict = OrderedDict(sorted(Counter(service_types_men).items()))
        self.service_types_women_dict = OrderedDict(sorted(Counter(service_types_women).items()))
        self.origin_dict = OrderedDict(sorted(Counter(origins).items()))
        self.origin_men_dict = OrderedDict(sorted(Counter(origins_men).items()))
        self.origin_women_dict = OrderedDict(sorted(Counter(origins_women).items()))
        self.lives_dict = OrderedDict(sorted(Counter(lives).items()))
        self.lives_men_dict = OrderedDict(sorted(Counter(lives_men).items()))
        self.lives_women_dict = OrderedDict(sorted(Counter(lives_women).items()))

        self.has_parse_file = True

    def _read_csv_file(self, parse_line_callback):
        with open(self.csv_file, mode="rt", encoding="utf8", buffering=8192) as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                parse_line_callback(row)

    def analyze(self):
        if not self.has_parse_file:
            self.parse_csv_file()
        self.print_tables()
        self.gen_images()
        self.save_to_xlsx()

    def print_tables(self):
        ages = [self.ages_dict, self.ages_men_dict, self.ages_women_dict]
        services = [self.service_types_dict, self.service_types_men_dict, self.service_types_women_dict]
        edus = [self.educations_dict, self.educations_men_dict, self.educations_women_dict]
        origins = [self.origin_dict, self.origin_men_dict, self.origin_women_dict]
        cities = [self.lives_dict, self.lives_men_dict, self.lives_women_dict]
        printer = TablePrinter(ages, services, edus, origins, cities)
        printer.print_tables()

    def save_to_xlsx(self):
        ages = [self.ages_dict, self.ages_men_dict, self.ages_women_dict]
        services = [self.service_types_dict, self.service_types_men_dict, self.service_types_women_dict]
        edus = [self.educations_dict, self.educations_men_dict, self.educations_women_dict]
        origins = [self.origin_dict, self.origin_men_dict, self.origin_women_dict]
        cities = [self.lives_dict, self.lives_men_dict, self.lives_women_dict]
        saver = XLSXSaver(filename="datas.xlsx", ages=ages, services=services,
                          educations=edus, origins=origins, cities=cities)
        saver.save_to_xlsx()

    def gen_images(self):
        ages = [self.ages_dict, self.ages_men_dict, self.ages_women_dict]
        services = [self.service_types_dict, self.service_types_men_dict, self.service_types_women_dict]
        edus = [self.educations_dict, self.educations_men_dict, self.educations_women_dict]
        origins = [self.origin_dict, self.origin_men_dict, self.origin_women_dict]
        cities = [self.lives_dict, self.lives_men_dict, self.lives_women_dict]
        generator = ImageGenerator(ages, services, edus, origins, cities)
        generator.gen_images()


if __name__ == "__main__":
    v = Analyzer("/home/allen/PycharmProjects/datas/www89yn_data/0_info_20180609.csv")
    v.analyze()
