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
        self.balance = 0  #баланс экземпляра банкомат
        self.quantity = 0

    def cnat(self, money):
        if self.check(money):
            self.balance -= money
        # переделать элиф
        
    def vnesti(self, money):
        if self.check(money):
            self.balance += money

    def check(self, money):
        # добавить в метод остальные проверки: налоги, кратность и перебор
        result = True
        if not money % 50:
            return False
        if money > self.balance:
            return False
        
        if self.quantity % 3:
            balance += (balance / 100 * 3)

        
        '''
        if balance >= 5_000_000:
            self.bank -= self.bank * 0.1
        '''
        return result

    
    


user_in = int(input('Команда: 1 - пополнить,2 - снять, 3 - выйти '))
balance = Bankomat()
#quantity = Bankomat()
while user_in != 3:
    # переделать!!!
    if user_in == 1:
        money = int(input('Сумма пополнения:'))
        balance.vnesti(money)
        quantity += 1
        user_in = int(input('Команда:(1 - пополнить,2 - снять, 3 - выйти,'))
    elif user_in == 2:
        money = int(input('Сумма снятия'))
        balance.cnat(money)
        quantity += 1
    print('Баланс: ', balance)
    user_in = int(input('Команда:(1 - пополнить,2 - снять, 3 - выйти,'))
