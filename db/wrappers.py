from datetime import datetime
from db.connector import col_crypto, col_cash, col_stocks, col_expenses
from db.conf import ANNUALY_BUDGET


def insert_btc(number: int, total_value: int):
    '''
    insert bitcoin in the wallet
    :param number: number of btc to be inserted
    :param total_value: total value spend of this amount of btc
    :return: void
    '''
    col_crypto.insert_one({
        'total_value': total_value,
        'number': number,
        'ppu_value': total_value / number
    })
    print("SUCCESFULLY ADDED BTC INTO YOUR WALLET")


def insert_cash(number: int, total_value: int, currency: str):
    '''
    insert cash in different types of currency in the wallet
    :param number: number of money to be inserted
    :param total_value: total spend on that currency
    :param currency: e.g USD, EUR
    :return: void
    '''
    col_cash.insert_one({
        'number': number,
        'currency': currency,
        'ppu': total_value / number
    })
    print("SUCCESFULLY ADDED CASH INTO YOUR WALLET")


def insert_stocks(number: int, total_value: int, ticker: str):
    '''
    insert stocks to portfolio
    :param number: number of stocks to be added
    :param total_value: total value spent on that stocks
    :param ticker: e.g TSLA, AMZN
    :return:
    '''

    col_stocks.insert_one({
        'total_value': total_value,
        'number': number,
        'ticker': ticker,
        'ppu': total_value / number
    })
    print("SUCCESFULLY ADDED STOCKS INTO YOUR WALLET")


def insert_expense(value: int, day=datetime.now().day, month=datetime.now().month, year=datetime.now().year,
                   details=""):
    '''
    subtract expenses to the budget and keeps the record
    :param value:
    :param day:
    :param month:
    :param year:
    :param details:
    :return:
    '''

    col_expenses.insert_one({
        "value": value,
        "details": details,
        "day": day,
        "month": month,
        "year": year
    })


def get_expense(month=None):
    if month:
        return col_expenses.find({"month": month})
    return col_expenses.find()


def get_btc():
    '''
    :return: btc entries in collection
    '''

    return col_crypto.find()


def get_cash():
    '''

    :return: cash in account
    '''
    return col_cash.find()


def get_stocks():
    '''

    :return:
    '''
    return col_stocks.find()


def get_remaining_money(month=None):
    money_spent = 0
    for expense in get_expense(month):

        money_spent += expense['value']
    return ANNUALY_BUDGET - money_spent
