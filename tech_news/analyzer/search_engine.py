from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    result_list = search_news({'title': {'$regex': title, '$options': 'i'}})
    result = []
    for new in result_list:
        result.append((new['title'], new['url']))

    return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
