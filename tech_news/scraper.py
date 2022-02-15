# Requisito 1
import requests
import time
import parsel
from bs4 import BeautifulSoup


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
    next_page = selector.css("div.tec--list > a.tec--btn::attr(href)").get()
    if not next_page:
        return None
    return next_page


# Requisito 4
def get_url(html_content):
    selector = parsel.Selector(html_content)
    url = selector.css("head link[rel=canonical]::attr(href)").get()
    return url


def get_title(html_content):
    selector = parsel.Selector(html_content)
    title = selector.css("h1.tec--article__header__title::text").get()
    return title


def get_time(html_content):
    selector = parsel.Selector(html_content)
    timestamp = selector.css(
        "div.tec--timestamp__item time::attr(datetime)"
    ).get()
    return timestamp


def get_writer(html_content):
    selector = parsel.Selector(html_content)
    author = selector.css(
        "div.tec--author__info a.tec--author__info__link::text"
    ).get()
    if not author:
        writer = selector.css(
            "div.tec--timestamp__item.z--font-bold a::text"
        ).get()
        if not writer:
            new_writer = selector.css(
                "#js-author-bar > div >"
                "p.z--m-none.z--truncate.z--font-bold::text"
            ).get()
            return new_writer
        return writer.strip()
    return author.strip()


def get_shares_count(html_content):
    selector = parsel.Selector(html_content)
    shares_count = selector.css("div.tec--toolbar__item::text").get()
    refatored_shares_count = ""
    if shares_count:
        refatored_shares_count = shares_count.replace(" Compartilharam", "")
    if not refatored_shares_count:
        return 0
    return int(refatored_shares_count)


def get_comments_count(html_content):
    selector = parsel.Selector(html_content)
    comments_count = selector.css(
        "button#js-comments-btn::attr(data-count)"
    ).get()
    if not comments_count:
        return 0
    return int(comments_count)


def get_summary(html_content):
    selector = parsel.Selector(html_content)
    # https://pt.stackoverflow.com/questions/192176/como-remover-tags-em-um-texto-em-python
    summary = BeautifulSoup(
        selector.css("div.tec--article__body > p").getall()[0], "html.parser"
    ).get_text()
    return summary


def get_source(html_content):
    selector = parsel.Selector(html_content)
    sources = selector.css(
        "div.tec--article__body-grid div.z--mb-16 a.tec--badge::text"
    ).getall()
    format_source = []
    for source in sources:
        format_source.append(source.strip())
    return format_source


def get_categories(html_content):
    selector = parsel.Selector(html_content)
    categories = selector.css(
        "#js-categories a.tec--badge.tec--badge--primary::text"
    ).getall()
    format_categories = []
    for cat in categories:
        format_categories.append(cat.strip())
    return format_categories


def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    dict_news = {
        "url": get_url(html_content),
        "title": get_title(html_content),
        "timestamp": get_time(html_content),
        "writer": get_writer(html_content),
        "shares_count": get_shares_count(html_content),
        "comments_count": get_comments_count(html_content),
        "summary": get_summary(html_content),
        "sources": get_source(html_content),
        "categories": get_categories(html_content),
    }
    return dict_news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
