from db.wrappers import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-g', '--get', type=str, choices=['money_left', 'expense', 'stock', 'cash', 'crypto'],
                    help="specifies that is a get request")
parser.add_argument('-i', '--insert', type=str, choices=['crypto', 'expense', 'stock', 'cash'],
                    help="specifies that is a insert request")
parser.add_argument('-ed', '--expense_details', type=str, help="specifies the details for a recent expense")
parser.add_argument('-v', '--value', type=int, help="specifies the value that will be used")
parser.add_argument('-c', '--count', type=int, help="specifies the count that will be used")

args = parser.parse_args()


def args_handle(args=args):
    if args.get == 'money_left':
        print("You have " + str(get_remaining_money()) + " left for this year")
    if args.get == 'expense':
        for e in get_expense():
            print(e)

    if args.insert == 'expense':
        value = args.value
        details = args.expense_details
        insert_expense(value=value, details=details)
