#Source: https://stackoverflow.com/questions/63338052/attributeerror-nonetype-object-has-no-attribute-find-in-bs4
import datetime as dt
import requests
import bs4
import lxml
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import math
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators

url=r'https://www.marketwatch.com/tools/stockresearch/screener/results.asp?submit=Screen&Symbol=true&Symbol=false&ChangePct=true&ChangePct=false&FiftyTwoWeekLow=false&CompanyName=true&CompanyName=false&Volume=true&Volume=false&PERatio=false&Price=true&Price=false&LastTradeTime=false&MarketCap=false&Change=true&Change=false&FiftyTwoWeekHigh=false&MoreInfo=true&MoreInfo=false&SortyBy=Symbol&SortDirection=Descending&ResultsPerPage=OneHundred&TradesShareEnable=false&TradesShareMin=&TradesShareMax=&PriceDirEnable=true&PriceDir=Up&PriceDirPct=100&LastYearEnable=false&LastYearAboveHigh=&TradeVolEnable=false&TradeVolMin=&TradeVolMax=&BlockEnable=false&BlockAmt=&BlockTime=&PERatioEnable=false&PERatioMin=&PERatioMax=&MktCapEnable=false&MktCapMin=&MktCapMax=&MovAvgEnable=false&MovAvgType=Outperform&MovAvgTime=FiftyDay&MktIdxEnable=false&MktIdxType=Outperform&MktIdxPct=&MktIdxExchange=&Exchange=All&IndustryEnable=false&Industry='

res=requests.get(url)
soup=bs4.BeautifulSoup(res.text, 'lxml')
tick=soup.find('td', {'class' :'aleft'}).find('a').text
print(tick)