from bs4 import BeautifulSoup
import requests
from time import sleep
from csv import writer, reader
from random import randint, sample, shuffle
from datetime import datetime

BASE_URL = 'https://quotes.toscrape.com'


def update_quotes():
    next_page_url = '/page/1/'
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
            print('Updating...')
            sleep(1)

def open_csv():
    with open('quotes.csv') as file:
        return list(reader(file))
        


used_quotes = []
def chose_quote(quotes):
    while True:
        pick = randint(0, len(quotes))
        if pick not in used_quotes:
            used_quotes.append(pick)
            return pick

def replace1(text, author):
    first, last = author.split()
    return text.replace(first, '******').replace(last, '******')

score = {'won':0, 'lost':0}
def game():
    quotes = open_csv()
    index = chose_quote(quotes)
    authors_set = set([i[1] for i in quotes])
    quote_author = quotes[index][1]
    authors_set_temp = authors_set
    authors_set_temp.remove(quote_author)
    options_list = sample(list(authors_set_temp), k = 5)
    options_list.append(quote_author)
    shuffle(options_list)

    print(quotes[index][0])
    for n, i in enumerate(options_list, start=1):
        print(f'{n}. {i}')
    
    remaining_guesses = 2
    while True:
        shot = input('Who is author of the listed quote? Choose a number: ')
        if shot not in ('1','2','3','4','5','6'): 
            print('You can only chose number 1-6') 
            continue
        if quote_author == options_list[int(shot)-1]:
            print('You won! Congratulations!')
            score['won'] +=1
            break

        elif remaining_guesses == 2:
            remaining_guesses -= 1 
            print('That is not correct answer, try again, here is hint: ')
            response = requests.get(BASE_URL + quotes[index][2])
            soup = BeautifulSoup(response.text, 'html.parser')
            birthdate = soup.find(class_='author-born-date').get_text()
            birth_loc = soup.find(class_='author-born-location').get_text()
            print(f'Born: {birthdate} {birth_loc}')
        elif remaining_guesses == 1:
            remaining_guesses -= 1 
            print('You have last chance, here is another hint:')
            author_description = soup.find(class_='author-description').get_text()
            print(replace1(author_description, quote_author))
        else:
            print('Unfortunately you did not guess, you are loosing this game...')
            score['lost'] +=1
            break
    print(f'You won {score["won"]} times and {score["lost"]} times lost')
    again = input('Would you like play again? y/n: ')
    if again == 'y': return game ()
    else: print('Thank you for game, see you latter')

if datetime.now().weekday() == 0:
    update_quotes()

game()

