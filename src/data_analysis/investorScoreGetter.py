import pandas as pd
import numpy as np

#Usage: input an email address, this function will return a list
def getPoint(email):
    #load excel as a dataframe, load npy as a dict
    dataframe = pd.read_excel(r'RoboAdvisor 1.1 (Responses).xls')
    newDict = np.load('investorScore.npy',allow_pickle=True)
    #result is a list contains [email, RC, RW, investor Type]
    result = [0]*4 
    #assign email to result
    result[0] = email

    # i is a pandas.series corresponds to the input email, we add RC and RW to result according to the dict
    for i in dataframe.loc[dataframe['Email Address']== email]:
        value = newDict.item().get((dataframe.loc[dataframe['Email Address']== email][i]).values[0])
        if(value == None):
            continue
        if(type(value) == list):
            result[value[0]+1] += value[1]
        else:
            result[3] = value
    
    return result
            
# def main():
#     print(getPoint('lijihang21@gmail.com'))
    
# main()