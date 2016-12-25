import csv
import pytz
from datetime import datetime

utc = pytz.utc


def csv_writer(parsed_times):
    pass


def format_time_zones(hour, minute):
    localFormat = "%H:%M:%S"
    raw_year = 1900  # place holder year use %Y-%m-%d if date needs to added
    raw_mon = 1  # place holder month
    raw_day = 1  # place holder day
    utcmoment_unaware = datetime(raw_year, raw_mon, raw_day, hour, minute)
    utcmoment = utcmoment_unaware.replace(tzinfo=pytz.utc)

    timezones = ['America/Los_Angeles', 'Europe/Madrid',
                 'America/Argentina/San_Juan', 'US/Eastern', 'UTC']

    for tz in timezones:
        localDatetime = utcmoment.astimezone(pytz.timezone(tz))
        print(tz, '-', localDatetime.strftime(localFormat))


def main():
    csv_file = 'raw_times.csv'
    with open(csv_file) as filename:
        reader = csv.reader(filename)
        for row in reader:
            raw_time = str(row)
            print(raw_time)
            print('Length of time: ',len(raw_time))
            if len(raw_time) == 8:
                raw_hour = int(raw_time[2])
                raw_minute = int(raw_time[4:6])
                print('Raw Hour from 8: ', raw_hour)  # debugging
                print('Raw minute from 8: ', raw_minute)  # debugging
            elif len(raw_time) == 9:
                raw_hour = int(raw_time[2:4])
                raw_minute = int(raw_time[5:7])
                print('Raw Hour from 8: ', raw_hour)  # debugging
                print('Raw minute from 8: ', raw_minute)  # debugging
            format_time_zones(raw_hour, raw_minute)


if __name__ == '__main__':
    main()
