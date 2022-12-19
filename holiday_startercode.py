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
        if type(holidayObj) != Holiday:
            print("The holiday you entered is not a valid holiday! Please try again.")
        
        
        # Use innerHolidays.append(holidayObj) to add holiday
        h = Holiday(
        name = h['name'],
        date = h['date']
        )
        self.innerHolidays.append(h)
        
        # print to the user that you added a holiday
        print(f'Great Job! You have added {holidayObj} within your holiday list.')


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
        filelocation = 'Module7Assessment/holidays.json'
        with open (filelocation, "r") as f:
            data = json.load(f, indent=4)
            print (data)
            
       
        # Use addHoliday function to add holidays to inner list.
            for i in data["holidays"]:
                 h = Holiday(
                name = h['name'],
                date = h['date']
                )
                self.addHoliday(h)

    
    
    def save_to_json(self, filelocation):
        # Write out json file to selected file.
        pass
    
    
    def scrapeHolidays(self):
        # Scrape Holidays from https://www.timeanddate.com/holidays/us/ 
        
        # Remember, 2 previous years, current year, and 2  years into the future. You can scrape multiple years by adding year to the timeanddate URL. For example https://www.timeanddate.com/holidays/us/2022
        
            # want the years from 2020 to 2024. 
            # number of holidays in 2020 = 379
            # number of holidays in 2021 = 347
            # number of holidays in 2022 = 351
            # number of holidays in 2023 = 341
            # number of holidays in 2024 = 333
        
            scrape_holidays = []
            
            for year in range (2020,2025):
            
                html = requests.get("https://www.timeanddate.com/holidays/us/{year}")
                soup = BeautifulSoup(html, "html.parser")
                table = soup.find("table", attrs = {'id':'holidays-table'})
                tbody = table.find('tbody')
                
            
                
                
                
                
                
        
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
       pass
    
    
    def displayHolidaysInWeek(self, holidayList):
        # Use your filter_holidays_by_week to get list of holidays within a week as a parameter
        for i in holidayList: 
            if holidayList == None:
                print("This holiday is not shown within the calendar.")
            else:
                print("This holiday is shown within the calendar.")
        # Output formated holidays in the week. 
        
        # * Remember to use the holiday __str__ method.
    
    
    
    def viewCurrentWeek(self):
        # Use the Datetime Module to look up current week and year
      
        # Use your filter_holidays_by_week function to get the list of holidays 
        
        # for the current week/year
        
        # Use your displayHolidaysInWeek function to display the holidays in the week
      



def main():

    # Large Pseudo Code steps
    # -------------------------------------
    # 1. Initialize HolidayList Object
    
    initializing_holidaylist = HolidayList()
    
    # 2. Load JSON file via HolidayList read_json function
    
    initializing_holidaylis.read_json("holidays.json")
    
    # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
    
    initializing_holidaylist.scrapeHolidays()
    
    # 3. Create while loop for user to keep adding or working with the Calender
    
    menu_user = True
    saved_work = False
    
    Print("Holiday Management")
    Print("===================")
    
    
    
    # 4. Display User Menu (Print the menu)
    
    while menu_user: 
        
        Print('Holiday Menu')
        Print("===========")
        Print("1. Add a Holiday")
        Print("2. Remove a Holiday")
        Print("3. Save Holiday List")
        Print("4. View Holidays")
        Print("5. Exit")
        
        Menu_options = int(input(f'Please select an option shown above.'))
    
        if Menu_options == 1:
            Print("Add a Holiday")
            Print("==============")
            holiday_choice = str(input(f'Please add a holiday:'))
            holiday_date = int(input(f'Please add a date (YYYY-MM-DD): ')
        
        if Menu_options == 2:
            Print("Remove a Holiday")
            remove_holiday = str(input(f'Name of the holiday you want to be removed:'))
        

        if Menu_options == 3:
            Print("Save Holiday List")
            Print("===================")
            save_holiday = str(input(f'Are you sure you want to save your changes? [y/n]:'))
                if save_holiday == 'y':  
                    print("Your holiday has been saved within the calendar!")
                    saved_work = True
                else:
                    Print("Sorry, the changes you have made have not been saved.")


        if Menu_options == 4:
            Print("View Holidays")
            Print("==============")
            holiday_year = int(input("Which year?"))
            holiday_week = str(input('Which week?'))

        if Menu_options == 5:
            Print('Exit')
            Print("=====")
            if saved_work = True:
                holiday_exit = str(input("Are you sure you want to exit? [y/n]:"))
                


    
    
    # 5. Take usehhor input for their action based on Menu and check the user input for errors
    
    # 6. Run appropriate method from the HolidayList object depending on what the user input is
    
    # 7. Ask the User if they would like to Continue, if not, end the while loop, ending the program.  If they do wish to continue, keep the program going.
    
    if __name__ == "__main__":
        main();





