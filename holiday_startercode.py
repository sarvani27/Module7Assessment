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
        
        findHoliday = Holiday(HolidayName, Date)
        for i in self.innerHolidays:
            if i == findHoliday:
                return i 
        return False
    
    
    def removeHoliday(self, HolidayName, Date):
        # Find Holiday in innerHolidays by searching the name and date combination.
        # remove the Holiday from innerHolidays
        # inform user you deleted the holiday
       
        removeHoliday = self.findHoliday(HolidayName, Date)
        if removeHoliday == False:
            return False
        else:
            self.innerHolidays.remove(removeHoliday)

    
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

    # 1. Initialize HolidayList Object
    init_holidaylist = HolidayList()
    # 2. Load JSON file via HolidayList read_json function
    filelocation = "holidays.json"
    init_holidaylist.read_json(filelocation)
    # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
#     initList.scrapeHolidays()
    # 3. Create while loop for user to keep adding or working with the Calender
    mainmenu = True
    savedWork = False

    print("Welcome to Holiday Manager!")
    print("===================")
#     print(f"There are {init_holidaylist.numHolidays()} holidays stored in the system.")
 
    
    while mainmenu:
    # Display User Menu (Print the menu)
        print("Holiday Menu")
        print("===================")
        print("1. Add a Holiday")
        print("2. Remove a holiday")
        print("3. Save Holiday List")
        print("4. View Holidays")
        print("5. Exit")
        option_menu = int(input("Please select an option shown above: "))
        if option_menu == 1:
            print("Add a Holiday")
            print("===================")
            holiday_choice = (input("Please add a holiday: "))
            holiday_date = input("Please add a date (YYYY-MM-DD): ")
            init_holidaylist.addHoliday(Holiday(holiday_choice, holiday_date))
        elif option_menu == 2:
            print("Remove a Holiday")
            print("===================")
            remove_holidayname = str(input("Name of the holiday you want to be removed:"))
            remove_holidaydate = input("Date of the holiday (YYYY-MM-DD):")
            init_holidaylist.removeHoliday(remove_holidayname, remove_holidaydate)
#             if success == 1:
#                 print ("Success! Your holiday has been removed from the system.")
#             else: 
#                 print("Sorry, your holiday has not been found.")
        elif option_menu == 3:
            print("Saving Holiday List")
            print("===================")
            wantSave = str(input("Do you want to save your changes? [Y/N]: "))
            if wantSave == "Y":
                initList.save_to_json(filelocation)
                print("Success! Your changes have been saved!")
                savedWork = True
            else:
                print("Sorry! your changes have not been saved.")
        elif option_menu == 4:
            print("View Holidays")
            print("===================")
            holiday_year = input("Please select a year between 2020 and 2024: ")
            holiday_week = input("Which week? (1-52)... Leave blank for current week]: ")
            if holiday_week == "":
                init_holidaylist.viewCurrentWeek()
            else:
                print(f"These are the holidays for {holiday_year} week {holiday_week}:")
                init_holidaylist.displayHolidaysInWeek(init_holidaylist.filter_holidays_by_week(holiday_year, holiday_week))
        elif option_menu == 5:
            if savedWork == True:
                exit_option = input("Do you want to exit? [Y/N]: ")
                if exit_option == 'Y':
                    print('Goodbye!')
                    break
                elif exit_option == 'N':
                    continue
            elif savedWork == False:
                unsaved_exit_option = input("Are you sure you want to exit? Your changes will be lost! [Y/N]: ")
                if unsaved_exit_option == 'Y':
                    print("Goodbye!")
                    break
                elif unsaved_exit_option == 'N':
                    continue

                  
        else:
            print('Something went wrong. Try again.')
            
if __name__ == "__main__":
    main();









