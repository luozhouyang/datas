import csv
from collections import Counter

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
            age = row[3].replace('岁', '')
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

        self.ages_dict = Counter(ages)
        self.ages_men_dict = Counter(ages_men)
        self.ages_women_dict = Counter(ages_women)
        self.genders_dict = Counter(genders)
        self.educations_dict = Counter(educations)
        self.educations_men_dict = Counter(educations_men)
        self.educations_women_dict = Counter(educations_women)

        self.has_parse_file = True

    def _read_csv_file(self, parse_line_callback):
        with open(self.csv_file, mode="rt", encoding="utf8", buffering=8192) as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                parse_line_callback(row)

    def _age_dict(self):
        age_dict = {}
        for i in range(15, 50):
            age_dict[i] = 0

        def parse_age(row):
            age_dict[int(row[3].replace('岁', ''))] += 1

        self._read_csv_file(parse_age)
        return age_dict

    def visualize_age_line(self):
        age_dict = self._age_dict()
        plt.figure()
        plt.title('Age distribution line chart')
        plt.plot(age_dict.keys(), age_dict.values())
        plt.xlabel('Age')
        plt.savefig("images/age_line.png")

    def visualize_age_pie(self):
        age_dict = self._age_dict()
        total = 0
        for _, v in age_dict.items():
            total += v
        plt.figure()
        plt.title('Age distribution pie chart')
        labels = []
        for k in age_dict.keys():
            v = "%s - %.2f" % (k, (age_dict[k] / total * 100))
            labels.append(v + "%")
        plt.pie(age_dict.values(), labels=labels)
        plt.savefig('images/age_pie.png')

    def visualize_age_men_line(self):
        if not self.has_parse_file:
            self.parse_csv_file()
        plt.figure(figsize=(7, 7))
        plt.title("Male age distribution", )
        # total = 0
        # for v in self.ages_men_dict.values():
        #     total += int(v)
        # labels = []
        # for k in self.ages_men_dict.keys():
        #     labels.append("%s - %.2f" % (k, int(k) / total))
        plt.pie(sorted(self.ages_men_dict.values()), labels=sorted(self.ages_men_dict.keys()))
        # plt.legend()
        plt.savefig('images/age_men_pie.png')


if __name__ == "__main__":
    v = Visualizer("/home/allen/PycharmProjects/datas/www89yn_data/info.csv")
    v.parse_csv_file()
    # v.visualize_age_line()
    # v.visualize_age_pie()
    v.visualize_age_men_line()
