import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.imdb.com/chart/tvmeter/?ref_=chttp_ql_5"

#Header for request
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36','referer':'https://www.google.com/','Accept-Language':'en-US, en;q=0.5' }

#request
site = requests.get(url, headers=headers)

soup = BeautifulSoup(site.content, 'html.parser')

shows=soup.find_all("li",attrs= {'class': 'ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent'})
print(len(shows))

csv_file='popular_shows.csv'

with open(csv_file, mode='w',newline='',encoding='utf-8-sig') as file:
 writer=csv.writer(file)

 header=['Name', 'Year', 'Rating']
 writer.writerow(header)

 for show in shows:
  name=show.find('div',class_='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN cli-title').a.text
  year = show.find('div', class_='sc-b189961a-7 feoqjK cli-title-metadata').span.text
  rating = show.find('div',class_='sc-e2dbc1a3-0 ajrIH sc-b189961a-2 fkPBP cli-ratings-container').span.text


  writer.writerow([name, year, rating ])

print("Data has been written to the CSV file:", csv_file)
