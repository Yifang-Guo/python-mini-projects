import matplotlib.pyplot as plt

x = [2, 4, 5]
y = [2, 3, 6]

plt.plot(x, y, color='green',linestyle='dashed',linewidth=3, marker='o',markerfacecolor='blue',markersize=12)

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Demo graph')
plt.show()