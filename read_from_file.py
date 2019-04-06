import create_dataframe as pd
import matplotlib.pyplot as plt


df = pd.read_csv('/home/kluz/allan.csv',names=['company','raisedAmt'])
print(df)
plt.plot(df)
plt.show()
