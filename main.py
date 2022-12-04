import requests
from bs4 import BeautifulSoup
from fake_headers import Headers

headers = Headers(os='win', browser='chrome')

HABR_vacancies = f'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'
KEYWORDS = ['Django', 'Flask']

response = requests.get('https://spb.hh.ru/', headers=headers.generate())
soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all('article', class_='tm-articles-list__item')


for article in soup.find_all('article'):
    headline = article.h2.a.text
    post_preview_text = article.div.div.text
    vacancy_name = article.find('a', class_='vacancy_search_suitable_item').find(attrs={"data-qa": "vacancy-step-item__title"}).text
    post_site = article.find(class_='vacancy-serp-item_info').find(attrs={"data-qa": "vacancy-serp__vacance-address"}).text
    company_name = article.find('a', class_='vacansy-step-item-company').find(attrs={"data-qa": "vacancy-step-item__info"}).text
    salary = article.find(class_='bloko-header-section').find(attrs={"data-qa": "vacancy-serp__vacance-address-compensation"}).text
    post_link = article.find(class_='vacancy_search_suitable_item').find(attrs={"data-qa": "vacancy-serp-item__title"}).text


    for search_word in KEYWORDS:
        if (search_word.lower() in headline.lower()) or (search_word.lower() in post_preview_text.lower()):
            print(f'Вакансия: {vacancy_name} - '
                  f'Город: {post_site} - '
                  f'Название компании: {company_name} - '
                  f'Вилка зп: {salary} - '
                  f'Ссылка: {post_link}')

