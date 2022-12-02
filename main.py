from bs4 import BeautifulSoup
import requests
from time import sleep
from csv import writer, reader
from random import randint, sample, shuffle
from datetime import datetime

BASE_URL = 'https://quotes.toscrape.com'
next_page_url = '/page/1/'

def update_quotes():

    with open('quotes.csv','w') as file:
        write = writer(file)
        write.writerow(['quote', 'author', 'link'])
        while next_page_url:
            response = requests.get(BASE_URL + next_page_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            quotes = soup.find_all(class_='quote')

            for i in quotes:
                quote = i.find(class_='text').get_text()
                author = i.find(class_='author').get_text()
                link_to_author = i.find('a')['href']
                write.writerow([quote, author, link_to_author])
            next_page = soup.find(class_='next')
            next_page_url = next_page.find('a')['href'] if next_page else None
            sleep(1)

with open('quotes.csv') as file:
    read = list(reader(file))
    authors_set = set([i[1] for i in read])


used_quotes = []
def chose_quote():
    while True:
        pick = randint(0, len(read))
        if pick not in used_quotes:
            used_quotes.append(pick)
            return pick

def game():
    index = chose_quote()
    quote_author = read[index][1]
    authors_set_temp =authors_set
    authors_set_temp.remove(quote_author)
    options_list = sample(authors_set_temp,k = 5)
    options_list.append(quote_author)
    shuffle(options_list)

    print(read[index][0])
    for n, i in enumerate(options_list, start=1):
        print(f'{n}. {i}')
    
    remaining_guesses = 3
    while remaining_guesses > 0:
        shot = int(input('Who is author of the listed quote?: '))
        if quote_author == options_list[shot-1]:

            print('You won! Congratulations!')
            break
        elif remaining_guesses == 3:
            remaining_guesses -= 1 
            print('Try again, here is hint: ')
            response = requests.get(BASE_URL + read[index][2])
            soup = BeautifulSoup(response.text, 'html.parser')
            birthdate = soup.find(class_='author-born-date').get_text()
            birth_loc = soup.find(class_='author-born-location').get_text()
            print(f'Born: {birthdate} {birth_loc}')
        elif remaining_guesses == 2:
            remaining_guesses -= 1 
            author_description = soup.find(class_='author-description').get_text()
            print(author_description)

if datetime.now() == datetime.weekday(0):
    update_quotes()

game()

