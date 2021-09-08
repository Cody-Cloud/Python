import os #Best practice so it can be run on different systems
from selenium import webdriver
#import pandas as pd
#import requests as rq
#from bs4 import BeautifulSoup as soup

os.environ["PATH"] += os.pathsep + r"C:/webdrivers/" #won't work without os.pathsep
#PATH = "C:\webdrivers\chromedriver.exe"
driver = webdriver.Chrome()

driver.get("http://www.google.com")
driver.find_element_by_css_selector("input.titlesearch>")
