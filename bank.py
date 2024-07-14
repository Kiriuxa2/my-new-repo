"""
Напишите программу банкомат.
✔ /Начальная сумма равна нулю
✔ /Допустимые действия: пополнить, снять, выйти
✔ /Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""


class Bankomat():
    def __init__(self):
        self.balance = 0  # баланс экземпляра банкомат
        self.quantity = 0

    def cnat(self, money):
        if self.check1(money) and self.check2(money):
            self.balance -= money

    def vnesti(self, money):
        if self.check1(money):
            self.balance += money

        """ разбить один метод проверки на несколько """
    def check1(self, money):
        # добавить в метод остальные проверки: налоги, кратность и перебор
        return not money % 50
            
    def check2(self,money):
        if money > self.balance:
            return False
        
    def check3(self):
        if self.quantity % 3:
            self.balance += (self.balance / 100 * 3)  # тут не balance

    def check4(self):
        if balance >= 5_000_000:
            self.balance -= self.balance * 0.1

    def take_off_percent(self,money):
        percent = money / 100 * 15  
        if percent < 30:
            money -= 30
        elif percent > 600:
            money -= 600
        else:
            money -= percent


user_in = int(input('Команда: 1 - пополнить,2 - снять, 3 - выйти '))
balance = Bankomat()

while user_in != 3:
    if user_in == 1:
        money = int(input('Сумма пополнения:'))
        balance.vnesti(money)
    elif user_in == 2:
        money = int(input('Сумма снятия'))
        balance.cnat(money)
        Bankomat.take_off_percent(money)

    balance.quantity += 1  # объект
    Bankomat.check3()
    Bankomat.check4()
    print('Баланс: ', balance)
    user_in = int(input('Команда:(1 - пополнить,2 - снять, 3 - выйти,'))
