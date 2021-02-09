"""This script is used to process data for the data report files generated
by a third party software. Due to the limitations of the third party software, 
the data output produced does not meet the requirements of the business, 
this lightweight data processing script is developed to process the data to the
expected output result.
Script Author: Nicholas Chin (Bits-AI)
©2020 Nicholas Chin (Bits-AI). All Rights Reserved.
"""

import os
import csv
from datetime import datetime, timedelta

def read_config():
    """Function to read the configuration file to get
    the user defined datetime format and filename prefix.
    """

    try:
        with open(f"./config.txt", "r") as config_file:
            line_count = 1
            
            for row in config_file:
                
                #Read the file prefix at line 8 in config.txt
                if line_count == 8:
                    configuration_prefix = row.split("=")
                    file_prefix = configuration_prefix[1]

                    return file_prefix

                line_count += 1

    except Exception as error:
        print("Invalid settings detected in the configuration file!")

def file_process(filename, file_prefix):
    """Main function to process the data."""

    try:
        with open(f"../Output/{file_prefix}_{filename}", "w", newline="") as csv_write:
            writer = csv.writer(csv_write)

            with open(f"../Source/{filename}") as csv_file:
                csv_reader = csv.reader(csv_file)
                line_count = 1

                for row in csv_reader:
                    #Write whatever text generated in the first 12 lines
                    if line_count < 12:
                        writer.writerow(row)

                    #Write the column headers for the Data Report
                    elif (line_count == 12):
                        writer.writerow(['Date', 'Time', 'Rainfall@0550161RF'])

                    #Start to process the data
                    else:
                        timestamp = row[0].split(" ")

                        #Convert the date section to date object first
                        date = format_date(timestamp[0])

                        new_date, new_time = format_timestamp(date, timestamp[1])

                        value = format_value(row[1], filename)

                        writer.writerow([new_date, new_time, value])

                    print(f"{line_count} lines processed.\r", end="")

                    line_count += 1

                return line_count

    except Exception as error:
        print(f"Unable to process the file {filename}. Invalid data format detected in the file.")

def format_date(date_raw):
    """Function to convert the extracted date value to date object."""

    #Multiple date formats here because the incoming dates do not have a fixed format
    #Try multiple date formats
    try:
        date = datetime.strptime(date_raw, "%Y-%m-%d")

    except ValueError:
        try:
            date = datetime.strptime(date_raw, "%Y/%m/%d")

        except ValueError:
            try:
                date = datetime.strptime(date_raw, "%d/%m/%Y")

            except ValueError:
                date = datetime.strptime(date_raw, "%d-%m-%Y")

    finally:
        return date

def format_timestamp(date, time):
    """Function to convert the extracted time value
    to the required time format 24:00 if the value is
    0:00, else write the original value only.
    """

    #Check the time if it is equals to 12am midnight
    if (time == "0:00"):
        date_calc = date - timedelta(days=1)
        new_date = datetime.strftime(date_calc, "%d/%m/%Y")
        new_time = "24:00"

    elif (time == "00:00:00"):
        date_calc = date - timedelta(days=1)
        new_date = datetime.strftime(date_calc, "%d/%m/%Y")
        new_time = "24:00:00"

    else:
        new_date = datetime.strftime(date, "%d/%m/%Y")
        new_time = time

    return new_date, new_time

def format_value(value_raw, filename):
    """Function for formatting the decimal points."""

    #Solve the decimal point issue
    try:
        float_value = float(value_raw)
        if (float_value % 1 == 0):
            value = int(float_value)

        else:
            value = float_value

    #If the value cannot be converted to float
    except ValueError:
        value = value_raw

    finally:
        return value

if __name__ == "__main__":
    file_prefix = read_config()

    #List the file in Source folder
    arr = os.listdir('../Source')

    if len(arr) == 0:
        print("There is no file in the source folder.")

    else:
        print(f"Detected {len(arr)} files in source folder.")
        for i in range(len(arr)):
            print(f"Processing file {arr[i]}...")
            line_count = file_process(arr[i], file_prefix)
            print(f"Done processing file {arr[i]}, {line_count} lines were processed.\n")
