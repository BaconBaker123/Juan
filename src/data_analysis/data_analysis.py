import pandas as pd

#dataframe from excel
dataframe = pd.read_excel(r'/Users/jihangli/Devlopment/Juan/src/data_collection_API/RoboAdvisor 1.1 (Responses).xls')

def main():
    global score_dict
    score_dict = {}
    score_cal(dataframe)
    select(score_dict)

#calculate score
def score_cal(dataframe):
    ###########score_dict = {RC , RW}#####################
    for i in range(dataframe.shape[0]):
        email_address = dataframe.loc[i]['Email Address']
        score_dict[email_address] = [0,0]
        #Qestion 1(Risk Capacity)
        if dataframe.loc[i]['What is your goal for investing?'] == 'prepare for retirement.':
            score_dict[email_address][0] += 20
        elif dataframe.loc[i]['What is your goal for investing?'] == 'save for major upcoming expenses (education, health bills, etc.).': 
            score_dict[email_address][0] += 10
        elif dataframe.loc[i]['What is your goal for investing?'] == 'save for something special (vacation, new car, etc.).':
            score_dict[email_address][0] += 20
        elif dataframe.loc[i]['What is your goal for investing?'] == 'build a rainy day fund for emergencies.':
            score_dict[email_address][0] += 0
        elif dataframe.loc[i]['What is your goal for investing?'] == 'generate income for expenses.':
            score_dict[email_address][0] += 0
        elif dataframe.loc[i]['What is your goal for investing?'] == 'build long term wealth.':
            score_dict[email_address][0] += 25
        #Qestion 2(Risk Willingness)
        if dataframe.loc[i]['What is your understanding of stocks, bonds, and ETFs?'] == 'None':
            score_dict[email_address][1] += 0
        elif dataframe.loc[i]['What is your understanding of stocks, bonds, and ETFs?'] == 'Good':
            score_dict[email_address][1] += 7
        elif dataframe.loc[i]['What is your understanding of stocks, bonds, and ETFs?'] == 'Some':
            score_dict[email_address][1] += 11
        elif dataframe.loc[i]['What is your understanding of stocks, bonds, and ETFs?'] == 'Extensive':
            score_dict[email_address][1] += 15
        #Qestion 3(Risk Willingness)
        if dataframe.loc[i]['When you hear “risk” related to your finances, what is the first thought that comes to mind?'] == 'I worry I could be left with nothing.':
            score_dict[email_address][1] += 0
        elif dataframe.loc[i]['When you hear “risk” related to your finances, what is the first thought that comes to mind?'] == 'I understand that it’s an inherent part of the investing process.':
            score_dict[email_address][1] += 3
        elif dataframe.loc[i]['When you hear “risk” related to your finances, what is the first thought that comes to mind?'] == 'I see opportunity for great returns.':
            score_dict[email_address][1] += 7
        elif dataframe.loc[i]['When you hear “risk” related to your finances, what is the first thought that comes to mind?'] == 'I think of the thrill of investing.':
            score_dict[email_address][1] += 10
        #Qestion 4(Risk Willingness/But Not Scored)
        #Qestion 5a(Risk Willingness)
        if dataframe.loc[i]['What did you do when you experienced a 20% decline in the value of your investments?'] == 'sold everything.':
            score_dict[email_address][1] += 0
        elif dataframe.loc[i]['What did you do when you experienced a 20% decline in the value of your investments?'] == 'sold some.':
            score_dict[email_address][1] += 10
        elif dataframe.loc[i]['What did you do when you experienced a 20% decline in the value of your investments?'] == 'did nothing.':
            score_dict[email_address][1] += 5
        elif dataframe.loc[i]['What did you do when you experienced a 20% decline in the value of your investments?'] == 'reallocated my investments.':
            score_dict[email_address][1] += 20
        elif dataframe.loc[i]['What did you do when you experienced a 20% decline in the value of your investments?'] == 'bought more.':
            score_dict[email_address][1] += 40
        #Qestion 5b(Risk Willingness)
        if dataframe.loc[i]['If you were ever to experience a 20% decline or more in the value of your investments in one year, what would you do?'] == 'sell everything.':
            score_dict[email_address][1] += 0
        elif dataframe.loc[i]['If you were ever to experience a 20% decline or more in the value of your investments in one year, what would you do?'] == 'sell some.':
            score_dict[email_address][1] += 10
        elif dataframe.loc[i]['If you were ever to experience a 20% decline or more in the value of your investments in one year, what would you do?'] == 'do nothing.':
            score_dict[email_address][1] += 5
        elif dataframe.loc[i]['If you were ever to experience a 20% decline or more in the value of your investments in one year, what would you do?'] == 'reallocate my investments.':
            score_dict[email_address][1] += 15
        elif dataframe.loc[i]['If you were ever to experience a 20% decline or more in the value of your investments in one year, what would you do?'] == 'buy more.':
            score_dict[email_address][1] += 20
        #Qestion 6(Risk Willingness)
        if dataframe.loc[i]['How would you describe your approach to making important financial decisions? ']:
            score_dict[email_address][1] += 0
        elif dataframe.loc[i]['How would you describe your approach to making important financial decisions? '] == 'I reluctantly make decisions.':
            score_dict[email_address][1] += 6
        elif dataframe.loc[i]['How would you describe your approach to making important financial decisions? '] == 'I confidently make decisions and don’t look back.':
            score_dict[email_address][1] += 15
        #Qestion 7(Risk Capacity)
        if dataframe.loc[i]['How much do you want to invest to get started?'] == '$5,000 to $25,000':
            score_dict[email_address][0] += 5
        elif dataframe.loc[i]['How much do you want to invest to get started?'] == '> $25,000':
            score_dict[email_address][0] += 10
        #Question 8(Risk Willingness)
        if dataframe.loc[i]['How much investment value fluctuation would you be comfortable with 1 year from now?'] == '−10% to 15%':
            score_dict[email_address][1] += 0
        elif dataframe.loc[i]['How much investment value fluctuation would you be comfortable with 1 year from now?'] == '−15% to 25%':
            score_dict[email_address][1] += 5
        elif dataframe.loc[i]['How much investment value fluctuation would you be comfortable with 1 year from now?'] == '−25% to 35%':
            score_dict[email_address][1] += 8
        elif dataframe.loc[i]['How much investment value fluctuation would you be comfortable with 1 year from now?'] == '−30% to 45%':
            score_dict[email_address][1] += 10
        elif dataframe.loc[i]['How much investment value fluctuation would you be comfortable with 1 year from now?'] == '−35% to 50%':
            score_dict[email_address][1] += 13
        elif dataframe.loc[i]['How much investment value fluctuation would you be comfortable with 1 year from now?'] == '−40% to 55%':
            score_dict[email_address][1] += 17
        elif dataframe.loc[i]['How much investment value fluctuation would you be comfortable with 1 year from now?'] == '−45% to 60%':
            score_dict[email_address][1] += 20
        #Qestion 9(Risk Capacity)
        if dataframe.loc[i]['How much do you want to contribute each month?'] == 'Monthly Contribution / Initial Investment < 10%':
            score_dict[email_address][0] += 5
        elif dataframe.loc[i]['How much do you want to contribute each month?'] == 'Monthly Contribution / Initial Investment ≥ 10%':
            score_dict[email_address][0] += 10
        #Qestion 10a(Risk Capacity)
        if dataframe.loc[i]['How long do you need the income to last?'] == '1 to 4 years':
            score_dict[email_address][0] += 0
        elif dataframe.loc[i]['How long do you need the income to last?'] == '5 to 9 years':
            score_dict[email_address][0] += 5
        elif dataframe.loc[i]['How long do you need the income to last?'] == '10 to 19 years':
            score_dict[email_address][0] += 20
        elif dataframe.loc[i]['How long do you need the income to last?'] == 'Over 19 years':
            score_dict[email_address][0] += 35
        #Qestion 10b(Risk Capacity)
        if dataframe.loc[i]['When will you need to start withdrawing funds from this account?'] == '1 year':
            score_dict[email_address][0] += 0
        elif dataframe.loc[i]['When will you need to start withdrawing funds from this account?'] == '2 to 5 years':
            score_dict[email_address][0] += 5
        elif dataframe.loc[i]['When will you need to start withdrawing funds from this account?'] == '6 to 10 years':
            score_dict[email_address][0] += 30
        elif dataframe.loc[i]['When will you need to start withdrawing funds from this account?'] == 'More than 10 years from now':
            score_dict[email_address][0] += 55
        #Qestion 11(Return strategy investor/Income strategy investor)
        if dataframe.loc[i]['How would you consider yourself?'] == 'Return strategy investor (i.e. prefer generating capital gains from stocks over fixed income from bonds)':
            score_dict[email_address].append('Return strategy investor')
        elif dataframe.loc[i]['How would you consider yourself?'] == 'Income strategy investor (i.e. prefer generating fixed income like coupon or interest from bonds over capital gains from stocks)':
            score_dict[email_address].append('Income strategy investor')
    return score_dict 

#input user email to search for score (score in a format [RC, RW, investor type])
def select(score_dict):
    while True:    
        try:
            global email
            email = input('Email:')
            print(f'score in format [RC, RW, type of investor], user score -----> {score_dict[email]}')
            print(f'You are a {score_dict[email][2]}, your risk score is {classify()}.')
            break
        except KeyError:
            print('You can\'t get your eamil correct? Try again -_-!')

#working on it 
def classify():
    #Return strategy investor
    #First compare RC, then compare RW 
    if score_dict[email][2] == 'Return strategy investor':
        if score_dict[email][0] <= 10:
            return 1
        elif score_dict[email][0] <= 20 and score_dict[email][0] >= 11:
            if score_dict[email][1] <= 80:
                return 2   
    else:
        return '6'

    

main()
