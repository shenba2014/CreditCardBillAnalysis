# -*- coding: utf-8 -*-

import pandas as pd


def load(filePath):
    billData = pd.read_table(
        filePath,
        delim_whitespace=True,
        usecols=[0, 1, 2, 3, 4, 5, 6],
        names=[
            'TradingDay', 'RecordedDay', 'CCNumber', 'Type', 'Currency',
            'Amount', 'Description'
        ],
        skiprows=3,
        parse_dates=[0, 1])
    return normalize(billData)


def normalize(data):
    data['TradingYear'] = [x.year for x in data.TradingDay]
    data['TradingYearMonth'] = [x.strftime('%Y-%m') for x in data.TradingDay]
    data['TradingMonthOnly'] = [x.month for x in data.TradingDay]
    data['TradingDayOnly'] = [x.day for x in data.TradingDay]
    data = data[data.Type.isin(['消费', '退货退税', '取现', '利息', '费用'])]
    return data


if __name__ == "__main__":
    print load('creditBill.txt')
