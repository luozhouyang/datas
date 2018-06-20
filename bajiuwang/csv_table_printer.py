from prettytable import PrettyTable


class TablePrinter:

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

    def print_age(self):
        self._print_table(["Age", "Count", "Percent"], "Age distribution table", self.ages_all_dict)

    def print_age_men(self):
        self._print_table(["Age", "Count", "Percent"], "Male age distribution table", self.ages_men_dict)

    def print_age_women(self):
        self._print_table(["Age", "Count", "Percent"], "Female age distribution table", self.ages_women_dict)

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

    def print_service_types(self):
        self._print_table(["Type", "Count", "Percent"], "Service types distribution table", self.services_all_dict)

    def print_service_types_men(self):
        self._print_table(["Type", "Count", "Percent"], "Male service types distribution table",
                          self.services_men_dict)

    def print_service_types_women(self):
        self._print_table(["Type", "Count", "Percent"], "Female service types distribution table",
                          self.services_women_dict)

    def print_edu(self):
        self._print_table(columns=["Education", "Count", "Percent"], header="Education distribution table",
                          collection=self.edus_all_dict)

    def print_edu_men(self):
        self._print_table(columns=["Education", "Count", "Percent"], header="Male education distribution table",
                          collection=self.edus_men_dict)

    def print_edu_women(self):
        self._print_table(columns=["Education", "Count", "Percent"], header="Female education distribution table",
                          collection=self.edus_women_dict)

    def print_origin(self):
        self._print_table(["Origin", "Count", "Percent"], "Origin distribution table", self.origins_all_dict)

    def print_origin_men(self):
        self._print_table(["Origin", "Count", "Percent"], "Male origin distribution table", self.origins_men_dict)

    def print_origin_women(self):
        self._print_table(["Origin", "Count", "Percent"], "Female origin distribution table", self.origins_women_dict)

    def print_cities(self):
        self._print_table(["City", "Count", "Percent"], "Cities distribution table", self.cities_all_dict)

    def print_cities_men(self):
        self._print_table(["City", "Count", "Percent"], "Male cities distribution table", self.cities_men_dict)

    def print_cities_women(self):
        self._print_table(["City", "Count", "Percent"], "Female cities distribution table", self.cities_women_dict)

    def print_tables(self):
        self.print_age()
        self.print_age_men()
        self.print_age_women()
        self.print_service_types()
        self.print_service_types_men()
        self.print_service_types_women()
        self.print_edu()
        self.print_edu_men()
        self.print_edu_women()
        self.print_origin()
        self.print_origin_men()
        self.print_origin_women()
        self.print_cities()
        self.print_cities_men()
        self.print_cities_women()
