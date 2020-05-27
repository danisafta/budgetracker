import pymongo

db_client = pymongo.MongoClient()

db = db_client['cointracker']
col_crypto = db['crypto']
col_stocks = db['stocks']
col_cash = db['cash']
col_total = db['total']
col_expenses = db['expenses']
