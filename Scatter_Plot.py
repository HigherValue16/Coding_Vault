import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('titanic.csv')
plt.scatter(df['Age'], df['Fare'])