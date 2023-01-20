# Final2022
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

YT = pd.read_csv("Bananas.csv")

YT['Date'] = pd.to_datetime(YT['DATE'],infer_datetime_format=True)

plt.style.available[:20]
plt.style.use('fivethirtyeight')
plt.scatter(YT['Date'],YT['Bananas price per lb'],color='red',
            marker='^')
plt.ylabel('Price per lb')
plt.xlabel('Date')
plt.title('Bananas price in US')
plt.yticks(np.arange(0.56,0.65,0.02))
plt.xticks(size=10)
plt.show()
