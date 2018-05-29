import csv
import os
from collections import Counter, OrderedDict

import matplotlib.pyplot as plt
from prettytable import PrettyTable


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
        self.service_types_dict = None
        self.service_types_men_dict = None
        self.service_types_women_dict = None

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

        def callback(row):
            age = str(row[3].replace('岁', ''))
            gender = row[2].strip()
            education = row[9].strip()
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
            if gender == "男":
                ages_men.append(age)
                educations_men.append(education)
                origins_men.append(origin)
                service_types_men.extend(services)
            elif gender == "女":
                ages_women.append(age)
                educations_women.append(education)
                origins_women.append(origin)
                service_types_women.extend(services)
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

        self.has_parse_file = True

    def _read_csv_file(self, parse_line_callback):
        with open(self.csv_file, mode="rt", encoding="utf8", buffering=8192) as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                parse_line_callback(row)

    @staticmethod
    def _total_value(values):
        total = 0
        for v in values:
            total += int(v)
        return total

    def plot_age_line(self):
        if not self.has_parse_file:
            self.parse_csv_file()
        plt.figure(figsize=(10, 7))
        plt.title('Age distribution line chart')
        plt.plot(self.ages_dict.keys(), self.ages_dict.values())
        plt.xlabel('Age')
        plt.savefig("images/age_line.png")

    def plot_age_pie(self):
        self._plot_pie("Age distribution pie chart", self.ages_dict, "age_pie.png")

    def plot_age_men_pie(self):
        self._plot_pie("Male age distribution pie chart", self.ages_men_dict, "age_men_pie.png")

    def plot_age_women_pie(self):
        self._plot_pie("Female age distribution pie chart", self.ages_women_dict, "age_women_pie.png")

    def print_age_table(self):
        self._print_table(["Age", "Count", "Percent"], "Age distribution table", self.ages_dict)

    def print_age_men_table(self):
        self._print_table(["Age", "Count", "Percent"], "Male age distribution table", self.ages_men_dict)

    def print_age_women_table(self):
        self._print_table(["Age", "Count", "Percent"], "Female age distribution table", self.ages_women_dict)

    def _plot_pie(self, title, collection, filename, rotatelabels=False):
        if not self.has_parse_file:
            self.parse_csv_file()
        total = self._total_value(collection.values())
        plt.figure(figsize=(7, 7))
        plt.title(title)
        labels = []
        for k, v in collection.items():
            v = "%s - %.2f" % (k, int(v) / total * 100)
            labels.append(v + "%")
        plt.pie(collection.values(), labels=labels, rotatelabels=rotatelabels)
        plt.savefig(os.path.join("images", filename))

    def plot_service_types_pie(self):
        self._plot_pie("Service types distribution pie chart", self.service_types_dict, "service_types_pie.png")

    def plot_service_types_men_pie(self):
        self._plot_pie("Male service types distribution pie chart", self.service_types_men_dict,
                       "service_types_men_pie.png")

    def plot_service_types_women_pie(self):
        self._plot_pie("Female service types distribution pie chart", self.service_types_women_dict,
                       "service_types_women_pie.png")

    def _print_table(self, columns, header, collection):
        print("=====" + header)
        table = PrettyTable(columns)
        table.align[columns[0]] = "l"
        table.padding_width = 1
        total = self._total_value(collection.values())
        for k, v in collection.items():
            p = "%.2f" % (int(v) / total * 100)
            table.add_row([k, v, p])
        print(table)
        print("Total: %d" % total)

    def print_service_types_table(self):
        self._print_table(["Type", "Count", "Percent"], "Service types distribution table", self.service_types_dict)

    def print_service_types_men_table(self):
        self._print_table(["Type", "Count", "Percent"], "Male service types distribution table",
                          self.service_types_men_dict)

    def print_service_types_women_table(self):
        self._print_table(["Type", "Count", "Percent"], "Female service types distribution table",
                          self.service_types_women_dict)

    def plot_edu_pie(self):
        self._plot_pie("Education distribution pie chart", self.educations_dict, "edu_pie.png")

    def plot_edu_men_pie(self):
        self._plot_pie("Male education distribution pie chart", self.educations_men_dict, "edu_men_pie.png")

    def plot_edu_women_pie(self):
        self._plot_pie("Female education distribution pie chart", self.educations_women_dict, "edu_women_pie.png")

    def print_edu(self):
        self._print_table(columns=["Education", "Count", "Percent"], header="Education distribution table",
                          collection=self.educations_dict)

    def print_edu_men(self):
        self._print_table(columns=["Education", "Count", "Percent"], header="Male education distribution table",
                          collection=self.educations_men_dict)

    def print_edu_women(self):
        self._print_table(columns=["Education", "Count", "Percent"], header="Female education distribution table",
                          collection=self.educations_women_dict)

    def plot_origin_pie(self):
        self._plot_pie("Origin distribution pie chart", self.origin_dict, "origin_pie.png")

    def plot_origin_men_pie(self):
        self._plot_pie("Male origin distribution pie chart", self.origin_men_dict, "origin_men_pie.png")

    def plot_origin_women_pie(self):
        self._plot_pie("Female origin distribution pie chart", self.origin_women_dict, "origin_women_pie.png")

    def print_origin(self):
        self._print_table(["Origin", "Count", "Percent"], "Origin distribution table", self.origin_dict)

    def print_origin_men(self):
        self._print_table(["Origin", "Count", "Percent"], "Male origin distribution table", self.origin_men_dict)

    def print_origin_women(self):
        self._print_table(["Origin", "Count", "Percent"], "Female origin distribution table", self.origin_women_dict)


if __name__ == "__main__":
    v = Visualizer("/home/allen/PycharmProjects/datas/www89yn_data/info.csv")
    v.parse_csv_file()

    v.plot_age_line()
    v.plot_age_pie()
    v.plot_age_men_pie()
    v.plot_age_women_pie()
    v.print_age_table()
    v.print_age_men_table()
    v.print_age_women_table()

    v.plot_service_types_pie()
    v.plot_service_types_men_pie()
    v.plot_service_types_women_pie()
    v.print_service_types_table()
    v.print_service_types_men_table()
    v.print_service_types_women_table()

    v.plot_edu_pie()
    v.plot_edu_men_pie()
    v.plot_edu_women_pie()
    v.print_edu()
    v.print_edu_men()
    v.print_edu_women()

    v.plot_origin_pie()
    v.plot_origin_men_pie()
    v.plot_origin_women_pie()
    v.print_origin()
    v.print_origin_men()
    v.print_origin_women()
