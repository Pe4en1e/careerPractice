
import requests
import json

vacDefaultUrl = 'https://api.hh.ru/vacancies'

headers =  {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:127.0) Gecko/20100101 Firefox/127.0"
}


def getVacancies(name):
    params = {
        "text": name
    }

    vacancies = requests.get(vacDefaultUrl, headers=headers, params=params)

    vacancies = vacancies.json()

    items = vacancies['items']

    vacancies = []

    for item in items:
        if item['salary'] == None:
            salary = "Не указано"
        else:
            salary = "От " + str(item['salary']['from']) + " " + str(item['salary']['currency'])

        requirement = str(item['snippet']['requirement'])

        if "highlighttext" in requirement:
            requirement = requirement.replace("<highlighttext>", "")
            requirement = requirement.replace("</highlighttext>", "")

        vacancy = {
            "name": item['name'],
            "area": item['area']['name'],
            "salary": salary,
            "url": item['alternate_url'],
            "requirement": requirement
        }

        vacancies.append(vacancy)

    return vacancies


