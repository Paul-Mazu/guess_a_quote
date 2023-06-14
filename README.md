# <center>Quotes Game Application</center>

<div align="center">

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/Paul-Mazu/guess_a_quote?color=1d7147&style=for-the-badge) ![GitHub language count](https://img.shields.io/github/languages/count/Paul-Mazu/guess_a_quote?color=62B096&style=for-the-badge)
</div>

<div align="center">
  <a href="#about">About</a>  |
  <a href="#key-features">Key Features</a>  |
  <a href="#dependencies">Dependencies</a>  |
  <a href="#setup">Setup</a>  |
  <a href="#authors">Authors</a>
</div>

<br>

# About

This Python application is a simple game that tests your knowledge of quotes and their authors.  
The application scrapes quotes from a website and presents them to the user in a multiple-choice format.  
The user needs to guess the correct author of the displayed quote.

Incorporated skillset: 
* fundamental programming concepts
* file handling  
* data manipulation 
* algorithmic thinking 
* time management 
* modularization

<br>

## Key Features

* The application uses the BeautifulSoup library to scrape quotes from a website.
* It saves the scraped quotes in a CSV file named "quotes.csv".
* The application randomly selects a quote and presents it to the user with multiple options for the author.
* The user can make a guess by choosing a number corresponding to the author's position in the options list.
* The application provides hints if the user fails to guess correctly within a certain number of attempts.
* The user's score is tracked, counting the number of wins and losses.
* The application allows the user to play multiple rounds and displays the overall score.


## Dependencies

The application requires the following Python libraries:  

* BeautifulSoup: Used for scraping the website and parsing HTML content.
* requests: Used to send HTTP requests and retrieve website content.
* csv: Used for reading from and writing to CSV files.
* random: Used for generating random numbers and shuffling lists.
* datetime: Used to check the current day of the week.

Please ensure that you have these libraries installed before running the application.  

## Setup
Clone repository: `git clone git@github.com:Paul-Mazu/guess_a_quote.git`

Import the necessary libraries:  

```
from bs4 import BeautifulSoup  
import requests  
from time import sleep  
from csv import writer, reader  
from random import randint, sample, shuffle  
from datetime import datetime 
```


## Authors

Pawel Mazurkiewicz:  
Tutor and Student of Digital Career Institute  
[My WWW](https://paul-mazu.github.io/portfolio/)  
[LinkedIn](https://www.linkedin.com/in/pawel-mazurkiewicz-906877173/)  
