#!/usr/bin/env python
import sys
import json

# field position of each row taken from stdin
SECTOR = 0
TICKER = 1
DATE = 2
CLOSE = 3
VOLUME = 4


class AverageObject:
    def __init__(self, value=0.0):
        self.value = value
        self.count = 1 if value else 0

    def add(self, value):
        self.value += value
        self.count += 1

    def avg(self):
        return self.value / self.count


class Record:
    def __init__(self):
        self.avg_year_volume = AverageObject()
        self.avg_year_change_company = AverageObject()
        self.avg_daily_price = AverageObject()

    def add_volume(self, volume):
        self.avg_year_volume.add(volume)

    def add_year_change(self, year_change):
        self.avg_year_change_company.add(year_change)

    def add_daily_price(self, daily_price):
        self.avg_daily_price.add(daily_price)


class Sector:
    def __init__(self, name):
        self.name = name
        self.year_2_record = {}

    def update(self, year, volume, year_change, daily_price):
        if not (year in self.year_2_record):
            self.year_2_record[year] = Record()
        self.year_2_record[year].add_volume(volume)
        self.year_2_record[year].add_year_change(year_change)
        self.year_2_record[year].add_daily_price(daily_price)


result = {}

current_sector = None
current_ticker = None
current_year = None
volume_ticker_year = 0
first_close_ticker_year = 0
last_close_ticker_year = 0
avg_price_ticker_year = AverageObject()


def parse_values(value_list):
    sector = value_list[SECTOR].strip()
    ticker = value_list[TICKER].strip()
    date = value_list[DATE].strip()
    close = float(value_list[CLOSE].strip())
    volume = int(value_list[VOLUME].strip())
    return (sector, ticker, date, close, volume)


def update():
    app_year_change = ((last_close_ticker_year - first_close_ticker_year) / first_close_ticker_year) * 100
    result[current_sector].update(current_year, volume_ticker_year, app_year_change, avg_price_ticker_year.avg())


# main script
for line in sys.stdin:
    value_list = line.strip().split(',')

    if len(value_list) == 5:
        sector, ticker, date, close, volume = parse_values(value_list)
        year = int(date[0:4])

        if not current_sector:
            result[sector] = Sector(sector)
            volume_ticker_year = volume
            first_close_ticker_year = close
            last_close_ticker_year = close
            avg_price_ticker_year.add(close)
        else:
            if current_sector == sector:
                if current_ticker == ticker:
                    if current_year == year:
                        volume_ticker_year += volume
                        last_close_ticker_year = close
                        avg_price_ticker_year.add(close)
                    else:
                        update()
                        volume_ticker_year = volume
                        first_close_ticker_year = close
                        last_close_ticker_year = close
                        avg_price_ticker_year = AverageObject(close)
                else:
                    update()
                    volume_ticker_year = volume
                    first_close_ticker_year = close
                    last_close_ticker_year = close
                    avg_price_ticker_year = AverageObject(close)
            else:
                result[sector] = Sector(sector)
                update()
                volume_ticker_year = volume
                first_close_ticker_year = close
                last_close_ticker_year = close
                avg_price_ticker_year = AverageObject(close)

        current_sector = sector
        current_ticker = ticker
        current_year = year

# print last computed key
if current_sector:
    update()

for r in result:
    sector = result[r]
    print(str(sector.name) + ":")
    for year in sector.year_2_record.keys():
        record = sector.year_2_record[year]
        print("\t-" + str(year) + " { " + str(record.avg_year_volume.avg()) + ", " + str(
            record.avg_year_change_company.avg()) + ", " + str(record.avg_daily_price.avg()) + "}")
