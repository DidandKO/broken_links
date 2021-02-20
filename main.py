import requests

# На вход программы подается массив ссылок, которые надо проверить
urls = ['https://vk.com/meh1243', 'https://vk.com/bidlo_intelligent', 'https://yandex.ru/',
        'https:/yandex.ru/', 'yandex.ru/', 'https://yandex']


# Основной метод выявления ссылок, которые ведут на несуществующую страницу ресурса.
def check_link(link):
    try:
        request_info = requests.get(link)
        print(request_info.status_code)
        if 400 <= request_info.status_code < 500:
            print('Мертвая ссылка')
            return False
        elif 200 <= request_info.status_code < 300:
            print('Подключение успешно')
            return True
        elif 300 <= request_info.status_code < 400:
            print('Перенаправление')
            return False
        elif 500 <= request_info.status_code < 600:
            print('Серверная ошибка')
            return False
        else:
            print('Неизвестный код')
    except Exception as e:
        print(e.__class__)


for url in urls:
    check_link(url)
