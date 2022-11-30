
# Не понял пояснения к этой задаче. Результат получается верный, но не уверен, что правильно написал конструктор и метод

import random
n = int(input())
coins_list = []
head_list = []
i = n
class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        random_list = ['head', 'tail']
        random_choice = random.choice(random_list)
        return random_choice
while n <= 0:
    print('Количество монет не может быть отрицательным или равняться нулю!')
    n = int(input())
while i > 0:
    coins_list.append(Coin.flip(0))
    i -= 1
for coin in coins_list:
    if coin == 'head':
        head_list.append(coin)
print(f"Аверс: ", ((len(head_list)*100)//n), f"%", f"Реверс: ", 100-(len(head_list)*100)//n, f"%")

# Задание:
# 1. Создайте список из n-монеток, n - вводится с клавиатуры
# 2. Подбросьте(flip) все монетки. У каждой монетки в списке вызовите метод .flip()
# 3. Выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())
