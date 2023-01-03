import datetime
import json
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass


# -------------------------------------------
# Modify the holiday class to 
# 1. Only accept Datetime objects for date.
# 2. You may need to add additional functions
# 3. You may drop the init if you are using @dataclasses
# --------------------------------------------
        
@dataclass
class Holiday:
    name : str
    date : datetime.date

# -------------------------------------------
# The HolidayList class acts as a wrapper and container
# For the list of holidays
# Each method has pseudo-code instructions
# --------------------------------------------
class HolidayList():
    def __init__(self):
       self.innerHolidays = []
   
    
    def addHoliday(self, holidayObj):
        # Make sure holidayObj is an Holiday Object by checking the type
        # Use innerHolidays.append(holidayObj) to add holiday
        # print to the user that you added a holiday

        if isinstance(holidayObj, Holiday):
            self.innerHolidays.append(holidayObj)
            print(f'Success! You have added {holidayObj} within your holiday list.')
        

    def findHoliday(self, HolidayName, Date):
        # Find Holiday in innerHolidays
        # Return Holiday
        
        for i in innerHolidays:
            if i.name == HolidayName and i.date == Date:
                print(f'{i} has been found within your calendar!')
                return Holiday
            else: 
                print(f'Sorry, the holiday you looked for is not within the calendar.')
    
    
    def removeHoliday(self, HolidayName, Date):
        # Find Holiday in innerHolidays by searching the name and date combination.
        # remove the Holiday from innerHolidays
        # inform user you deleted the holiday
        for i in innerHolidays:
            if i.name == HolidayName and i.date == Date:
                self.innerHolidays.remove(i)
                print(f' Holiday: {i} has been removed from your calendar')
            else:
                print(f' Holiday: {i} is not within your calendar! This cannot be removed.')
    
    
    def read_json(self, filelocation):
        # Read in things from json file location
        # Use addHoliday function to add holidays to inner list.

        with open(filelocation) as f:
            data = json.load(f)
            for i in data['holidays']:
                add_holi = Holiday(i['name'], i['date'])
                self.addHoliday(add_holi)

    
    
    def save_to_json(self, filelocation):
        # Write out json file to selected file.

        save_holidays = json.dumps(self.innerHolidays, indent = None)
        with open('holidays.json', 'r') as f:
            f.write(save_holidays)
        
    
    
#     def scrapeHolidays(self):
        # Scrape Holidays from https://www.timeanddate.com/holidays/us/ 
        # Remember, 2 previous years, current year, and 2  years into the future. You can scrape multiple years by adding year to the timeanddate URL. For example https://www.timeanddate.com/holidays/us/2022       
        # Check to see if name and date of holiday is in innerHolidays array
        # Add non-duplicates to innerHolidays
        # Handle any exceptions.     
    
    
    def numHolidays(self):
        # Return the total number of holidays in innerHolidays
        return len(self.innerHolidays())
       
    
    def filter_holidays_by_week(self, year, week_number):
        # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays
        # Week number is part of the the Datetime object
        # Cast filter results as list
        # return your holidays
        
        holidayweek = list(filter(lambda a: a.values()[1].strftime('%W') == week_number and a.values()[1].strftime('%Y') == year, self.holidayobject))
        return holidayweek
        
    
    
    def displayHolidaysInWeek(self, holidayList):
        # Use your filter_holidays_by_week to get list of holidays within a week as a parameter
        # Output formated holidays in the week. 
        # * Remember to use the holiday __str__ method.
        
        for i in holidayList: 
            if holidayList == None:
                print("This holiday is not shown within the calendar.")
            else:
                print("This holiday is shown within the calendar.")
 
    
    
    def viewCurrentWeek(self):
        # Use the Datetime Module to look up current week and year
        # Use your filter_holidays_by_week function to get the list of holidays 
        # for the current week/year
        # Use your displayHolidaysInWeek function to display the holidays in the week
      
        today = datetime.today()
        iso = today.isocalendar()
        weeknumber = iso[1]
        return weeknumber 


def main():
    initholiday = HolidayList()
    filelocation = "holidays.json"
    initholiday.read_json(filelocation)
    changes = 0
    stop = 0
    
    while stop == 0:
        print('Holiday Menu')
        print("===========")
        print("1. Add a Holiday")
        print("2. Remove a Holiday")
        print("3. Save Holiday List")
        print("4. View Holidays")
        print("5. Exit")
        option_menu = int(input('Please select an option shown above:'))

        if option_menu == '1':
            holiday_choice = input('Please add a holiday: ')
            holiday_date = input('Please add a date (YYYY-MM-DD): ')
            success = initholiday.addHoliday(holiday_choice, holiday_date)
            if success == 1:
                changes = 1
            else:
                print(" Your holiday has not been found.")

        elif option_menu == '2':
            remove_holidayname = input('Name of the holiday you want to be removed: ')
            remove_holidaydate = input('Date of the holiday (YYYY-MM-DD): ')
            success = initholiday.removeHoliday(remove_holidayname, remove_holidaydate)
            if success == 1:
                changes = 1
            else:
                print('Your holiday has not been found.')

        elif option_menu == '3':
            if changes == 0:
                print('Your changes have not been saved.')
            else:
                initholiday.save_to_json(filelocation)
                print('Your changes have been saved.')
                changes = 0

        elif option_menu == '4':
            print("View Holidays")
            holiday_year = int(input("Please select a year between 2020 and 2024: "))
            holiday_week = input("Which week? (1-52)... Leave Blank for current week: ")
            if week == "":
                initholiday.viewCurrentWeek(year)
            else:
                initholiday.displayHolidaysInWeek(year, week)

        elif option_menu == '5':
            if changes == 0:
                print('Goodbye!')
#                 stop = 1
            else:
                holiday_exit = input('Do you want to exit? [y/n]: ')
                if holiday_exit == "y":
                      initholiday.save_to_json(filelocation)
                      print("Goodbye!")
                      stop = 1
                else: 
                      print("Return to menu.")
                      stop = 1
                  
        else:
            print('Something went wrong. Try again.')
            
if __name__ == "__main__":
    main();







