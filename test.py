import pandas as pd

currency_df = pd.read_csv('Currency2Year.csv')
dict_of_currencies = dict(iter(currency_df.groupby('Currency')))


def convert_to_usd(original_price, factor):
	# converted_price = round(orginal_price * factor, 2)
	converted_price = original_price * factor
	return converted_price


def find_closest_date(txn):
	txn_currency = txn['Currency'].iloc[0]

	if txn_currency == 'USD':
		return txn

	currency_date_df = pd.DataFrame.from_dict(dict_of_currencies[txn_currency])
	currency_date_df['Date'] = pd.to_datetime(currency_date_df['Date'])
	txn_date_df = pd.to_datetime(txn_df['Transaction Date'])

	location = currency_date_df['Date'].searchsorted(txn_date_df, side='left')

	if currency_date_df['Date'][location[0] + currency_date_df['Date'].head(1).index.item()] > txn_date_df.iloc[0]:
		row = location[0] - 1 + currency_date_df['Date'].head(1).index.item()
	else:
		row = location[0] + currency_date_df['Date'].head(1).index.item()

	txn_df['Transaction amount'] = convert_to_usd(txn_df['Transaction amount'].iloc[0], currency_date_df['Factor'][row])
	txn_df['Currency'] = 'USD'

	return txn_df


headers = pd.read_csv('DummyTransactions.csv', index_col=0, nrows=0)
headers.to_csv("ModifiedDummy.csv", encoding='utf-8')

for txn_df in pd.read_csv('DummyTransactions.csv', chunksize=1):
	converted_df = find_closest_date(txn_df)
	converted_df.to_csv("ModifiedDummy.csv", mode='a', header=None, encoding='utf-8')
