from db.connector import col_stocks
import pandas as pd
import numpy as np
from pandas_datareader import data as wb


def get_tickers_from_db(month = None) -> list:
    '''
    get all the tickers from db, no duplicates
    '''
    tickers = []
    if month:
        for stock in col_stocks.find({'month': month}):
            tickers.append(stock['ticker'])
        return list(set(tickers))

    for stock in col_stocks.find():
        tickers.append(stock['ticker'])
    return list(set(tickers))

def get_total_invested(ticker = None) -> float:
    '''
    returns the value for the entire portfolio if ticker not specified
    returns the value invested in a company if ticker specified
    '''
    total = 0.0
    if ticker:
        for stock in col_stocks.find({'ticker': ticker}):
           total += float(stock['total_value'])
        return total

    for stock in col_stocks.find():
        total += float(stock['total_value'])
    return total


def get_financial_data(tickers: list, start_date = '2000-01-01', end = None):
    stock_data = pd.DataFrame()
    for t in tickers:
        stock_data[t] = wb.DataReader(t, data_source='yahoo', start=start_date, end='2020-01-01')['Adj Close']
    return stock_data

def get_simple_returns(data):
    '''
    return the simple returns for the portfolio
    @data is dataframe

    '''
    return (data / data.shift(1)) -1


def get_log_returns(data):
    '''
    return the log returns for the portfolio
    @data is dataframe

    '''
    security_returns = np.log(data / data.shift(1))
    return security_returns, security_returns.cov() * 250, security_returns.corr()

def get_var_vol(weights, security_returns):
    '''
    return variance and volatility for the portfolio
    security returns must be log returns not simple
    '''
    weights = np.array(list(weights.values()))
    portfolio_variance = np.dot(weights.T, np.dot(security_returns.cov() * 250, weights))
    portfolio_volatility = portfolio_variance ** 0.5
    return portfolio_variance, portfolio_volatility

def get_weights_dict(tickers_tuple: list, total_invested: float) -> dict:
    '''
    returns a weights dict for the entire portfolio
    tickers must be a list of tuples e.g (AAPL, 23.4)
    '''
    weights = {}
    for ticker, value_invested in tickers_tuple:
        weights[ticker] = value_invested / total_invested
    return weights

def get_investment_tuples(tickers: list) -> list:
    '''
    returns all the companies where was invested as a list of tuples
    '''
    result = []
    for ticker in tickers:
        result.append((ticker, get_total_invested(ticker= ticker)))
    return result


def get_annual_returns(returns):
    '''
    returns the annual return for returns
    @returns is dataframe
    '''
    return returns.mean() * 250


def get_portfolio_return(weights: dict, annual_returns ) ->float:
    '''
    returns portfolio return

    '''
    weights = np.array(list(weights.values()))
    p_return =  np.dot(annual_returns, weights)

    return  p_return



def get_portfolio_summary():
    '''
    Displays a summary of the portfolio
    '''
    tickers = get_tickers_from_db()
    total = get_total_invested()
    tt = get_investment_tuples(tickers)

    data = get_financial_data(tickers=tickers)
    returns = get_simple_returns(data)
    annual_ret = get_annual_returns(returns)
    weigths = get_weights_dict(tickers_tuple=tt, total_invested=get_total_invested())
    pret = get_portfolio_return(weights=weigths, annual_returns=annual_ret)

    logret, cov, cor = get_log_returns(data)
    variance, volatily = get_var_vol(weigths, logret)

    print("You have invested {} USD in this portfolio".format(total))
    print("Your portfolio has " + str(round(pret * 100, 2)) + " % return")
    print("Your portfolio has "+ str(round(volatily * 100, 2)) +" % volatility and "+  str(round(variance * 100, 2))+" % variance ".format(volatily,variance))


if __name__ == "__main__":
    get_portfolio_summary()