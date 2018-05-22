import csv

from matplotlib import pyplot

ages = []
genders = []
heights = []
weights = []
educations = []
marriages = []
live_cities = []
origins = []

ages_dict = {}
for i in range(10, 50):
    ages_dict[i] = 0
with open("/home/allen/PycharmProjects/datas/www89yn_data/info.csv", mode="rt", encoding="utf8", buffering=8192) as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        # ages.append(row[0])
        ages_dict[int(row[3].replace('岁', ''))] += 1

x = ages_dict.keys()
y = ages_dict.values()

for k, v in ages_dict.items():
    print("%d--->%s" % (k, v))

pyplot.plot(x, y)
pyplot.xlabel("Age")
pyplot.show()
