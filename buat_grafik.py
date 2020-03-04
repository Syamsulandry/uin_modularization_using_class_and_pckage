import matplotlib.pyplot as plt

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs', 'Man'

data = [15, 30, 45, 10, 30] #grafik

fig, ax1, = plt.subplots() #grafik
ax1.pie(data, labels=labels, shadow=True)
plt.show()