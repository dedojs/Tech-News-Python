from tech_news.database import db
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
    result_list = db.news.find().sort('category', 1)
    categories = []
    order_categories = []
    for new in result_list:
        categories.append(new['category'])

    categories_count = Counter(categories)
    categories_select = categories_count.most_common(5)
    # erro
    for category in categories_select:
        order_categories.append(category[0])

    return order_categories
