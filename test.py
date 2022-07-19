import pandas as pd
import numpy as np


def convert_to_usd(orginal_price, factor):
	converted_price = 0
	return converted_price


currency_df = pd.read_csv('Currency2Year.csv')
dict_of_currencies = dict(iter(currency_df.groupby('Currency')))
# print(dict_of_currencies.keys())
# print(dict_of_currencies['AUD']['Date'])
currency_date_df = pd.to_datetime(dict_of_currencies['AUD']['Date'])
# print(currency_date_df)

# for txn_df in pd.read_csv('DummyTransactions.csv', chunksize=1):
txn_df = pd.read_csv('DummyTransactions.csv', nrows=1)
txn_date_df = pd.to_datetime(txn_df['Transaction Date'])
# print(txn_date_df[0])

# dat = currency_date_df.truncate(before=txn_date_df[0])
# print(dat)
for i, v in enumerate(currency_date_df, start=currency_date_df.index[0]):
	if v < txn_date_df[0]:
		continue
	else:
		print(txn_date_df[0])
		print(currency_date_df[i])
		print(currency_date_df[i - 1])
		break

# df = currency_date_df.truncate(before=txn_date_df['Transaction Date'])
# df = pd.merge_asof(currency_date_df, txn_date_df, left_on='Date', right_on='Transaction Date')
# print(df)




