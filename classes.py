
import requests
import json


class HeadHunterApi:
    """ Класс для работы с данными через API сайта hh.ru. """

    def __init__(self, key_word):
        self.key_word = key_word

    def get_employers(self):
        """ Метод для подключения к API и получения данных с hh.ru. """

        url = 'http://api.hh.ru/employers'
        params = {'text': {self.key_word}, 'area': 113}

        dict_info = requests.get(url, params=params).json()

        return dict_info

    def write_to_json(self):
        """ Запись данных в json-файл """

        with open('data/employers.json', 'w', encoding=('utf-8')) as f:
            json.dump(self.get_employers(), f, ensure_ascii=False, indent=4)


    def choice_from_json(self):
        """  """
        other_list = []
        with open('data/employers.json', 'r', encoding=('utf-8')) as f:
            result = json.load(f)
            for item in result['items']:
                if item['open_vacancies'] > 0:
                    other_list.append(item)
            return other_list
