import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("breastcancer.csv")
plt.plot(df['radius_mean'], df['diagnosis'], 'bo')