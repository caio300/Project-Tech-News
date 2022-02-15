# Requisito 1
import requests
import time
import parsel


def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
    except requests.ReadTimeout:
        return None
    else:
        if response.status_code != 200:
            return None
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(html_content)
    links_news = selector.css(
        "div.tec--list__item a.tec--card__title__link::attr(href)"
    ).getall()

    return links_news


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(html_content)
    next_page = selector.css(
        "div.tec--list > a.tec--btn::attr(href)"
    ).get()
    if not next_page:
        return None
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
