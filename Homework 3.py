class Horse:                                                             #Объявили класс в последсвтии он стал родительским для Eagle.
    def __init__(self):                                                  #Атрибуты класса.
        self.x_distance = 0                                              #2
        self.sound = 'Frrr'

    def run(self, dx):                                                   #Метод бега для лошади.
        self.x_distance = + dx
        return self.x_distance


class Eagle(Horse):                                                      #Здесь объявляем дк.
    def __init__(self):                                                  #Его инит.
        super().__init__()                                               #Тут начинается садомазо с передачей нашего инита из рк в дк орёл, а в последствии в дк пегас.
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):                                                   #Метод полёта для орла.
        self.y_distance = + dy
        return self.y_distance


class Pegasus(Eagle):                                                    #Пегас который украл атрибуты наших 2 классов выше.
    def __init__(self):                                                  #Инит для него.
        super().__init__()                                               #Еще один супер который передает уже переданные для орла атрибуты и методы и так же атр и мет от орла.

    def move(self, dx, dy):                                              #Метод движения которому переданы методы наших двух классов.
        super().fly(dx)
        super().run(dy)

    def get_pos(self):                                                   #Метод возврата X и Y.
        return self.x_distance, self.y_distance

    def voice(self):                                                     #Метод вывода саунда, выводит первое значение из наследования(то есть из Eagle).
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())                                                      #Проверочное, тех. заданию соответсвует.
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
