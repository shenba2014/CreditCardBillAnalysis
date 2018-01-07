# -*- coding: utf-8 -*-

import loadBillData as lbd
import numpy as np
import pandas as pd


def plot(billFilePath, monthIndex=[]):
    billData = lbd.load(billFilePath)

    amountGroupedByTradingMonthAndDay = billData[[
        'TradingYearMonth', 'TradingDayOnly', 'Amount'
    ]].groupby(['TradingYearMonth', 'TradingDayOnly']).sum()

    dayIndex = range(1, 32)

    if (len(monthIndex) == 0):
        monthIndex = amountGroupedByTradingMonthAndDay.index.levels[0].values

    amountInDaysGroupedByMonth = [
        amountGroupedByTradingMonthAndDay.loc[x].reindex(
            dayIndex, fill_value=0.0).cumsum().values[:, 0] for x in monthIndex
    ]

    amountInDaysMergedByMonth = np.vstack(amountInDaysGroupedByMonth)

    df = pd.DataFrame(
        amountInDaysMergedByMonth.T, index=dayIndex, columns=monthIndex)

    df.plot()
