import matplotlib.pyplot as plt

with open('losses.txt') as f:
    lines = f.readlines()
    x = [line.split()[0] for line in lines]
    y = [line.split()[1] for line in lines]

plt.plot(x ,y)
plt.savefig("losses_plot.png")
