import csv
from collections import Counter, OrderedDict

import matplotlib.pyplot as plt


class Visualizer:

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

        def callback(row):
            age = str(row[3].replace('岁', ''))
            gender = row[2].strip()
            education = row[9].strip()
            origin = row[13].strip()
            ages.append(age)
            educations.append(education)
            origins.append(origin)
            if gender == "男":
                ages_men.append(age)
                educations_men.append(education)
                origins_men.append(origin)
            elif gender == "女":
                ages_women.append(age)
                educations_women.append(education)
                origins_women.append(origin)
            genders.append(gender)

        self._read_csv_file(callback)

        self.ages_dict = OrderedDict(sorted(Counter(ages).items()))
        self.ages_men_dict = OrderedDict(sorted(Counter(ages_men).items()))
        self.ages_women_dict = OrderedDict(sorted(Counter(ages_women).items()))
        self.genders_dict = OrderedDict(sorted(Counter(genders).items()))
        self.educations_dict = OrderedDict(sorted(Counter(educations).items()))
        self.educations_men_dict = OrderedDict(sorted(Counter(educations_men).items()))
        self.educations_women_dict = OrderedDict(sorted(Counter(educations_women).items()))

        self.has_parse_file = True

    def _read_csv_file(self, parse_line_callback):
        with open(self.csv_file, mode="rt", encoding="utf8", buffering=8192) as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                parse_line_callback(row)

    def visualize_age_line(self):
        if not self.has_parse_file:
            self.parse_csv_file()
        plt.figure(figsize=(10, 7))
        plt.title('Age distribution line chart')
        plt.plot(self.ages_dict.keys(), self.ages_dict.values())
        plt.xlabel('Age')
        plt.savefig("images/age_line.png")

    def visualize_age_pie(self):
        if not self.has_parse_file:
            self.parse_csv_file()
        # age_dict = self._age_dict()
        total = 0
        for _, v in self.ages_dict.items():
            total += v
        plt.figure(figsize=(8, 8))
        plt.title('Age distribution pie chart')
        labels = []
        for k in self.ages_dict.keys():
            v = "%s - %.2f" % (k, (int(self.ages_dict[k]) / total * 100))
            labels.append(v + "%")
        plt.pie(self.ages_dict.values(), labels=labels)
        plt.savefig('images/age_pie.png')

    def visualize_age_men_line(self):
        if not self.has_parse_file:
            self.parse_csv_file()
        plt.figure(figsize=(8, 8))
        plt.title("Male age distribution", )
        # total = 0
        # for v in self.ages_men_dict.values():
        #     total += int(v)
        # labels = []
        # for k in self.ages_men_dict.keys():
        #     labels.append("%s - %.2f" % (k, int(k) / total))
        plt.pie(self.ages_men_dict.values(), labels=self.ages_men_dict.keys())
        # plt.legend()
        plt.savefig('images/age_men_pie.png')


if __name__ == "__main__":
    v = Visualizer("/home/allen/PycharmProjects/datas/www89yn_data/info.csv")
    v.parse_csv_file()
    v.visualize_age_line()
    v.visualize_age_pie()
    v.visualize_age_men_line()
