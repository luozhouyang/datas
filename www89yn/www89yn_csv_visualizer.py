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

    def visualize_age_line(self):
        age_dict = {}
        for i in range(15, 50):
            age_dict[i] = 0

        def parse_age(row):
            age_dict[int(row[3].replace('岁', ''))] += 1

        self.read_csv_file(parse_age)
        plt.plot(age_dict.keys(), age_dict.values())
        plt.xlabel('Age')
        plt.show()


if __name__ == "__main__":
    v = Visualizer("/home/allen/PycharmProjects/datas/www89yn_data/info.csv")
    v.visualize_age_line()
