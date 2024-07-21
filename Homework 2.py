class Vehicle:                                                                          #Объявили рк (род. класс).
    def __init__(self, owner, __model, __color, __engine_power):                        #Объявили инициализатор класса.
        self.owner = owner                                                              #Так же переобъявили параметры с ссылкой на них.
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
        self.__COLOR_VARIANTS = ["gray", 'green', 'black', 'white']                     #Объявили список доступных нам цветов.

    def print_info(self):                                                               #Вывод результатов методов.
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'{'Владелец:'} {self.owner}')

    def set_color(self, new_color):                                                     #Метод изменения цвета.
        self.new_color = new_color.lower()
        self.__COLOR_VARIANTS = self.__COLOR_VARIANTS
        if self.new_color in self.__COLOR_VARIANTS:
            self.__color = self.new_color
        else:
            print('Нельзя сменить цвет на', self.new_color)

    def get_model(self):                                                                #Метод возврата значения параметра __model(модель транспорта).
        return (f'{'Модель:'} {self.__model}')

    def get_horsepower(self):                                                           #Метод возврата значения параметра __engine_power(мощность двигателя).
        return (f'{'Мощность двигателя:'} {self.__engine_power}')

    def get_color(self):                                                                #И цвета соответственно.
        return (f'{'Цвет:'} {self.__color}')


class Sedan(Vehicle):                                                                   #ДК(Дочерний класс) класса Vehicle.
    __PASSENGER_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)                #Вызовы для проверки.
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()