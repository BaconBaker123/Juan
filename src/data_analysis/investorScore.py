import numpy as np

#create a dict, key is the answer, and the value is point that correspond to the answer. if the value is a list[int, int], the first int repersent RC or RW(0 is RC, 1 is RW), and the second int is the answer
newDict = {'prepare for retirement.':[0,20],
'save for major upcoming expenses (education, health bills, etc.).':[0,10],
'save for something special (vacation, new car, etc.).':[0,20],
'build a rainy day fund for emergencies.':[0,0],
'generate income for expenses.':[0,0],
'build long term wealth.':[0,25],
'None':[1,0],
'Good':[1,7],
'Some':[1,11],
'Extensive':[1,15],
'I worry I could be left with nothing.':[1,0],
'I understand that it’s an inherent part of the investing process.':[1,3],
'I see opportunity for great returns.':[1,7],
'I think of the thrill of investing.':[1,10],
'sold everything.':[1,0],
'sold some.':[1,10],
'did nothing.':[1,5],
'reallocated my investments.':[1,20],
'bought more.':[1,40],
'sell everything.':[1,0],
'sell some.':[1,10],
'do nothing.':[1,5],
'reallocate my investments.':[1,15],
'buy more.':[1,20],
'I try to avoid making decisions.':[1,0],
'I reluctantly make decisions.':[1,6],
'I confidently make decisions and don’t look back.':[1,15],
'$5,000 to $25,000':[0,5],
'> $25,000':[0,10],
'−10% to 15%':[1,0],
'−15% to 25%':[1,5],
'−25% to 35%':[1,8],
'−30% to 45%':[1,10],
'−35% to 50%':[1,13],
'−40% to 55%':[1,17],
'−45% to 60%':[1,20],
'Monthly Contribution / Initial Investment < 10%':[0,5],
'Monthly Contribution / Initial Investment ≥ 10%':[0,10],
'1 to 4 years':[0,0],
'5 to 9 years':[0,5],
'10 to 19 years':[0,20],
'Over 19 years':[0,35],
'1 year':[0,0],
'2 to 5 years':[0,5],
'6 to 10 years':[0,30],
'More than 10 years from now':[0,55],
'Return strategy investor (i.e. prefer generating capital gains from stocks over fixed income from bonds)':'Return strategy investor',
'Income strategy investor (i.e. prefer generating fixed income like coupon or interest from bonds over capital gains from stocks)':'Income strategy investor'}

np.save("investorScore.npy",newDict)

#create and save 2 list that contains risk score for return strategy investor and income strategy investor
returnStrategiesRiskScore = [[1,2,3,3,4,5,5,6,7,8],
[1,2,3,4,4,5,5,6,7,8],
[1,2,3,4,4,5,6,6,8,9],
[1,2,3,4,4,5,6,7,8,9],
[1,2,3,4,5,6,6,7,8,9],
[1,2,4,4,5,6,7,7,9,10],
[1,2,4,5,5,6,7,8,10,11],
[1,2,4,5,5,6,8,9,10,11],
[1,3,4,5,6,7,8,10,11,12],
[1,3,5,5,6,7,9,10,12,12]]

np.save("returnStrategiesRiskScore.npy",returnStrategiesRiskScore)

incomeStrategiesRiskScore = [[1,1,2,2,2,3,3,3,3,3],
[1,1,2,2,2,3,3,3,3,3],
[1,1,2,2,2,3,3,3,3,3],
[1,1,2,2,2,3,3,3,3,3],
[1,1,2,2,3,3,3,3,3,3],
[1,1,3,3,3,3,3,3,3,3],
[1,2,3,3,3,3,3,3,3,3],
[1,2,3,3,3,3,3,3,3,3]]

np.save("incomeStrategiesRiskScore.npy",incomeStrategiesRiskScore)