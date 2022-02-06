import matplotlib.pyplot as plt

wa = [1,2,3]
wb = [-1,-2,-3]

x1, y1 = [7, -11], [-5, 7]
x2, y2 = [7, -11], [5, -7]
plt.xlim(-5, 5), plt.ylim(-5, 5)
plt.plot(x1, y1, x2,y2)
plt.legend(['w = [1,2,3]', 'w = [-1,-2,-3]'])
plt.show()