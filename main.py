import forecast
import send_sms
from datetime import datetime

# Since the api call is made at 6:00 AM, hourly_forecast[0] is 6 AM
def main():
    startTimes = [10, 8, 10, 8, 10]
    endTimes = [19, 15, 13, 19, 13]
    date = datetime.today()
    dayOfWeek = date.weekday()
    message = ""
    phone_number = "+19257877379"

    hourly_forecast = forecast.get_hourly_forecast("CA", "Goleta")

    for i in range(5):
        if (dayOfWeek == i):
            minTemp = int(hourly_forecast[startTimes[dayOfWeek] - 6]['temp']['english'])
            maxTemp = int(hourly_forecast[startTimes[dayOfWeek] - 6]['temp']['english'])
            minTempTime = startTimes[dayOfWeek]
            maxTempTime = endTimes[dayOfWeek]

            for j in range(startTimes[dayOfWeek] - 6,
                           endTimes[dayOfWeek] - 5):
                if ("Rain" in hourly_forecast[j]['condition']):
                    message += "Rain forecasted at " + str(j % 12) + ":00. "
                if (int(hourly_forecast[j]['temp']['english']) < minTemp):
                    minTemp = int(hourly_forecast[j]['temp']['english'])
                    minTempTime = j + 6
                if (int(hourly_forecast[j]['temp']['english']) > maxTemp):
                    maxTemp = int(hourly_forecast[j]['temp']['english'])
                    maxTempTime = j + 6

    message += "Min temp today is " + str(minTemp % 12) + " at " \
            + str(minTempTime) + ":00. "
    message += "Max temp today is " + str(maxTemp % 12) + " at " \
            + str(maxTempTime) + ":00. "
    #print(message)
    send_sms.send_message(phone_number, message)    
    # checked hours should depend on day of the week

if __name__ == '__main__':
    main()
