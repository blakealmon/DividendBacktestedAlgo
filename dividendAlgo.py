import requests
from dotenv import load_dotenv
import os
ß
load_dotenv()
#Dot env
SECRET_KEY = os.environ.get("POLYGON_API_KEY");

#secret key for polygon API stocks
polygonAPIKEY = SECRET_KEY



#all dates backtested since the beginning of 2023
dateFormatted = ['2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06', '2023-01-09', '2023-01-10', '2023-01-11', '2023-01-12', '2023-01-13', '2023-01-17', '2023-01-18', '2023-01-19', '2023-01-20', '2023-01-23', '2023-01-24', '2023-01-25', '2023-01-26', '2023-01-27', '2023-01-30', '2023-01-31', '2023-02-01', '2023-02-02', '2023-02-03', '2023-02-06', '2023-02-07', '2023-02-08', '2023-02-09', '2023-02-10', '2023-02-13', '2023-02-14', '2023-02-15', '2023-02-16', '2023-02-17', '2023-02-21', '2023-02-22', '2023-02-23', '2023-02-24', '2023-02-27', '2023-02-28', '2023-03-01', '2023-03-02', '2023-03-03', '2023-03-06', '2023-03-08', '2023-03-09', '2023-03-10', '2023-03-13', '2023-03-14', '2023-03-15', '2023-03-16', '2023-03-17', '2023-03-20', '2023-03-21', '2023-03-22', '2023-03-23', '2023-03-24', '2023-03-27', '2023-03-28', '2023-03-30', '2023-03-31', '2023-04-03', '2023-04-04', '2023-04-05', '2023-04-06', '2023-04-07', '2023-04-10', '2023-04-11', '2023-04-12', '2023-04-13', '2023-04-14', '2023-04-17', '2023-04-18', '2023-04-19', '2023-04-20', '2023-04-21', '2023-04-24', '2023-04-25', '2023-04-26', '2023-04-27', '2023-04-28', '2023-05-01', '2023-05-02', '2023-05-03', '2023-05-04', '2023-05-05', '2023-05-08', '2023-05-09', '2023-05-10', '2023-05-11', '2023-05-12', '2023-05-15', '2023-05-16', '2023-05-17', '2023-05-18', '2023-05-19', '2023-05-22', '2023-05-23', '2023-05-24', '2023-05-25', '2023-05-26', '2023-05-29', '2023-05-30', '2023-05-31', '2023-06-01', '2023-06-02', '2023-06-05', '2023-06-06', '2023-06-07', '2023-06-08', '2023-06-09', '2023-06-12', '2023-06-13', '2023-06-14', '2023-06-15', '2023-06-16', '2023-06-20', '2023-06-21', '2023-06-22', '2023-06-23', '2023-06-26', '2023-06-27', '2023-06-28', '2023-06-29', '2023-06-30', '2023-07-03', '2023-07-05', '2023-07-06', '2023-07-07', '2023-07-10', '2023-07-11', '2023-07-12', '2023-07-13', '2023-07-14', '2023-07-17', '2023-07-18', '2023-07-19', '2023-07-20', '2023-07-21', '2023-07-24', '2023-07-25', '2023-07-26', '2023-07-27', '2023-07-28', '2023-07-31', '2023-08-01', '2023-08-02', '2023-08-03', '2023-08-04', '2023-08-07', '2023-08-08', '2023-08-09', '2023-08-10', '2023-08-11', '2023-08-14', '2023-08-15', '2023-08-16', '2023-08-17', '2023-08-18', '2023-08-21', '2023-08-22', '2023-08-23', '2023-08-24', '2023-08-25', '2023-08-28', '2023-08-29', '2023-08-30', '2023-08-31', '2023-09-01', '2023-09-05', '2023-09-06', '2023-09-07', '2023-09-08', '2023-09-11', '2023-09-12', '2023-09-13', '2023-09-14', '2023-09-15', '2023-09-18', '2023-09-19', '2023-09-20', '2023-09-21', '2023-09-22', '2023-09-25', '2023-09-26', '2023-09-27', '2023-09-28', '2023-09-29', '2023-10-02']

dateX = 0

#full for loop
#logic : 
# (1) grabs every stock that is having dividends each day
# (2) gets the close and open of each stock and subtracts them to see the profit if you had shorted that stock
# (3) turns that number into a percent, then adds all the percents together to see how much total percent for the day was
# (3) then adds the data + percent to the text file

#len(dateFormatted)
for x in range(len(dateFormatted)):


    polygonDividends = 'https://api.polygon.io/v3/reference/dividends?ex_dividend_date=' + dateFormatted[dateX] + '&limit=1000&apiKey=' + polygonAPIKEY

    response = requests.get(polygonDividends)

    jsonObj = response.json()

    stockOpenCloseList = []
    stockOpenCloseList.clear()


    #len(jsonObj["results"])
    for x in range(len(jsonObj["results"])):
    #    print(jsonObj["results"][x]['ticker'])

       polgonDailyOpenClose = 'https://api.polygon.io/v1/open-close/' + jsonObj["results"][x]['ticker'] + '/' + dateFormatted[dateX] + '?adjusted=true&apiKey=' + polygonAPIKEY

       print(polgonDailyOpenClose)
       responseDaily = requests.get(polgonDailyOpenClose)

       jsonObjDaily = responseDaily.json()
       print(jsonObjDaily)

       if(jsonObjDaily['status'] == 'OK'):

           if('volume' in jsonObjDaily):

                if(jsonObjDaily['volume'] > 250000):

                 gainValue = jsonObjDaily['open'] - jsonObjDaily['close']
    
                 gainPercent = (gainValue/jsonObjDaily['open']) * 100

                 stockOpenCloseList.append(gainPercent)

                else:
                    print("to little volume")

           else:
                print('No volume')
                
       else:
        print("error")
    
    

    
    
    #print(stockOpenCloseList)
    try:
        totalPercent = sum(stockOpenCloseList)/int(len(stockOpenCloseList))
        print(str(totalPercent))

        stringTotalPercent = str(totalPercent)

        f = open("DividendBacktestedAlgo/dividendAlgo.txt", "a")
        f.write(stringTotalPercent + "%\n")
        f.close()

    except ZeroDivisionError as e:
       print("Not enough stocks that day")
    
   
    dateX += 1
    print(dateX)





