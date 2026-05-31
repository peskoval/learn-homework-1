"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    data_1 = input('Enter some data for the first variable: ')
    data_2 = input('Enter some data for the second variable: ')
    if not isinstance(data_1, str) and not isinstance(data_2, str):
        return 0
    elif data_1 == data_2:
        return 1
    elif data_2 == 'learn':
        return 3
    elif len(data_1) > len(data_2):
        return 2


if __name__ == "__main__":
    print(main())
