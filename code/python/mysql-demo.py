import time
import datetime
import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Float,DateTime
from sqlalchemy.orm import sessionmaker
import matplotlib
matplotlib.use('TKAgg')
# matplotlib.use('WXAgg')

import matplotlib.pyplot as plt
import numpy as np
# import statsmodels
import talib
from talib import MA_Type


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='./log.txt',
                    filemode='w')
logger = logging.getLogger(__name__)

engine = create_engine("mysql+pymysql://")
# 创建会话
session = sessionmaker(engine)
mySession = session()

Base = declarative_base()


class History(Base):
    __tablename__='history'
    id = Column(Integer,primary_key=True,autoincrement=True)
    symbol = Column(String(255))
    timestamp = Column(Integer)
    time_cn = Column(DateTime)
    time_utc = Column(DateTime)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)
    time_frame = Column(String)
    gmt_create = Column(DateTime)
btc = 'BTC/USD'
btc18z = 'XBTZ18'
btc19M = 'XBTM19'
btc19H = 'XBTH19'

btc_list = mySession.query(History.id,History.symbol,History.timestamp,History.time_cn,History.close).filter(History.symbol == btc).order_by(History.id).all()
btc18z_list = mySession.query(History.id,History.symbol,History.timestamp,History.time_cn,History.close).filter(History.symbol == btc18z).order_by(History.id).all()
btc19M_list = mySession.query(History.id,History.symbol,History.timestamp,History.time_cn,History.close).filter(History.symbol == btc19M).order_by(History.id).all()
btc19H_list = mySession.query(History.id,History.symbol,History.timestamp,History.time_cn,History.close).filter(History.symbol == btc19H).order_by(History.id).all()

print('btc_list is {}'.format(btc_list))

x_time = []
btc_close = []
for btc in btc_list:
    # x_time.append(btc.timestamp)
    x_time.append(btc.time_cn)
    btc_close.append(btc.close)

# list转数组
x = np.array(x_time)
btc_close_array = np.array(btc_close)

"""
BBANDS(real[, timeperiod=?, nbdevup=?, nbdevdn=?, matype=?])

    Bollinger Bands (Overlap Studies)

    Inputs:
        real: (any ndarray)
    Parameters:
        timeperiod: 5
        nbdevup: 2
        nbdevdn: 2
        matype: 0 (Simple Moving Average)
    Outputs:
        upperband
        middleband
        lowerband
"""
upper, middle, lower = talib.BBANDS(btc_close_array,matype=MA_Type.T3)

# mom = talib.MOM(close, timeperiod=5)

plt.plot(x,btc_close,'r',label='close')
plt.plot(x,upper,'g',label='upper')
plt.plot(x,middle,'b',label='middle')
plt.plot(x,lower,'y',label='lower')
plt.grid()
plt.xlabel('timstamp') # 给 x 轴添加标签
plt.ylabel('BTC/USD future price') # 给 y 轴添加标签
plt.title('bitmex BTC/USD future boll line') # 添加图形标题

plt.legend()
plt.show()