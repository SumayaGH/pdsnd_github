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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = CITY_DATA.keys()
    city = input('Would you like to see data for Chicago, New York City, or Washington? ').lower()
    while city not in cities:
        print('That\'s not a valid city name! Please try again.')
        city = input('Would you like to see data for Chicago, New York City, or Washington? ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = input('Would you like to get data from January, February, March, April, May, June, or from all? ').lower()
    while month not in months:
        print('That\'s not a valid month name! Please try again.')
        month = input('Would you like to get data from January, February, March, April, May, June, or from all? ').lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','all']
    day = input('Enter the name of the day if you would like to see data for that specific day. If not, enter all. ').lower()
    while day not in days:
        print('That\'s not a valid day name! Please try again.')
        day = input('Enter the name of the day if you would like to see data for that specific day. If not, enter all. ').lower()
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
    df['day_of_week'] = df['Start Time'].dt.weekday_name



    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1



        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()



    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month:', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most Common Day:', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour

    common_hour = df['hour'].mode()[0]
    print('Most Common Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Satrt Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination = df['Start Station'] + df['End Station']
    popular_station_combination = combination.mode()[0]
    print('Most Frequent Combination Of Station:', popular_station_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Of Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print('Counts Of Users Types:\n', user_types_count)

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_count()
        print('Counts Of Gender:\n', gender_count)
    except:
        pass


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = int(df['Birth Year'].min())
        print('Earliest Birth Year:', earliest_year)
        most_recent_year = int(df['Birth Year'].max())
        print('Latest Birth Year:', most_recent_year)
        most_commoon_year = int(df['Birth Year'].mode())
        print('Most Common Birth Year:', most_commoon_year)
    except:
        pass


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_output(df):

    view = input('\nWould you like to view raw data? Enter yes or no.\n')
    i = 0
    x = 5
    if view.lower() == 'yes':
        check = 0
        while check < len(df):
            if view.lower() == 'yes':
                raw_display = df.iloc[i: x]
                print(raw_display)
                check += 1
                view = input('\nWould you like to view more?\n')
                if view.lower() == 'yes':
                    i += 5
                    x += 5
                    print( raw_display.iloc[i : x])
                elif view.lower() == 'no':
                    break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_output(df)



        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
