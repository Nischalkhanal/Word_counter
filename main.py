import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    print("Start function called")
    word_list = []
    headers = {'User-Agent':''}
    source_code = requests.get(url, headers=headers)
    #source_code.raise_for_status()  # Check for request errors
    plain_text = source_code.content  # Use .content for binary content like HTML
    soup = BeautifulSoup(plain_text, 'html.parser')
    for post_text in soup.findAll('div', {'class': 'b-info__title'}):
        content = post_text.get_text()
        words = content.lower().split()
        for each_word in words:
            print(each_word)
            word_list.append(each_word)
    clean_list(word_list)

def clean_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "~!@#$%^&*()_+=,_-./;'[]{}:|\"\<>?"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            clean_word_list.append(word)
    create_dictionary(clean_word_list)

def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] +=1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)




start('https://www.ebay.com.au/b/Electronics/bn_7000259947')
