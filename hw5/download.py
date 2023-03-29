#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 18:22:04 2022

@author: hanniel
"""

import urllib.request

files = '''2010/01052099999.csv
2010/99407099999.csv
2011/01008099999.csv
2011/01046099999.csv
2012/01023099999.csv
2012/01044099999.csv
2013/01001499999.csv
2013/01008099999.csv
2014/01008099999.csv
2014/01023099999.csv
2015/01008099999.csv
2015/01025099999.csv
2016/01008099999.csv
2016/01023199999.csv
2017/01008099999.csv
2017/01023099999.csv
2018/01008099999.csv
2018/01025099999.csv
2019/01008099999.csv
2019/01023099999.csv
2020/01008099999.csv
2020/01023099999.csv
2021/01062099999.csv
2021/01065099999.csv
2022/01241099999.csv
2022/02095099999.csv'''
files = files.split()
#%%
from os import mkdir
from os.path import isdir
if not isdir('data'):
    mkdir('data')
for f in files:
    folder, file = f.split('/')
    if not isdir(f'data/{folder}'):
        mkdir(f'data/{folder}')
    else:
        urllib.request.urlretrieve(f"https://www.ncei.noaa.gov/data/global-summary-of-the-day/access/{f}", 
                                f'data/{folder}/{file}')