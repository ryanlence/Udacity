
# coding: utf-8

# In[ ]:



import pandas as pd
import numpy as np
import time
import csv
from datetime import datetime as dt
import os


# In[ ]:


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


# # Read CSV FILE

# In[ ]:


cd \Users\Guinness PC\Desktop\bikeshare


# In[ ]:


ls


# In[ ]:


CITIES = ['chicago', 'new york', 'washington']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]


# In[20]:


chicago_df= pd.read_csv("chicago.csv")
new_york_city_df=pd.read_csv("new_york_city.csv")
washington_df=pd.read_csv("washington.csv")


# In[21]:


chicago_df.head()


# In[22]:


chicago_df.info


# In[23]:


chicago_df.describe()


# In[24]:


new_york_city_df.head()


# In[25]:


washington_df.head()


# # Get input from the users 

# In[26]:


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
       city = input("Tell us which city data you want to Explore ?  Chicago, New York or Washington? \n> ").lower()
       if city in CITIES:
           break


    # get user input for month (all, january, february, ... , june)
    month = get_user_input('All right! now it\'s time to provide us a month name '                    'or just say \'all\' to apply no month filter. \n(e.g. all, january, february, march, april, may, june) \n> ', MONTHS)


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = get_user_input('One last thing. Could you type one of the week day you want to analyze?'                   ' You can type \'all\' again to apply no day filter. \n(e.g. all, monday, sunday) \n> ', DAYS)


    print('-'*40)
    return city, month, day


# # LOAD DATA

# In[27]:


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour  
     # filter by month if applicable
    if month != 'all':
        month =  MONTHS.index(month) + 1
        df= df[df['month'] == month ]
    
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[ df['day_of_week'] == day.title()]


    return df


# # Displays statistics on the most frequent times of travel."

# In[28]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("The highest  common of the month is :", most_common_month)


    # display the most common day of week
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The highest common day of the  week is :", most_common_day_of_week)


    # display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is :", most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# # Displays statistics on the most popular stations and trip

# In[29]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_popular_start_station = df['Start Station'].value_counts().idxmax()
    print("The most popular used start station is  :",  most_popular_start_station)

    # display most commonly used end station
    most_popular_End_station = df['Start Station'].value_counts().idxmax()
    print("The most popular used End station is  :",  most_popular_End_station)

    # display most frequent combination of start station and end station trip
    most_popular_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}"            .format(most_popular_start_end_station[0], most_popular_start_end_station[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# # Displays statistics on the total and average trip duration

# In[30]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time is :", total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The Mean travel time is :", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# # Displays statistics on bikeshare users.

# In[31]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_counts =df['User Type'].value_counts()

    # Display counts of gender
    if 'Gender' in df.columns:
        user_stats_gender(df)

    if 'Birth Year' in df.columns:
        user_stats_birth(df)


    # Display earliest, most recent, and most common year of birth
    dt.strftime(max(dt.strptime(row[0], "%m/%d/%Y")                     for row in csv.reader(infile)),                 "%m/%d/%Y")
    reader = csv.reader(infile)
    date, *_rest = next(infile)
    date = dt.strptime(date, "%m/%d/%Y")

    for date, *_rest in reader:
        date = dt.strptime(date, "%m/%d/%Y")
        earliest = min(date, earliest)
        latest = max(date, latest)
    print("earliest:", dt.strftime(earliest, "%m/%d/%Y"))
    print("latest:", dt.strftime(latest, "%m/%d/%Y"))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[32]:


def datetime_conversion(df):
    df["Start Time"]=pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday_name
    df["hour"] = df["Start Time"].dt.hour
    return df


# In[33]:


def main():
    while True:
        CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
        
        chicago_df= pd.read_csv("chicago.csv")
        new_york_city_df= pd.read_csv("new_york_city.csv")
        washington_df= pd.read_csv("washington.csv")
        
        
        dfs=(chicago_df,new_york_city_df,washington_df)
        
        for _ in dfs: 
            datetime_conversion(_ , "Start Time")
            datetime_conversion(_ , "End Time")
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

