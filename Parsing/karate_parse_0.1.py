import collections
import re
import requests
import sys
from lxml import html


class KarateSushiScrape:
    def __init__(self, url):
        self.url = url

    def get_menu_categories(self):
        response = requests.get(self.url).content
        tree = html.fromstring(response)
        data = tree.xpath(
            '/html/body/div[@class="main wrapper"]'
            '/div[@class="container-fluid"]'
            '/div[@class="row category-list"]/div')
        return data

    def __get_categories_links(self):
        categories_dict = collections.deque()
        categories = self.get_menu_categories()
        for category in categories:
            categories_dict.append(
                {'name': category.xpath('a/h3')[0].text,
                 'link': category.xpath('a')[0].get('href')}
            )
        return categories_dict

    def show_categories(self):
        for category in self.__get_categories_links():
            print(category['name'])

    def choose_category(self):
        category = str(input(
            'Введите название категории, чтобы выбрать блюдо меню.\n'
            'Нажмите "Enter" для просмотра категорий.\n'
            'Ввеидте "выход", чтобы выйти из программы.\n'
        )).lower()
        category_names = collections.deque(
            [name['name'] for name in self.__get_categories_links()])
        if category == '':
            self.show_categories()
            self.choose_category()
        elif category.capitalize() in category_names:
            link = [
                name['link'] for name in self.__get_categories_links()
                if category == name['name'].lower()
            ][0]
            print(link)
            menu = self.get_menu(self.get_category(link), category)
            self.print_menu(menu, category)
        elif category == 'выход':
            sys.exit('До свилания! Заходите ещё!')
        else:
            print('Нет такой категориию Попробуйте ещё раз.')
            self.choose_category()

    @staticmethod
    def get_category(url):
        response = requests.get(url).content
        tree = html.fromstring(response)
        data = tree.xpath(
            '/html/body/div[@class="main wrapper"]'
            '/div[@class="container-fluid"]/div[@class="category-items"]/div')
        return data

    def get_menu(self, category_data, category):
        menu_data = collections.deque()
        for menu in category_data:
            menu_data.append(
                {'name': menu.xpath('div')[0].get('data-ss-cart-name'),
                 'composition': self.get_menu_info(menu, category),
                 'price': menu.xpath('div')[0].get('data-ss-cart-price'),
                 'weight': menu.xpath('div')[0].get('data-ss-cart-size'),
                 'link': menu.xpath('div')[0].get('data-ss-cart-url')}
            )
        return menu_data

    @staticmethod
    def get_menu_info(menu, category):
        if category == 'сеты':
            dishes_data = menu.xpath('div/div/div[1]/p')
            dishes = collections.deque()
            for dish in dishes_data:
                dishes.append(
                    {'name': dish.xpath('b')[0].text,
                     'composition': dish.xpath('span')[0].text}
                )
        elif category == 'лапша и плов':
            dishes = collections.deque()
        else:
            dishes_data = menu.xpath('div/div/div')[0].text
            dishes = re.findall('\t{7}(.+)\n', dishes_data)[0]
        return dishes

    @staticmethod
    def print_menu(menu, category):
        print(menu)
        for dish in menu:
            print('Название: {}'.format(dish['name']))
            print('Вес: {}'.format(dish['weight']))
            if category == 'сеты':
                print('Состав сета:')
                for composition in dish['composition']:
                    print('\n\tНазвание блюда: {}'.format(composition['name']))
                    print('\tСостав блюда: {}\n'.format(composition['composition']))
            elif category == 'лапша и плов':
                pass
            else:
                print('Состав блюда: {}'.format(dish['composition']))
            print('Цена: {} рублей'.format(dish['price']))
            print('Ссылка на блюдо: {}\n'.format(dish['link']))


KarateSushiScrape('https://sushi-karate.ru/menu').choose_category()
