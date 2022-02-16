from ..database import search_news
from datetime import datetime


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
    try:
        datetime.strptime(date, "%Y-%m-%d")
        print(date)
        news = search_news({"timestamp": {"$regex": date}})
        news_list = [(new["title"], new["url"]) for new in news]
        return news_list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    news = search_news({"sources": {"$regex": source, "$options": "i"}})
    news_list = [(new["title"], new["url"]) for new in news]
    return news_list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
