import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    URL = 'http://www.jokes4us.com/miscellaneousjokes/mathjokes/calculusjokes.html'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find('p')
    print(results)