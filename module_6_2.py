class Vehicle:
    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__color = __color
        self.__engine_power = __engine_power

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return  f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):

        return f"Цвет: {self.__color}"

    def print_info(self):
        print(Vehicle.get_model)
        print(Vehicle.get_horsepower)
        print(Vehicle.get_color)
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):

        new_color = new_color.lower()
        for i in Vehicle.__COLOR_VARIANTS:
            if new_color == i.lower:
                self.__color = new_color
            else:
                return
            print(f"Нельзя сменить цвет на {new_color}]")


class Sedan(Vehicle):

    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
print(vehicle1)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()


print(dir(Vehicle))
print(dir(Sedan))


