from tech_news.database import db, find_news
from collections import Counter


# Requisito 10
def top_5_news():
    result_order = db.news.find().sort('comments_count', -1)
    result = []
    for new in result_order:
        result.append((new['title'], new['url']))

    return result[:5]


# Requisito 11
def top_5_categories():
    result_list = find_news()
    categories = []
    result = []
    order_cat = []
    for new in result_list:
        categories.append(new['category'])

    resp = Counter(categories)
    result = resp.most_common(5)
    for category in result:
        order_cat.append(category[0])

    return order_cat
