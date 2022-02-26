#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }           

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    cities=['chicago','new york city','washington']
    months=["january","febraury","march","april","may","june","july","augest","septemper","ocober","november","december","all"]
    days=["saterday","sunday","monday","tuesday","wednesday","thursday","friday","all"]
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input ("Please Entre the City you Want  : ").lower()
        if city not in cities :
            print("Pleaes Enter chicago or new york city or washington")
        else :
            print("you choose {} and you can analyze it".format(city))
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month =input ("please Enter the Month you want OR Enter all if you  want all Months :").lower()
        if month not in months :
            print("Pleaes Enter The Correct month ! ")
        else :
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input ("please Enter the Name of the day of week you want OR Enter all if you want all das :").lower()
        if day not in days:
            print("Please Enter the correct day")
        else :
            break


    print('-'*40)
    return city, month, day



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
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
    
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month']==month]
        
      
    if day != 'all':
        
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month is :{}".format(df['month'].mode()[0]))


    # display the most common day of week
    print("The most common day is :{}".format(df['day_of_week'].mode()[0]))


    # display the most common start hour
    print("The most common hour is :{}".format(df['hour'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used start station is : {}".format(df['Start Station'].mode()[0]))


    # display most commonly used end station
    print("The most commonly used end station is : {}".format(df['End Station'].mode()[0]))


    # display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip is : {}".format(df.groupby(['Start Station','End Station']).size().nlargest(1)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("The total travel time is: {}".format(df['Trip Duration'].sum()))


    # display mean travel time
    print("The mean travel time is : {}".format(df['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("The counts of user types is : {}".format(df['User Type'].value_counts()))


    # Display counts of gender
    city_column=df.columns
    if "Gender" in city_column :
        print("The counts of gender is : {}".format(df['Gender'].value_counts()))
    else :
        print("This column not found in this city")


    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in city_column :
        print("The earliest year of bith is : {}".format(df['Birth Year'].min()))
        print("The most recent year of bith is : {}".format(df['Birth Year'].max()))
        print("The most common year of bith is : {}".format(df['Birth Year'].mode()[0]))
    else :
        print("This column not found in this city")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    start_loc = 0
    
        
    while view_data =="yes":
        
            print(df.iloc[start_loc:start_loc + 5])
            start_loc += 5
            view_data = input("Do you wish to continue?: ").lower()
            
       
            
          
        
       



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:




