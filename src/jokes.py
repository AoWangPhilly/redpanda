'''
description: webscrapes for math jokes and memes
author: ao wang
date: 08/30/2020
'''

import requests
from bs4 import BeautifulSoup
import re
import json


def scrapeJokes():
    '''Webscrapes jobs from thoughtcatalog and saves the question/answer jokes into JSON file'''

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
    a = a[a.index('Because she’ll go on and on and on forever.')
                  :a.index('It was a ‘mean’ thing to say! ')+1]

    qna = {i: j for i, j in zip(q, a)}

    with open('src/cogs/jokes.json', 'w') as joke_file:
        json.dump(qna, joke_file)


def scrapeMemes(URL='https://www.memedroid.com/memes/tag/math'):
    '''Retrieves meme images from memedroid

    Parameter
    =========
        URL (str): the url for math memes, can also loop through various pages

    Return
    ======
        list (str): list of the meme img src links 
    '''
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return [img['src'] for img in soup.findAll('img') if 'https://images3.memedroid.com/images/' in img['src']]


if __name__ == '__main__':
    listOfMemes = scrapeMemes()
    NUM_PAGE_MEMES = 9

    for i in range(2, NUM_PAGE_MEMES):
        listOfMemes.extend(scrapeMemes(
            'https://www.memedroid.com/memes/tag/math/{}'.format(i)))

    with open('src/cogs/memes.txt', 'w') as memes:
        for src in listOfMemes:
            memes.write('{}\n'.format(src))
