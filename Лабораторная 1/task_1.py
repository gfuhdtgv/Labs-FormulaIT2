# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union

class Facebook:
    def __init__(self, user, password):
        """
        конструктор для класса фэйсбук, атрибуты имя пользователя, пароль.
        """
        self.user = user
        self.password = password

    def login(self):
        """
        Функция для входа в систему, возвращается сообщение о входе

        >>> f = Facebook("Иван", "1234")
        >>> f.login()
        """
        return f'{self.user} вошел в сеть.'

    def post_status(self, status):
        """
        Публикация статуса
        >>> f = Facebook("Иван", "1234")
        >>> f.post_status("Hello, world!")
        """
        return f'{self.user} запостил: {status}'

class Pineapple:
    def __init__(self, color, weight):
        """
        цвет и вес ананаса
        """
        self.color = color
        self.weight = weight

    def eat(self):
        """
        Функция съесть...
        >>> p = Pineapple("Желтый", 1.5)
        >>> p.eat()
        """
        return f' {self.color} Ананас съеден.'

class Laptop:
    def __init__(self, brand: str, model: str, ram: int):
        self.brand = brand
        self.model = model
        self.ram = ram

    def turn_on(self):
        """
        Включает ноутбук
        >>> laptop = Laptop('Apple', 'MacBook Pro', 16)
        >>> laptop.turn_on()
        """
        print("Запущен")

    def turn_off(self):
        """
        Выключает ноутбук

        >>> laptop = Laptop('Apple', 'MacBook Pro', 16)
        >>> laptop.turn_off()
        """
        print("Завершение работы компьютера...")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
