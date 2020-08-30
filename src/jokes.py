import requests
from bs4 import BeautifulSoup
import re
import json

if __name__ == '__main__':
    URL = 'https://thoughtcatalog.com/january-nelson/2018/04/39-math-jokes-and-puns-that-will-make-you-smile-easy-as-pi/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Getting the questions
    r = re.compile('^[1-9]+.')
    q = [h4.get_text() for h4 in soup.findAll('h4')]
    q = list(filter(r.match, q))
    q = [word[word.find('.')+2:] for word in q]

    # Getting answers
    a = [p.get_text() for p in soup.findAll('p')]
    a = [p for p in a if p]
    a = a[a.index('Because she’ll go on and on and on forever.'):a.index('It was a ‘mean’ thing to say! ')+1]

    qna = {i: j for i, j in zip(q, a)}

    with open('jokes.json', 'w') as joke_file:
        json.dump(qna, joke_file)
