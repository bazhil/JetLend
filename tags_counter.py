from bs4 import BeautifulSoup
import requests

link = 'https://jetlend.ru/'


def tags_counter(link):
    """
    Простейший парсер, который подсчитывает количество тегов
    :param link: ссылка на сайт
    :return: dict
    """
    html = requests.get(link)
    soup = BeautifulSoup(html.text, 'lxml')
    body = soup.find_all()
    tags = [tag.name for tag in body]
    unique_tags = list(set(tags))
    tags_with_attrs = [tag for tag in body if len(tag.attrs) > 0]

    result = {
        'tags': len(tags),
        'unique_tags': len(unique_tags),
        'tags_with_attrs': len(tags_with_attrs)
    }

    return result


if __name__ == '__main__':
    print(tags_counter(link))


