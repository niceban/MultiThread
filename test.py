__author__ = 'NealLee'

import pandas as pd
# import plotly.plotly as pp
# from datetime import datetime
from plotly.tools import FigureFactory as FF

class smoother ():

    global  Capitalize

    def __init__(self):
        self.Data = mat.Data = pd.read_csv('/Users/Aha/Desktop/QuantInv/MultiThread/Datas/600033')
        self.Data.columns = map(Capitalize , self.Data.columns)
        pass

    def Captalize(self , s):
        s[0].toupper + s[1:]

    def candlePlot(self):
        FF.create_candlestick(self.open, self.high, self.low, self.close, dates=self.Data)

    def denoise(self):
        pass

    def extractFeatures(self):
        pass

    def rePlot(self):
        pass

    def semi_sp_clustering(self):
        pass

    def clustering(self):
        pass

    def loadTicks(self):
        pass

    def re_Ext_Fea(self):
        pass

    def backTesting(self):
        pass

    def predicting(self):
        pass

    def CV(self):
        pass


# ======================================
import numpy as np
import scipy.fftpack as fft

N = 100
x = np.linspace(0,2*np.pi,N)
y = np.sin(x) + np.random.random(N) * 0.2

w = fft.rfft(y)
f = fft.rfftfreq(N, x[1]-x[0])
spectrum = w**2

cutoff_idx = spectrum < (spectrum.max()/5)
w2 = w.copy()
w2[cutoff_idx] = 0

y2 = fft.irfft(w2)

# ------------------------------------

if __name__ == "__main__":

    mat = smoother()
    print mat.Data.ix[1:10,:]
    mat.candlePlot


import plotly.plotly as py
from plotly.tools import FigureFactory as FF
from datetime import datetime

import pandas.io.data as web

mat.Data = web.DataReader("aapl", 'yahoo', datetime(2007, 10, 1), datetime(2009, 4, 1))
fig = FF.create_candlestick(mat.Data.open, mat.Data.high, mat.Data.low, mat.Data.close, dates=mat.Data.index)
py.iplot(fig, filename='finance/aapl-candlestick', validate=False)
