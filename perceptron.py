from math import inf, ceil
from datetime import datetime
from random import shuffle, choice


def random_split_data(data, ratio):
    shuffle(data)
    m = ceil(ratio * len(data))
    return data[:m], data[m:]


def calculate_initial_w(data):
    positives = [p for p, label in data if label == 1]
    negatives = [p for p, label in data if label == -1]
    d = len(positives[0])
    w = []
    avg_points = []
    for i in range(d):
        avg_pos_xi = sum([p[i] for p in positives]) / len(positives)
        avg_neg_xi = sum([p[i] for p in negatives]) / len(negatives)

        w.append(avg_pos_xi - avg_neg_xi)
        avg_points.append((avg_pos_xi, avg_neg_xi))

    w0 = sum([-(pi ** 2 - ni ** 2) / 2 for pi, ni in avg_points])

    return [w0] + w


n, d = map(int, input().split())

start_time = datetime.now()

data = []
for _ in range(n):
    _in = input().split()
    x = list(map(float, _in[:-1]))
    y = int(_in[-1])
    data.append((x, y))

w = calculate_initial_w(data)
data = [([1] + x, y) for x, y in data]

train, test = random_split_data(data, 0.7)

perceptron = lambda w, x: 1 if sum([a * b for a, b in zip(w, x)]) >= 0 else -1

best_w = None
best_incorrect = inf

while (datetime.now() - start_time).total_seconds() * 1000 < 2800:
    incorrect = [(x, y) for x, y in train if perceptron(w, x) != y]
    eval_incorrect = [(x, y) for x, y in test if perceptron(w, x) != y]

    if len(incorrect) == 0:
        break
    if len(eval_incorrect) < best_incorrect:
        best_incorrect = len(eval_incorrect)
        best_w = w

    # xw, yw = incorrect[0]
    xw, yw = choice(incorrect)
    w = [a + b if yw > 0 else a - b for a, b in zip(w, xw)]

print(" ".join([str(x) for x in best_w]))
