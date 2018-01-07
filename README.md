# CreditCardBillAnalysis
just a credit card bill analysis using python(pandas, numpy), now it only support credit card of CCB

usage:

0.First download your bill data from CCB
1.Analysis for each day and compare by month
For example:

pass billDataFile path and month range list
import creditBillAnalysisByDay
creditBillAnalysisByDay.plot('creditBill_2016-2018.txt',['2017-11','2017-12','2018-01'])

2.Analysis for each month and compare by year
For example:
pass billDataFile path and year range list

import creditBillAnalysisByMonth
creditBillAnalysisByMonth.plot('creditBill_2016-2018.txt', [2016,2017,2018])

