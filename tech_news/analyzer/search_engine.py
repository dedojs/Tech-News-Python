from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    result_list = search_news({'title': {'$regex': title, '$options': 'i'}})
    result = []
    for new in result_list:
        result.append((new['title'], new['url']))

    return result


# Requisito 7
def search_by_date(date):
    result = []
    try:
        date_list = date.split('-')
        new_datetime = datetime(
            int(date_list[0]), int(date_list[1]), int(date_list[2])
        )

        format_date = new_datetime.strftime("%d/%m/%Y")

        result_list = search_news({'timestamp': format_date})

        for new in result_list:
            result.append((new['title'], new['url']))

    except ValueError:
        raise ValueError('Data inválida')

    return result


# Requisito 8
def search_by_tag(tag):
    result_list = search_news({'tags': {'$regex': tag, '$options': 'i'}})
    result = []
    for new in result_list:
        result.append((new['title'], new['url']))

    return result


# Requisito 9
def search_by_category(category):
    result_list = search_news(
        {'category': {'$regex': category, '$options': 'i'}}
    )
    result = []
    for new in result_list:
        result.append((new['title'], new['url']))

    return result
