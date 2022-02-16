from ..database import search_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    # https://stackoverflow.com/questions/7101703/how-do-i-make-case-insensitive-queries-on-mongodb/36916270#36916270
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    new_list = [(new["title"], new["url"]) for new in news]
    return new_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
