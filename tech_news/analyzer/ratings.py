from tech_news.database import db


# Requisito 10
def top_5_news():
    result_order = db.news.find().sort('comments_count', -1)
    result = []
    for new in result_order:
        result.append((new['title'], new['url']))

    return result[:5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
