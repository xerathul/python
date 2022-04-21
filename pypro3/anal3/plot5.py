#주식 데이터 읽어 시각화
#yahoo 사이트 제공
#pip install pandas_datareader

from pandas_datareader import data
import pandas as pd
import matplotlib.pyplot as plt

kosdaq = pd.read_pickle('./kosdaq.pickle')
kospi = pd.read_pickle('./kospi.pickle')
print(kosdaq.head(10))
print(kospi.head(10))

print('-------------')

start_date ="2018-01-01"
tickers = ['003380.KQ', '251270.KS']
holding_df= data.get_data_yahoo(tickers[0],start_date)
net_df= data.get_data_yahoo(tickers[1],start_date)
print(holding_df.head(3),len(holding_df))
print()
print(net_df.head(3),len(net_df))

#읽은 자료 파일로 저장
holding_df.to_pickle('holding.pickle')
net_df.to_csv('net.csv')
net_df.to_html('net.html')

#시각화
plt.plot(net_df)
plt.show()

import seaborn as sns
sns.scatterplot(x='Open', y='Close', data=net_df)
plt.show()