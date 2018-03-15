import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt

%matplotlib inline

start=datetime.datetime(1970, 5,16)
end  =datetime.datetime(2018, 2,28)
nikkei225=web.DataReader('NIKKEI225', 'fred', start, end)

plt.plot(nikkei225)
