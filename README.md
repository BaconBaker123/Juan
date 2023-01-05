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

<p align="center">HelloWorld</p>

|**Score**|**Level**|
|---------|---------|
|**33-47**|High tolerance for risk|    
|**29-32**|Above-average tolerance for risk|
|**23-28**|Average/moderate tolerance for risk|
|**19-22**|Below-average tolerance for risk|
|**0-18**|Low tolerance for risk|

Prompt the following questions to determine the _risk index_, note that answers to the questions have varying effects on changing the _risk index_:

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






