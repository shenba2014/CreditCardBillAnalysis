# -*- coding: utf-8 -*-

import loadBillData as lbd
import numpy as np
import pandas as pd


def plot(billFilePath, yearIndex=[]):
    billData = lbd.load(billFilePath)

    amountGroupedByTradingYearAndMonth = billData[[
        'TradingYear', 'TradingMonthOnly', 'Amount'
    ]].groupby(['TradingYear', 'TradingMonthOnly']).sum()

    monthIndex = range(1, 13)

    if (len(yearIndex) == 0):
        yearIndex = amountGroupedByTradingYearAndMonth.index.levels[0].values

    amountInDaysGroupedByMonth = [
        amountGroupedByTradingYearAndMonth.loc[x].reindex(
            monthIndex, fill_value=0.0).values[:, 0] for x in yearIndex
    ]

    amountInMonthsMergedByYear = np.vstack(amountInDaysGroupedByMonth)

    df = pd.DataFrame(
        amountInMonthsMergedByYear.T, index=monthIndex, columns=yearIndex)

    df.plot()
