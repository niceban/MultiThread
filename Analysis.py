__author__ = 'NealLee'

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import dates
from datetime import datetime
import datetime as dt
# import plotly.plotly as py
# from datetime import daetime
# import plotly.tools as tls
# from plotly.tools import FigureFactory as FF



# Index([u'Date', u'Open', u'High', u'Close', u'Low', u'Volume', u'Price_change', u'P_change', u'Ma5', u'Ma10', u'Ma20', u'V_ma5', u'V_ma10', u'V_ma20', u'Turnover'], dtype='object')

def Captalize( s ):
    return s[0].upper() + s[1:]

class Analysis ():

    plt.interactive(False)

    def __init__(self):
        self.Data = pd.read_csv('/Users/Aha/Desktop/QuantInv/MultiThread/Datas/600033')
        self.Data.columns = map(Captalize , self.Data.columns)
        self.Data['Date'] = map(lambda s : datetime.strptime( s , "%Y-%m-%d" ) , self.Data.Date)
        self.Data['Weekday'] = map(lambda s : s.weekday() , self.Data.Date)
        # pass

    # def candlePlot(self):
    #     FF.create_candlestick(self.open, self.high, self.low, self.close, dates=self.Data)

    def plot(self ):
        Dates = map(lambda d : dates.date2num(d) , self.Data.Date)
        plt.scatter( Dates , self.Data.High , marker=0 , cmap='r' )
        plt.scatter( Dates , self.Data.Open , marker=0 , cmap='b' )
        plt.scatter( Dates , self.Data.Close , marker=0 , cmap='c' )
        plt.scatter( Dates , self.Data.Low , marker=0 , cmap='g' )
        print plt.show()
        return plt.show()


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


if __name__ == "__main__":

    mat = Analysis()
    mat.plot()
    exit()
    # plt.show()


