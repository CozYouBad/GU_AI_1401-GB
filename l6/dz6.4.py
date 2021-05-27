class Car:
    # атрибуты
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # методы
    def go(self):
        return f'{self.name} тронулась'

    def stop(self):
        return f'{self.name} стоит'

    def turn_right(self):
        return f'{self.name} повёрнута направо'

    def turn_left(self):
        return f'{self.name} повёрнута налево'

    def show_speed(self):
        return f'Текущая скорость марки {self.name} : {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городской машины марки {self.name} : {self.speed}')

        if self.speed > 40:
            return f'Скорость марки {self.name} выше, чем разрешено для городской машины'
        else:
            return f'Скорость марки {self.name} нормальная для городской машины'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочей машины марки {self.name} : {self.speed}')

        if self.speed > 60:
            return f'Скорость марки {self.name} выше, чем разрешено для рабочей машины'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из управления полиции'
        else:
            return f'{self.name} не из управления полиции'


audi = SportCar(100, 'Красная', 'Audi', False)
oka = TownCar(30, 'Белая', 'Oka', False)
lada = WorkCar(70, 'Розовая', 'Lada', True)
ford = PoliceCar(110, 'Голубая',  'Ford', True)
print(lada.turn_left())
print(f'Когда {oka.turn_right()}, тогда {audi.stop()}')
print(f'{lada.go()} с определённой скоростью {lada.show_speed()}')
print(f'{lada.name} - {lada.color}')
print(f'{audi.name} - полицейская машина? {audi.is_police}')
print(f'{lada.name} - полицейская машина? {lada.is_police}')
print(audi.show_speed())
print(oka.show_speed())
print(ford.police())
print(ford.show_speed())