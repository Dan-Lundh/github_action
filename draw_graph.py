import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.DataFrame({"x": np.array([1, 2, 3]), "y": np.array([2, 5, 8])})

print(df)

plt.plot(df["x"], df["y"])


# hej 2

plt.show()
