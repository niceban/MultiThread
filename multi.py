__author__ = 'Aha'
# import gc
# gc.disable()

from multiprocessing.dummy import Pool as ThreadPool
import tushare as ts
import os
import pandas as pd
import threading


infos = ts.get_stock_basics()

path = '/QuantInv/Datas'
files = os.listdir(path + '/Daily')


def output(i):
    ts.get_tick_data(i, date).to_csv(path + '/Tick/%s/%s' % (i, date))


def retry(sig, i):
    if sig < 3:
        try:
            output(i)
            pass
        except Exception, e:
            sig += 1
            retry(sig, i)
            print i, date, e

# retry(sig)


# for i in files[1:]:
def crawler(i):
    global date
    file_in = open(path + '/Daily/%s' % i)
    # print file_in
    sig = 1
    for line in file_in:
        if sig == 1:
            sig = sig + 1
            continue
        date = line.split(',')[0]
        if not os.path.exists(path + '/Tick/%s' % i):
            os.mkdir(path + '/Tick/%s' % i)
        retry(sig, i)


# crawler('000703')

# mutex = threading.Lock()
for i in files :
    print i
    t = threading.Thread(target = crawler , args = (i,) )
    t.start()

# pool = ThreadPool(8)
# pool.map(crawler, files)
