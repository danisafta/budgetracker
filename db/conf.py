config = {}

config['USER'] = 'saftone1'
config['PASSWORD'] = 'suget1o!'

config['DB_LIST'] = ["mongodb://", config['USER'], ":", config['PASSWORD'], "'@ds263048.mlab.com:63048/cointracker"]
config['DB_URL'] = "".join(config['DB_LIST'])

ANNUALY_BUDGET = 30000
