import os

import matplotlib.pyplot as plt


class ImageGenerator:

    def __init__(self, ages, services, educations, origins, cities):
        self.ages_all_dict = ages[0]
        self.ages_men_dict = ages[1]
        self.ages_women_dict = ages[2]
        self.services_all_dict = services[0]
        self.services_men_dict = services[1]
        self.services_women_dict = services[2]
        self.edus_all_dict = educations[0]
        self.edus_men_dict = educations[1]
        self.edus_women_dict = educations[2]
        self.origins_all_dict = origins[0]
        self.origins_men_dict = origins[1]
        self.origins_women_dict = origins[2]
        self.cities_all_dict = cities[0]
        self.cities_men_dict = cities[1]
        self.cities_women_dict = cities[2]

    @staticmethod
    def _total_value(values):
        total = 0
        for v in values:
            total += int(v)
        return total

    def plot_age_line(self):
        plt.figure(figsize=(10, 7))
        plt.title('Age distribution line chart')
        plt.plot(self.ages_all_dict.keys(), self.ages_all_dict.values())
        plt.xlabel('Age')
        plt.savefig("images/age_line.png")

    def plot_age_pie(self):
        self._plot_pie("Age distribution pie chart", self.ages_all_dict, "age_pie.png")

    def plot_age_men_pie(self):
        self._plot_pie("Male age distribution pie chart", self.ages_men_dict, "age_men_pie.png")

    def plot_age_women_pie(self):
        self._plot_pie("Female age distribution pie chart", self.ages_women_dict, "age_women_pie.png")

    def _plot_pie(self, title, collection, filename, rotatelabels=False):
        total = self._total_value(collection.values())
        plt.figure(figsize=(7, 7))
        plt.title(title)
        labels = []
        for k, v in collection.items():
            v = "%s - %.2f" % (k, int(v) / total * 100)
            labels.append(v + "%")
        plt.pie(collection.values(), labels=labels, rotatelabels=rotatelabels)
        plt.savefig(os.path.join(os.path.dirname(__file__), "images", filename))

    def plot_service_types_pie(self):
        self._plot_pie("Service types distribution pie chart", self.services_all_dict, "service_types_pie.png")

    def plot_service_types_men_pie(self):
        self._plot_pie("Male service types distribution pie chart", self.services_men_dict,
                       "service_types_men_pie.png")

    def plot_service_types_women_pie(self):
        self._plot_pie("Female service types distribution pie chart", self.services_women_dict,
                       "service_types_women_pie.png")

    def plot_edus_pie(self):
        self._plot_pie("Educations distribution pie chart", self.edus_all_dict, "educations_pie.png")

    def plot_edus_men_pie(self):
        self._plot_pie("Male educations distribution pie chart", self.edus_men_dict, "educations_men_pie.png")

    def plot_edus_women_pie(self):
        self._plot_pie("Female educations distribution pie chart", self.edus_women_dict, "educations_women.png")

    def plot_origins_pie(self):
        self._plot_pie("Origins distribution pie chart", self.origins_all_dict, "origins_pie.png")

    def plot_origins_men_pie(self):
        self._plot_pie("Male origins distribution pie chart", self.origins_men_dict, "origins_men_pie.png")

    def plot_origins_women_pie(self):
        self._plot_pie("Female origins distribution pie chart", self.origins_women_dict, "origins_women.png")

    def plot_cities_pie(self):
        self._plot_pie("Cities distribution pie chart", self.cities_all_dict, "cities_pie.png")

    def plot_cities_men_pie(self):
        self._plot_pie("Male cities distribution pie chart", self.cities_men_dict, "cities_men_pie.png")

    def plot_cities_women_pie(self):
        self._plot_pie("Female cities distribution pie chart", self.cities_women_dict, "cities_women_pie.png")

    def gen_images(self):
        self.plot_age_pie()
        self.plot_age_men_pie()
        self.plot_age_women_pie()
        self.plot_service_types_pie()
        self.plot_service_types_men_pie()
        self.plot_service_types_women_pie()
        self.plot_edus_pie()
        self.plot_edus_men_pie()
        self.plot_edus_women_pie()
        self.plot_origins_pie()
        self.plot_origins_men_pie()
        self.plot_edus_women_pie()
        self.plot_cities_pie()
        self.plot_cities_men_pie()
        self.plot_cities_women_pie()
