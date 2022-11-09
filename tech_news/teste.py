 db_result = find_news()

    result = []
    for new in db.news.find({'title': 'Algoritmos'}):
        result.append(new)
    return result
