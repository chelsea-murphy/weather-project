import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"

def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date=datetime.fromisoformat(iso_string) 
    return date.strftime("%A %d %B %Y")


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    celsius = (float(temp_in_fahrenheit) - 32) * 5 / 9
    return round(celsius,1)
#example = "77"
#convert_f_to_c(example)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    # get sum 
    total = 0
    for each_number in weather_data:
        #print(each_number)
        total=total + float(each_number)
    # get mean
    mean = total/len(weather_data)
    return mean
#weather_data = ["51", "58", "59", "52", "52", "48", "47", "53"]
#print(f"The mean is {calculate_mean(weather_data)}")


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    weather_data = []
    with open(csv_file) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            #if len (row) == 0 : 
            # continue
            #if not row: 
            #   continue
            if row: 
                row[1] = int(row[1])
                row[2] = int(row[2])
                weather_data.append (row)
        return weather_data
            #print (row)
result = load_data_from_csv("tests/data/example_two.csv")
#print(result)

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    #find min in list
    #assume first value is minimum
    min = float(weather_data [0])
    min_position = 0
    for i, number in enumerate(weather_data):
        number = float(number)
        #print (f"position{i} value{number}")
        if (number <= min):
            min = number
            min_position = i
    return (min,min_position)
        #print(min)
    #return (min,)

#my_list = ["49", "57", "56", "55", "53", "49"]
#print (find_min(my_list))
#print(f"The index of the last occurrence of the minimum value ({min(my_list)}) is: {last_min_index}")


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    max = float(weather_data [0])
    max_position = 0
    for i, number in enumerate(weather_data):
        number = float(number)
        #print (f"position{i} value{number}")
        if (number >= max):
            max = number
            max_position = i
    return (max,max_position)
        #print(min)
    #return (min,)

#my_list = ["49", "57", "56", "55", "57", "49"]
#print (find_max(my_list))


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    min = float(weather_data [0])
    min_position = 0
    for i, number in enumerate(weather_data):
        number = float(number)
        if (number <= min):
            min = number
            min_position = i
    return (min,min_position)


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
