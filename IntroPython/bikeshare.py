import pandas as pd
import numpy as np
import time
import csv
from datetime import datetime as dt
import os

place = pd.Series(['chicago.csv', 'new_york_city.csv', 'washington.csv'], ['wind', 'apple', 'stress'])
months = ['january', 'febuary', 'march', 'april', 'may', 'june']
days = ['sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def main():
    get_city()
    get_time()



def get_city():

    city = input('\nHello here is some very cool data about sharing bikes........\n'
                 '\nPick the city that you want to know about Chicago (CH), New York (NY), Washington (WA)\n')

    city = city.lower()

    while True:
        if city == 'ny':
            print('\nWelcome to the Big Apple, enjoy the bike data\n')
            return place['apple']
        elif city == 'ch':
            print('\nWelcome to the Wind, enjoy the bike data\n')
            return place['wind']
        elif city == 'wa':
            print('\nWelcome to the Stress, enjoy the bike data\n')
            return place['stress']
        else:
            print('Sorry can you say that again??')
            city = input('\nHello here is some very cool data about sharing bikes........\n'
                         '\nPick the city that you want to know about Chicago (CH), New York (NY), Washington (WA)\n')


def get_time():
    times = input('\nPick your time...  Month (M), Day (D), or None (N)\n')

    times = times.lower()

    while True:
        if times == 'm':
            print('\nYou have chosen to view data by the month\n')
            return get_month()
        elif times == 'd': 
            print('\nYou have chosen to view the data by the day\n')
            return get_day()
        elif times == 'n':
            print('\nYou are skipping time\n')
            return
        else:
            times = input('\nPick your time...  Month (M), Day (D), or None (N)\n')
            


def get_month():
    month = input('\nWhich month? January, February, March, April, May, or June? Please type the full month name.\n')

    month = month.lower()

    while True:
        if month == 'january':
            print("\nHappy new year\n")
            return months[0]
        elif month == 'february':
            print("\nHappy winter\n")
            return months[1]
        elif month == 'march':
            print("\nHappy St. Pat\n")
            return months[2]
        elif month == 'april':
            print("\nHappy April Showers\n")
            return months[3]
        elif month == 'may':
            print("\nHappy May showers\n")
            return months[4]
        elif month == 'june':
            print("\nHappy Summer\n")
            return months[5]
        else:
            month = input('Select January, February, March, April, May, or June? Please type the full month name.\n')


def get_day():
    day = input('\nWhich day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday \n')

    day = day.lower()

    while True:
        if day == 'sunday':
            print("\nGood Sabbath\n")
            return days[0]
        elif day == 'monday':
            print("\nHappy Monday\n")
            return days[1]
        elif day == 'tuesday':
            print("\nHappy 2nd friday\n")
            return days[2]
        elif day == 'wednesday':
            print("\nHappy Hump Day\n")
            return days[3]
        elif day == 'thursday':
            print("\nTired Thursday\n")
            return days[4]
        elif day == 'friday':
            print("\nIt's Friday\n")
            return days[5]
        elif day == 'saturday':
            print("\nHappy Yard Day\n")
            return days[6]
        else:
            day = input('Select Monday, Tuesday, Wednesday, Thursday, Friday, Saturday \n')


def load_data():
    pass


if __name__ == '__main__':
    main()
# -*- coding: utf-8 -*-

