"""
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""


class Bankomat():
    def __init__(self):
        self.bank = 0

    def cnat(self, money):
        self.bank -= money

    def vnesti(self, money):
        self.bank += money

    def check(self, money):
        # добавить в метод остальные проверки: налоги, кратность и перебор
        result = True
        if not money % 50:
            self.cnat(money)
        if money > bank:
            ...
        '''
        if bank >= 5_000_000:
            self.bank -= self.bank * 0.1
        '''
        return result


user_in = int(input('Команда: 1 - пополнить,2 - снять, 3 - выйти '))
bank = Bankomat()
while user_in != 3:
    # переделать!!!
    if user_in == 1:
        money = int(input('Сумма пополнения:'))
        bank.vnesti(money)
    elif user_in == 2:
        money = int(input('Сумма снятия'))
        bank.cnat(money)
    print('Баланс: ', bank)
    user_in = int(input('Команда:(1 - пополнить,2 - снять, 3 - выйти,'))
