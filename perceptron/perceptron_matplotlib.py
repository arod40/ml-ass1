n, d = map(int, input().split())

data = []
for _ in range(n):
    _in = input().split()
    x = list(map(float, _in[:-1]))
    y = int(_in[-1])
    data.append((x,y))
data = [([1] + x, y) for x,y in data]

w = [0]*(d+1)
perceptron =  lambda w, x: 1 if sum([a*b for a,b in zip(w, x)]) >=0 else -1

it = 10000
for i in range(it):
    incorrect = [(x,y) for x,y in data if perceptron(w,x)!=y]
    if len(incorrect) == 0:
        break

    xw, yw = incorrect[0]
    w = [a + b if yw > 0 else a - b for a,b in zip(w, xw)]

import matplotlib.pyplot as plt

TRUE = [x[1:] for x,y in data if y == 1]
TRUE_X = [a for a,_ in TRUE]
TRUE_Y = [b for _,b in TRUE]
FALSE = [x[1:] for x,y in data if y == -1]
FALSE_X = [a for a,_ in FALSE]
FALSE_Y = [b for _,b in FALSE]
plt.scatter(TRUE_X,TRUE_Y)
plt.scatter(FALSE_X,FALSE_Y,marker="x")
plt.show()

print(i)
print(len(incorrect))
print(" ".join([str(x) for x in w]))
