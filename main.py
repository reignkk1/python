
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"

options = Options()
options.add_experimental_option("detach",True)

browser = webdriver.Chrome(options=options)


browser.get(f"{base_url}{search_term}")



  
      
