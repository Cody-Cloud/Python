"""
Author: Cody Swindells

Created: 23/08/21

Modified: 31/08/21

I decided to add web scraping to some of the random number and list task as a advance task set for myself

This module requies beauitful soup and requests to be installed

#FIXED - Getting close, csv has been implemented but some error need to be fix for both functional purpose to work - line 149 key error state_names

Notes :- I am considering learning about GUI in python. Most of the classes we eventually be connect to a single GUI to use each of the classes.

"""
import requests as r
from bs4 import BeautifulSoup
import random
from datetime import datetime
from time import sleep
from tqdm import tqdm
import pandas as pd

"""
Some useful notes From Python Course:

love_score = random.randint(1, 100)

print(f"Your love score is {love_score}") # had a similar functionality `Your love score is ${insert var here}` starts with f before " {}"
"""

class states:
    """
    The main object which contains all method related to lists and states. 
    It was a part of larger advance task I set for myself.

    """

    def scrapeStates():
        """
        Uses the beautiful soup module to scrape a list of United States 'States'

        and returns the list

        Returns:

        state - list of united states names
        
        """
        wiki_url = 'https://en.wikipedia.org/wiki/U.S._state'
        response = r.get(wiki_url)

        wiki_text_state = response.text

        soup = BeautifulSoup(wiki_text_state, 'lxml')
        print("\nRetreiving data...\n")
        state = [a.text.strip() for a in tqdm(soup.select('.div-col a'))]

        return state

    def date_rat():
        """

        Return:

        array of state date admission to the untied states
        
        """
        wiki_url = 'https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States'
        response = r.get(wiki_url)

        wiki_text_state = response.text

        soup = BeautifulSoup(wiki_text_state, 'lxml')
        print("\nRetreiving data...\n")
        span = [span.text.strip() for span in tqdm(soup.find_all('span', attrs={'style':'white-space:nowrap'}))]


        return span

    def random_num():
        """
        A separate function for random number generation.

        Returns:-

        A random number between the numbers 0 and 49.
        """
        random_number = random.randint(0, 49)

        return random_number

    def collect_rand():
        """
        Select a random number between 0 and 50 and prints out a state and date it was admitted
        to the united states

        Returns:

        state_rand - array using states_scrapeStates and states.date_rat methods
        """

        randy = states.random_num()

        df = pd.read_csv('states_and_dates.csv', sep = ',', header = 0, usecols=['states_name', 'Date of ratification'])

        state_rand = [df.iloc[randy, 0], df.iloc[randy, 1]]

        return state_rand

    def write_csv():
        df = pd.DataFrame({'states_name': states.scrapeStates(),
        'Date of ratification': states.date_rat()})

        df.head()

        df.to_csv('states_and_dates.csv')

    def read_csv():
        """
        The main read from the initial web scrapin of data.

        Returns:-

        An array based on the data now stored in a csv
        """

        df = pd.read_csv('states_and_dates.csv', index_col=0)

        return df['Date of ratification']



    def sort_dates():

        """ 
        Next advance task set for myself convert dates in numbers and reorder
        first to last to join the union

        sorted dates done but now index has to applied to states

        Returns:

        A list union joined dates according from first to last and formats and reformats the dates.
        """
        order = states.read_csv()
        order = [sub.replace(',', '') for sub in order]
        order.sort(key = lambda date: datetime.strptime(date, '%b %d %Y'))
        for i in range(len(order)): #put it back into the original format
            order[i] = order[i][0:len(order[i])-5] + ', ' + order[i][len(order[i])-4:]
        df = pd.read_csv('states_and_dates.csv', index_col=[0])
        df['Sorted_Dates'] = order
        df.head()
        df.to_csv('states_and_dates.csv', index='sort')

    def sort_states():
        """
        Sorted the state name names according to sorting of dates

        Returns:-

        An array of state name in order from earilest date to enter the union, to the last.
        """
        index = []
        count = 0
        df = pd.read_csv('states_and_dates.csv', index_col=0)
        print("\n Sorting Data...\n")
        for i in tqdm(df['Sorted_Dates']):
            for count in range(len(df['Sorted_Dates'])):
                if i == df['Date of ratification'][count]:
                    index.append(df['states_name'][count])
                    break
        return index

    def store_state():
        """
        Stores stored state names as according to states.sorted_dates() into the csv.
        """
        df = pd.read_csv('states_and_dates.csv', index_col=0)
        df['Sorted_States'] = states.sort_states()
        df.head()
        df.to_csv('states_and_dates.csv', index='sort')

    def main_rand():
        """
        The main function for a random print of a state and date of ratification.
        
        """
        states.write_csv()
        sleep(4)
        states.sort_dates()
        sleep(4)
        print(f"\nThe state of {states.collect_rand()[0]} entered the union on {states.collect_rand()[1]}.\n")

    def main_sort():
        """
        The main function used for displaying first state and last state to enter the union.
        """
        states.write_csv()
        sleep(4)
        states.sort_dates()
        sleep(4)
        states.sort_states()
        sleep(4)
        states.store_state()
        df =pd.read_csv("states_and_dates.csv ", index_col=[0])
        Name_State = df['Sorted_States']
        Dates = df['Sorted_Dates']
        print(f"\nThe first state to join union was {Name_State[0]} on {Dates[0]}, the last was {Name_State[49]} on {Dates[49]}.\n")


states.main_sort()

states.main_rand()