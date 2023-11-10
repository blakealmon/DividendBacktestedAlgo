# DividendBacktestedAlgo
 dividend strat built by Blake Almon

Requirements 
-Requests
-Dotenv

API Requirements
-Polygon API 

Description:
-Backtests and adds profitability from beginning of 2023 to "2023-10-02" to the dividendAlgo.txt file. You can change the parameters and algorithm itself in the for loop.

#logic : 
(1) grabs every stock that is having dividends each day
(2) gets the close and open of each stock and subtracts them to see the profit if you had shorted that stock
(3) turns that number into a percent, then adds all the percents together to see how much total percent for the day was
(3) then adds the data + percent to the text file