"""
File: webcrawler.py
Name: Chen, Wei Ting
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names' + year + '.html'

        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #
        tags = soup.find_all('table', {'class': 't-stripe'})

        male = 0
        female = 0
        for tag in tags:
            a = tag.tbody.text.split()

            # pop 22 irrelevant items
            for i in range(22):
                a.pop(-1)

            # calculate the total number of male
            for i in range(2, len(a), 5):
                result = int(a[i].replace(",", ""))  # remove comma
                male += result

            # calculate the total number of female
            for i in range(4, len(a), 5):
                result = int(a[i].replace(",", ""))  # remove comma
                female += result
            print('Male Number: ' + str(male))
            print('Female Number: ' + str(female))


if __name__ == '__main__':
    main()
