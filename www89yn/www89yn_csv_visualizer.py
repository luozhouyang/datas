import csv

import matplotlib.pyplot as plt


class Visualizer:

    def __init__(self, csv_file):
        self.csv_file = csv_file

    def read_csv_file(self, parse_line_callback):
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

        self.read_csv_file(parse_age)
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
            # print(k)
            # print(age_dict[k])
            # print("%.4f" % (age_dict[k] / total))
            v = "%s - %.2f" % (k, (age_dict[k] / total * 100))
            # print(v)
            labels.append(v + "%")
        plt.pie(age_dict.values(), labels=labels)
        plt.savefig('images/age_pie.png')


if __name__ == "__main__":
    v = Visualizer("/home/allen/PycharmProjects/datas/www89yn_data/info.csv")
    v.visualize_age_line()
    v.visualize_age_pie()
