from requests import get
from bs4 import BeautifulSoup

base_url = 'https://weworkremotely.com/remote-jobs/search?=%E2%9C%93&term='
search_term = 'python'

response = get(f'{base_url}{search_term}')

if response.status_code != 200:
  print('에러가 발생했습니다.')
else:
  soup = BeautifulSoup(response.text,'html.parser')
  print(soup.find_all('title'))