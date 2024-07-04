
import requests

vacDefaultUrl = 'https://api.hh.ru/vacancies'

vacancyName = input()

headers =  {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:127.0) Gecko/20100101 Firefox/127.0"
}


def getVacancies(name, salary, area, exp, time):
    params = {
        "text": name,
        "area": area,
        "salary": salary,
        "experience": exp,
        "schedule": time
    }

    vacancies = requests.get(vacDefaultUrl, headers=headers, params=params)

    return vacancies.json()