"""
Author: Cody Swindells

Testing ground while I was learning build upon the use of beautiful soup.


"""


from bs4 import BeautifulSoup
import requests as r

wiki_url = 'https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States'
response = r.get(wiki_url)
#table_id = 

wiki_text_state = response.text

soup = BeautifulSoup(wiki_text_state, 'lxml')

span = [span.text.strip() for span in soup.find_all('span', attrs={'style':'white-space:nowrap'})]


print(span)