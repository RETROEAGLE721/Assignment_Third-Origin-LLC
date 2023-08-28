from datetime import datetime,date,timedelta
import numpy as np 
import pandas as pd 
from pytz import timezone
import time

class DateUtility:
    def convert_dt(self,from_date:datetime, from_date_TZ:str , to_date_TZ:str) -> datetime:
        print("Enter date time in",from_date_TZ,"is",from_date)
        return from_date.astimezone(timezone(to_date_TZ))


    def add_dt(self,from_date:datetime, number_of_days:int) -> datetime:
        return from_date + timedelta(days=number_of_days)


    def sub_dt(self,from_date:datetime, number_of_days:datetime) -> datetime :
        return from_date - timedelta(days=10)


    def get_days(self,from_date:datetime, to_date:datetime) -> int:
        if from_date < to_date:
            return (to_date - from_date).days
        else:
            return (from_date - to_date).days


    def get_days_exclude_we(self,from_date:datetime, to_date:datetime) -> int :
        return np.busday_count(from_date,to_date,weekmask=[1,1,1,1,1,0,0])


    def get_days_since_epoch(self,from_date:datetime) -> int:
        return (from_date-datetime(1970,1,1).date()).days


    def get_business_days(self,from_date:datetime, to_date:datetime) -> int:
        holidays_dates = []
        read_data = pd.read_csv('holidays.dat')
        for x in range(0,read_data.shape[0]):
            holidays_ = str(read_data.at[0,'DATE'])
            holidays_dates.append(holidays_[:4]+"-"+holidays_[4:6]+"-"+holidays_[6:])
        return np.busday_count(from_date,to_date,weekmask=[1,1,1,1,1,0,0],holidays=holidays_dates)


init_test = DateUtility()
while True:

    print("1. Date time coversions between timezones \n2. Add numbers of days to given date \n3. Subtract numbers of days form given date \n4. Get number of days between two given dates \n5. Get number of days excluding weekends \n6. Get number of days since EPOCH from given date \n7. Get number of business days between two days excluding holidays\n8. Exit")
    a = input("Enter number:- ")

    try :
        if a == "8":
            break

        elif a != "1":
            start_date = datetime.strptime(input("Enter starting date :-"),'%Y-%m-%d').date()


        if a == "1":
            date_to_convert = datetime.strptime(input("Enter date :-"),'%Y-%m-%d')
            from_timezone = input("Enter from timezone :-")
            to_timezone = input("Enter to timezone :-")
            print("Output Time in",to_timezone,"is",init_test.convert_dt(date_to_convert,from_timezone,to_timezone))


        elif a == "2":
            numbers_of_days = int(input("Enter number of days to add :- "))
            print("After adding",numbers_of_days," days to",start_date,"we get",init_test.add_dt(start_date,numbers_of_days))


        elif a == "3":
            numbers_of_days = int(input("Enter number of days to subtract :- "))
            print("After subtracting",numbers_of_days," days to",start_date,"we get",init_test.sub_dt(start_date,numbers_of_days))


        elif a == "4":
            end_date = datetime.strptime(input("Enter ending date :-"),'%Y-%m-%d').date()
            print("Numbers of days between",start_date,"and",end_date,"are",init_test.get_days(start_date,end_date),"days")


        elif a == "5":
            end_date = datetime.strptime(input("Enter ending date :-"),'%Y-%m-%d').date()
            print("Numbers of days between",start_date,"and",end_date," excluding weekends are",init_test.get_days_exclude_we(start_date,end_date),"days")


        elif a == "6":
            print("Numbers of days between",start_date,"and ECOCH(1970-01-01) are",init_test.get_days_since_epoch(start_date),"days")


        elif a == "7":
            end_date = datetime.strptime(input("Enter ending date :-"),'%Y-%m-%d').date()       
            print("Numbers of business days between",start_date,"and",end_date,"are",init_test.get_business_days(start_date,end_date),"days")


        else:
            print("Please enter valid input")

    
    except:
        print("Please enter invalid date")

        
    time.sleep(2)


exit()
