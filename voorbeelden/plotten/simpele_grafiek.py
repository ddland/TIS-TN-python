#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

# TN_code version > 1.1
from TN_code import TISTNplot as TN

x = np.arange(100)
y = 3 * x + 4

formatterX = TN.TNFormatter(4)
formatterY = TN.TNFormatter(2)

fig, ax = plt.subplots()  # 1 figuur
ax.yaxis.set_major_formatter(formatterY)
ax.xaxis.set_major_formatter(formatterX)

plt.plot(x, y)
TN.label_x("t", "s", ax, text="tijd ")
TN.label_y("v", "m/s", ax, text="snelheid ")

plt.grid()
plt.tight_layout()
plt.savefig("voorbeeld.png", dpi=300)  # of sla op als pdf!
plt.show()
