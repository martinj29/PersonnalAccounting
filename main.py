from Accounting import Account

ops = "/Users/martinjacquelard/Documents/programmation/pycharm/PersonnalAccounting/data/PersonalAccountingDatabase.csv"


def main():
    CCP = Account('CCP', init_money=150)
    CCP.load_from_csv(ops)
    CCP.sum
    a=1



if __name__ == '__main__':
    main()