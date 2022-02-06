from random import choice

BLACK = 0
WHITE = 1

bag1 = [BLACK, WHITE]
bag2 = [BLACK, BLACK]

exps = 1000000


total = 0
good = 0
for _ in range(exps):
    bag = choice([bag1, bag2])
    ball = choice(bag)
    if ball == BLACK:
        total += 1
        good += all([ball == BLACK for ball in bag])

print(f"Calculated probability in {exps} simulations is: {good / total}")

