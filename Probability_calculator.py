import copy
import random


class Hat:

    def __init__(self, **kwargs):
        if not kwargs:
            raise ValueError('Class object must contain at least one argument.')
        else:
            self.contents = [key for key, value in kwargs.items() for v in range(value)]

    def draw(self, draw_num):
        balls_withdrawn = []

        if not isinstance(draw_num, int):
            raise TypeError('The number of balls to draw should be an integer.')

        if draw_num <= 0:
            raise ValueError('The number of balls to draw should be greater than 0.')
        elif draw_num >= len(self.contents):
            balls_withdrawn = copy.deepcopy(self.contents)
            self.contents.clear()
            return balls_withdrawn
        else:
            while draw_num > 0:
                amount_in_hat = len(self.contents)
                x = random.randint(0, amount_in_hat - 1)
                balls_withdrawn.append(self.contents[x])
                del self.contents[x]
                draw_num -= 1
            return balls_withdrawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    counter = 0
    balls_for_exp = [key for key, value in expected_balls.items() for v in range(value)]

    while counter < num_experiments:
        doppelganger = copy.deepcopy(hat)
        t_or_f_list = []
        balls_picked = doppelganger.draw(num_balls_drawn)
        for i in range(len(balls_for_exp)):
            if balls_for_exp.count(balls_for_exp[i]) <= balls_picked.count(balls_for_exp[i]):
                t_or_f_list.append(True)
            else:
                t_or_f_list.append(False)

        if all(t_or_f_list):
            success += 1

        counter += 1
    p = success / num_experiments
    return p


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, expected_balls={'red': 2, 'green': 1}, num_balls_drawn=5, num_experiments=2000)

print('Probability:',probability)