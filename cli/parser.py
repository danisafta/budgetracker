from db.wrappers import *
import argparse
def is_number(var):
    try:
        value = float(var)
        return value
    except:
        raise argparse.ArgumentTypeError(str(var) + " is not a number")

parser = argparse.ArgumentParser()

parser.add_argument('-g', '--get', type=str, choices=['money_left', 'expense', 'stocks', 'cash', 'crypto'],
                    help="specifies that is a get request")
parser.add_argument('-i', '--insert', type=str, choices=['crypto', 'expense', 'stocks', 'cash'],
                    help="specifies that is a insert request")

parser.add_argument('-ed', '--expense_details', type=str, help="specifies the details for a recent expense")
parser.add_argument('-v', '--value', type=is_number, help="specifies the value that will be used")
parser.add_argument('-c', '--count', type=is_number,  help="specifies the count that will be used")
parser.add_argument('-t', '--ticker', type=str, help="specifies the ticker that will be used")

args = parser.parse_args()

def args_handle(args=args):
    if args.get == 'money_left':
        print("You have " + str(get_remaining_money()) + " left for this year")
    elif args.get == 'expense':
        for e in get_expense():
            print(e)
    elif args.get == 'stocks':
        for stock in get_stocks():
            print(stock)

    if args.insert == 'expense':
        value = args.value
        details = args.expense_details
        insert_expense(value=value, details=details)
    elif args.insert == 'stocks':
        value = args.value
        count = args.count
        ticker = args.ticker
        insert_stocks(count,total_value=value,ticker=ticker)