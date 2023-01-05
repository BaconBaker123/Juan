# Robo Advisor
The program assesses users’ 1) risk preferences and 2) investment strategies to provide corresponding equity recommendations based on rationality. 
## 1) Analyze Client Risk Preference
---
![Risk Preference Indifference Curves](https://github.com/BaconBaker123/Juan/blob/main/image/l4J7O.png)

_What the image means_:
* **Risk aversion**: prefer safer strategies/assets.
* **Risk neutral**: no specific preference.
* **Risk lover**: prefer investing in higher-risk assets that could result in higher return. 

_Steps_:
1.Prompt the questions to clients.
2.Use the Grable and Lytton risk-tolerance scale (the questionnaire is provided below) to evaluate each client

_Goals_:
Set a variable for _risk index_. Calculate the _risk index_ the user, which will impact our methods of equity analysis. The risk index is scaled as follows: 
|**Score**|**Level**|
|---------|---------|
|**33-47**|High tolerance for risk|    
|**29-32**|Above-average tolerance for risk|
|**23-28**|Average/moderate tolerance for risk|
|**19-22**|Below-average tolerance for risk|
|**0-18**|Low tolerance for risk|

Prompt the following questions to determine the _risk index_, note that answers to the questions have varying effects on changing the _risk index_:

1. In general, how would your best friend describe you as a risk taker?
    
    a). A real gambler

    b). Willing to take risks after completing adequate research

    c). Cautious

    d). A real risk avoider

2. You are on a TV game show and can choose one of the following, which would you take?

    a). $1,000 in cash

    b). A 50% chance at winning $5,000

    c). A 25% chance at winning $10,000

    d). A 5% chance at winning $100,000

3. You have just finished saving for a “once-in-a-lifetime” vacation. Three weeks before you plan to leave, you lose your job. You would:

    a). Cancel the vacation

    b). Take a much more modest vacation

    c). Go as scheduled, reasoning that you need the time to prepare for a job search

    d). Extend your vacation, because this might be your last chance to go first-class

4. If you unexpectedly received $20,000 to invest, what would you do?
    a). Deposit it in a bank account, money market account, or an insured CD

    b). Invest it in safe high quality bonds or bond mutual funds

    c). Invest it in stocks or stock mutual funds

5. In terms of experience, how comfortable are you investing in stocks or stock mutual
funds?

    a). Not at all comfortable

    b). Somewhat comfortable

    c). Very comfortable

6. When you think of the word “risk,” which of the following words comes to mind first?

    a). Loss

    b). Uncertainty

    c). Opportunity

    d). Thrill

7. Some experts are predicting prices of assets such as gold, jewels, collectibles, and real estate (hard assets) to increase in value; bond prices may fall, however, experts tend to agree that government bonds are relatively safe. Most of your investment assets are now in high interest government bonds. What would you do?

    a). Hold the bonds

    b). Sell the bonds, put half the proceeds into money market accounts, and the other half into hard assets

    c). Sell the bonds and put the total proceeds into hard assets

    d). Sell the bonds, put all the money into hard assets, and borrow additional money to buy more

8. Given the best and worst case returns of the four investment choices below, which
would you prefer?

    a). $200 gain best case; $0 gain/loss worst case

    b). $800 gain best case; $200 loss worst case

    c). $2,600 gain best case; $800 loss worst case

    d). $4,800 gain best case; $2,400 loss worst case

9. In addition to whatever you own, you have been given $1,000. You are now asked to choose between:

    a). A sure gain of $500
    
    b). A 50% chance to gain $1,000 and a 50% chance to gain nothing

10. In addition to whatever you own, you have been given $2,000. You are now asked to choose between:

    a). A sure loss of $500

    b). A 50% chance to lose $1,000 and a 50% chance to lose nothing

11. Suppose a relative left you an inheritance of $100,000, stipulating in the will that you invest ALL the money in ONE of the following choices. Which one would you select?

    a). A savings account or money market mutual fund

    b). A mutual fund that owns stocks and bonds

    c). A portfolio of 15 common stocks

    d). Commodities like gold, silver, and oil

12. If you had to invest $20,000, which of the following investment choices would you find most appealing?

    a). 60% in low-risk investments, 30% in medium-risk investments, 10% in high-risk investments

    b). 30% in low-risk investments, 40% in medium-risk investments, 30% in high-risk investments

    c). 10% in low-risk investments, 40% in medium-risk investments, 50% in high-risk investments

13. Your trusted friend and neighbor, an experienced geologist, is putting together a group of investors to fund an exploratory gold mining venture. The venture could pay back 50 to 100 times the investment if successful. If the mine is a bust, the entire investment is worthless. Your friend estimates the chance of success is only 20%. If you had the money, how much would you invest?

    a). Nothing

    b). One month’s salary

    c). Three month’s salary

    d). Six month’s salary

Now that you have finished collecting the answers of the questions from the user, you may start **adding** the answers' corresponding numerical value and match it with the scale provided above. The scoring method is provided as:

1. a = 4; b = 3; c = 2; d = 1
2. a = 1; b = 2; c = 3; d = 4
3. a = 1; b = 2; c = 3; d = 4
4. a = 1; b = 2; c = 3
5. a = 1; b = 2; c = 3
6. a = l ; b = 2 ;c = 3 ;d = 4
7. a = 1; b = 2; c = 3; d = 4
8. a = 1; b = 2; c = 3; d = 4
9. a = 1; b = 3
10. a = 1; b = 3
11. a = 1; b = 2; c = 3; d = 4
12. a = 1; b = 2; c = 3
13. a = 1; b = 2; c = 3; d = 4

After you are done with this step, you should receive the numerical risk index of the user. Now, we will match the number with their corresponding range to determine their **risk level** (e.g. high tolerance). Refer to the table above. 

After your are done with this step, you should be left with a variable that shows you which of the 5 risk levels the user is at. 






