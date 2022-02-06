from math import inf
from datetime import datetime

n, d = map(int, input().split())

start_time = datetime.now()

data = []
for _ in range(n):
    _in = input().split()
    x = list(map(float, _in[:-1]))
    y = int(_in[-1])
    data.append((x,y))
data = [([1] + x, y) for x,y in data]

w = [0]*(d+1)
perceptron =  lambda w, x: 1 if sum([a*b for a,b in zip(w, x)]) >=0 else -1

best_w = None
best_incorrect = inf
while True:
    incorrect = [(x,y) for x,y in data if perceptron(w,x)!=y]
    if len(incorrect) < best_incorrect:
        best_incorrect = len(incorrect)
        best_w = w 
    if len(incorrect) == 0 or (datetime.now()-start_time).total_seconds() * 1000 > 2900:
        break

    xw, yw = incorrect[0]
    w = [a + b if yw > 0 else a - b for a,b in zip(w, xw)]

print(" ".join([str(x) for x in best_w]))
