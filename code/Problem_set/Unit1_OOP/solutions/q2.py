class Car:
    color = 'gray'
    def describCar(self):
        return 'A color ' + Car.color + ' car'
    def describeSelf(self):
        return 'A cool ' + self.color + ' car'


nona = Car()
result = nona.describCar()  # A cool gray car
# print(result)