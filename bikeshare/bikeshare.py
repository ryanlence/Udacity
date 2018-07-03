import time
import pandas as pd
import numpy as np

place = pd.Series(['chicago.csv', 'new_york_city.csv', 'washington.csv'], ['wind', 'apple', 'rain'])
months = ['january', 'febuary', 'march', 'april', 'may', 'june']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']


def load_city():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city = input('\nHi! here is some bikeshare data...\n'
                 '\nPick your city Chicago (CH), New York (NY), Washington (WA)?\n')
    city = city.lower()

    while True:
        if city == "ny":
            print("\nWelcome to the Big Apple, enjoy the data\n")
            return place['apple']
        elif city == "ch":
            print("\nWelcome to the Windy City, enjoy the data\n")
            return place['wind']
        elif city == "wa":
            print("\nWelcome to the Land of Rain, enjoy the data\n")
            return place['rain']
        city = input("Select Chicago (CH), New York (NY), Washington (WA)")


def load_time():
    # ask for the user time

    time = input('\nSelect if you want to filter by month or day\n')

    time = time.lower()

    if time == 'month':
        return ['month', load_month()]
    if time == 'day':
        return ['day', load_day()]
    else:
        print('\nCan you try that again?')


def load_month():
    # get user input for month (all, january, february, ... , june)

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
        month = input('Select January, February, March, April, May, or June? Please type the full month name.\n')


def load_day():
    # get user input for day of week (all, monday, tuesday, ... sunday)

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
        day = input('Select Monday, Tuesday, Wednesday, Thursday, Friday, Saturday \n')


def load_data(city):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print('\nLoading the data...\n')
    df = pd.read_csv(city)

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['month'] = df['Start Time'].dt.month
    df["day_of_month"] = df["Start Time"].dt.day

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    # display the most common day of week

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("\n* What is the most popular start station?\n")
    start_station = df['Start Station'].value_counts().reset_index()['index'][0]
    print(start_station)

    # display most commonly used end station
    print("\n* What is the most popular end station?\n")
    end_station = df['End Station'].value_counts().reset_index()['index'][0]
    print(end_station)

    return end_station

    # display most frequent combination of start station and end station trip

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    # display mean travel time

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    # Display counts of gender

    # Display earliest, most recent, and most common year of birth

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def gender(df):
    gender_counts = df.groupby('Gender')['Gender'].count()
    return gender_counts


def main():
    while True:
        city = load_city()
        time = load_time()
        # month = load_month()
        # day = load_day()
        df = load_data(city)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)


if __name__ == "__main__":
    main()
