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
        if self.check(money):
            self.bank -= money
        # переделать элиф
        
    def vnesti(self, money):
        if self.check(money):
            self.bank += money

    def check(self, money):
        # добавить в метод остальные проверки: налоги, кратность и перебор
        if not money % 50:
            return False
        if money > bank:
            return False
        '''
        if bank >= 5000000:
            money / 10%
        '''
    
    


user_in = int(input('Команда: 1 - пополнить,2 - снять, 3 - выйти '))
bank = Bankomat()
print('Баланс: ', bank)
while user_in != 3:
    # переделать!!!
    if user_in == 1:
        money = int(input('Сумма пополнения:'))
        bank.vnesti(money)
        print(bank)
        user_in = int(input('Команда:(1 - пополнить,2 - снять, 3 - выйти,'))
    elif user_in == 2:
        money = int(input('Сумма снятия'))
        bank.cnat(money)
        print(bank)
        user_in = int(input('Команда:(1 - пополнить,2 - снять, 3 - выйти,'))
