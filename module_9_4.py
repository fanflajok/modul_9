first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x[0][0] == y[0][0], first, second)))


def get_advanced_writer(file_name):

    def write_everything(*data_set):
        file = open(file_name, 'w', encoding='utf=8')
        for i in data_set:
            file.write(str(i)+ '\n')
    return write_everything
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
import random
class MysticBall:
    def __init__(self, *words):
        self.words = words
    def __call__(self):
        random_element = random.choice(self.words)
        return random_element

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

