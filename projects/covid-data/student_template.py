import sys
import numpy as np
import pandas as pd
import math

def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date, county, state, cases, deaths) information
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

def first_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """

    # your code here
    # create new dataframe from provided data
    df = pd.DataFrame(data, columns=['date','county','state','cases','deaths'])

    # isolate rockingham/harrisonburg city, virginia, and when cases are greater than or equal to 1
    df_RC = df[(df['county'] == 'Rockingham') & (df['state'] == 'Virginia') & (df['cases'] >= 1)]
    df_HB = df[(df['county'] == 'Harrisonburg city') & (df['state'] == 'Virginia') & (df['cases'] >= 1)]

    # find the date of the first appearance of a covid case as from previously sorted dataframe
    RC_COVID_Date = df_RC.iloc[0]['date']
    HB_COVID_Date = df_HB.iloc[0]['date']

    # print results
    print(f"The first positive COVID case in Rockingham County was on {RC_COVID_Date}")
    print(f"The first positive COVID case in Harrisonburg was on {HB_COVID_Date}")

    return

def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """

    # create new dataframe from provided data
    df = pd.DataFrame(data, columns=['date', 'county', 'state', 'cases', 'deaths'])

    # isolate rockingham/harrisonburg city and virginia dataframe data
    df_RC = df[(df['county'] == 'Rockingham') & (df['state'] == 'Virginia')]
    df_HB = df[(df['county'] == 'Harrisonburg city') & (df['state'] == 'Virginia')]

    # find the differences between each datapoint within the 'cases' column of data and take absolute value
    difference_RC = df_RC['cases'].diff().abs()
    difference_HB = df_HB['cases'].diff().abs()

    # find the index of the maximum value within the previously found datapoints
    index_RC_cases = difference_RC.idxmax()
    index_HB_cases = difference_HB.idxmax()

    # find the date in which there was the greatest number of new daily cases
    jump_date_RC = df_RC.loc[index_RC_cases, 'date']
    jump_date_HB = df_HB.loc[index_HB_cases, 'date']

    # print results
    print(f"the greatest number of new daily cases recorded in Rockingham County was on {jump_date_RC}")
    print(f"the greatest number of new daily cases recorded in Harrisonburg was on {jump_date_HB}")

    return

def third_question(data):
    # Write code to address the following question:Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.

    # create new dataframe from provided data
    df = pd.DataFrame(data, columns=['date', 'county', 'state', 'cases', 'deaths'])

    # isolate rockingham/harrisonburg city and virginia dataframe data
    df_RC = df[(df['county'] == 'Rockingham') & (df['state'] == 'Virginia')]
    df_HB = df[(df['county'] == 'Harrisonburg city') & (df['state'] == 'Virginia')]

    # find the differences between each period of 7 days within the 'cases' column of data
    difference_RC = df_RC['cases'].diff(periods=6).abs()
    difference_HB = df_HB['cases'].diff(periods=6).abs()

    # determine which area has the worst 7-day period of new covid cases
    if difference_RC.max() > difference_HB.max():
        index_cases = difference_RC.idxmax()                     #finds the index of the largest difference
        worst_period = df_RC.loc[index_cases, 'date']            #finds the initial day of the worst 7 day period w.r.t. new COVID cases
        area = "Rockingham"                                      #sets and "area" parameter for results

    else:
        index_cases = difference_HB.idxmax()
        worst_period = df_HB.loc[index_cases, 'date']
        area = "Harrisonburg city"

    # print results
    print(f"The worst 7 day period of new covid cases started on {worst_period} in {area}")

    return

if __name__ == "__main__":
    data = parse_nyt_data('us-counties.csv')

    #for (date, county, state, cases, deaths) in data:
     #   print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')


    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    first_question(data)


    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    second_question(data)

    # write code to address the following question:Use print() to display your responses.
    # What was the worst seven day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    third_question(data)


