"""
This will a project that will employ the use selenium and beautiful soup in order to build
a bot that can be ask any question and answer it.

Planning stage

Web driver: Chrome

Author: Cody Swindells

Created: 01/09/21

Modified: 02/09/21

"""

import os #Best practice so it can be run on different systems
from selenium import webdriver
import pandas as pd
import requests as r
from bs4 import BeautifulSoup as soup

os.environ["PATH"] += os.pathsep + r"C:/webdrivers/" #won't work without os.pathsep
driver = webdriver.Chrome()


class askme:
    """
    Main class containing methods related to askme bot
    """
    def ask():

        """
        
        """
        question = input("Ask me anything!")

        google = "http://www.google.com"

        request = r

        driver.get("http://www.google.com")
        driver.find_element_by_tag_name('<input')


