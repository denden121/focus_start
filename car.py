class Car():
    def __init__(self, identifier, model, manufacturer, type_of_body, year):
        self.model = model
        self.type_of_body = type_of_body
        self.manufacturer = manufacturer
        try:
            self.year = int(year)
        except ValueError:
            while True:
                print("Данные не верны, повторите ввод")
                year = input()
                if year.isdigit():
                    self.year = year
                    break
        self.id = identifier

    def __str__(self):
        return str(self.id)+';'+self.manufacturer+';'+self.model+';'+self.type_of_body+';'+str(self.year)+'\n'
    