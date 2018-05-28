import csv
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
        if not self.has_parse_file:
            self.parse_csv_file()
        # age_dict = self._age_dict()
        total = self._total_value(self.ages_dict.values())
        plt.figure(figsize=(7, 7))
        plt.title('Age distribution pie chart')
        labels = []
        for k in self.ages_dict.keys():
            v = "%s - %.2f" % (k, (int(self.ages_dict[k]) / total * 100))
            labels.append(v + "%")
        plt.pie(self.ages_dict.values(), labels=labels)
        plt.savefig('images/age_pie.png')

    def plot_age_men_pie(self):
        if not self.has_parse_file:
            self.parse_csv_file()
        plt.figure(figsize=(8, 8))
        plt.title("Male age distribution", )
        total = self._total_value(self.ages_men_dict.values())
        labels = []
        for k in self.ages_men_dict.keys():
            label = "%s - %.2f" % (k, (int(self.ages_men_dict[k]) / total * 100))
            labels.append(label + "%")
        plt.pie(self.ages_men_dict.values(), labels=labels)
        plt.savefig('images/age_men_pie.png')

    def plot_age_women_pie(self):
        if not self.has_parse_file:
            self.parse_csv_file()
        plt.figure(figsize=(8, 8))
        plt.title("Female age distribution", )
        total = self._total_value(self.ages_women_dict.values())
        labels = []
        for k in self.ages_women_dict.keys():
            label = "%s - %.2f" % (k, (int(self.ages_women_dict[k]) / total * 100))
            labels.append(label + "%")
        plt.pie(self.ages_women_dict.values(), labels=labels)
        plt.savefig('images/age_women_pie.png')

    def print_age_table(self):
        print("======Age distribution table")
        table = PrettyTable(["Age", "Count", "Percent"])
        table.align["Age"] = "l"
        table.padding_width = 1
        total = self._total_value(self.ages_dict.values())
        for k, v in self.ages_dict.items():
            p = "%.2f" % (int(v) / total * 100)
            table.add_row([k, v, p])
        print(table)
        print("Total: %d" % total)

    def print_age_men_table(self):
        print("======Male age distribution table")
        table = PrettyTable(["Age", "Count", "Percent"])
        table.align["Age"] = "l"
        table.padding_width = 1
        total = self._total_value(self.ages_men_dict.values())
        for k, v in self.ages_men_dict.items():
            p = "%.2f" % (int(v) / total * 100)
            table.add_row([k, v, p])
        print(table)
        print("Total: %d" % total)

    def print_age_women_table(self):
        print("======Female age distribution table")
        table = PrettyTable(["Age", "Count", "Percent"])
        table.align["Age"] = "l"
        table.padding_width = 1
        total = self._total_value(self.ages_women_dict.values())
        for k, v in self.ages_women_dict.items():
            p = "%.2f" % (int(v) / total * 100)
            table.add_row([k, v, p])
        print(table)
        print("Total: %d" % total)

    def plot_service_types_pie(self):
        if not self.has_parse_file:
            self.parse_csv_file()
        total = self._total_value(self.service_types_dict.values())
        plt.figure(figsize=(7, 7))
        plt.title('Service types distribution pie chart')
        labels = []
        for k, v in self.service_types_dict.items():
            v = "%s - %.2f" % (k, int(v) / total * 100)
            labels.append(v + "%")
        plt.pie(self.service_types_dict.values(), labels=labels)
        plt.savefig('images/service_types_pie.png')

    def plot_service_types_men_pie(self):
        if not self.has_parse_file:
            self.parse_csv_file()
        total = self._total_value(self.service_types_men_dict.values())
        plt.figure(figsize=(7, 7))
        plt.title('Service types distribution pie chart')
        labels = []
        for k, v in self.service_types_men_dict.items():
            v = "%s - %.2f" % (k, int(v) / total * 100)
            labels.append(v + "%")
        plt.pie(self.service_types_men_dict.values(), labels=labels)
        plt.savefig('images/service_types_men_pie.png')

    def plot_service_types_women_pie(self):
        if not self.has_parse_file:
            self.parse_csv_file()
        total = self._total_value(self.service_types_women_dict.values())
        plt.figure(figsize=(7, 7))
        plt.title('Service types distribution pie chart')
        labels = []
        for k, v in self.service_types_women_dict.items():
            v = "%s - %.2f" % (k, int(v) / total * 100)
            labels.append(v + "%")
        plt.pie(self.service_types_women_dict.values(), labels=labels)
        plt.savefig('images/service_types_women_pie.png')

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
        self._print_table(["Type", "Count", "Percent"],
                          "Service types distribution table",
                          self.service_types_dict)

    def print_service_types_men_table(self):
        self._print_table(["Type", "Count", "Percent"],
                          "Male service types distribution table",
                          self.service_types_men_dict)

    def print_service_types_women_table(self):
        self._print_table(["Type", "Count", "Percent"],
                          "Female service types distribution table",
                          self.service_types_women_dict)


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
