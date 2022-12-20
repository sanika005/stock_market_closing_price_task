# from pandas import DataFrame
import pandas as pd
# import pandas_datareader as web
# from datetime import datetime
# filename='/Users/apple/Desktop/Sanika/Projects/DataAnalysis/List of Stocks case study.xlsx'
# df = pd.read_excel(filename)
# print(df)
# symbol = []
# symbol = list(df['SYMBOL    '])
# print(symbol)
# start = datetime(2022,9,1)
# end = datetime(2022,11,30)

# symbol_list_without_spaces = []
# for stripped_symbol in symbol:
#     single_symbol = stripped_symbol.strip()
#     symbol_list_without_spaces.append(single_symbol)
# print(symbol_list_without_spaces)

# for stock in symbol_list_without_spaces:
#     print(stock)
#     try:
#         df = web.get_data_yahoo('BAJAJFINSV',start,end)
#         print(df)
#         print(df.columns['Close'])
#     except Exception as e:
#         print(e)

import yfinance as yf

#define the ticker symbol
tickerSymbol = 'MSFT'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')
print(type(tickerDf))
closing_price_data = tickerDf['Close']
print(type(closing_price_data))
closing_price_data['Date'] = pd.to_datetime( closing_price_data['date'], errors='coerce',utc=True)
print(closing_price_data)