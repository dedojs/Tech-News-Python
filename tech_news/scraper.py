import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, headers={"user-agent": "Fake user-agent"},
                                timeout=3)
        # selector = Selector(text=response.text)
        time.sleep(1)
        if (response.status_code == 200):
            return response.text
        elif (response.status_code != '200'):
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    news_link = selector.css('div.cs-overlay a::attr(href)').getall()
    return news_link


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    new_page = selector.css('a.next.page-numbers::attr(href)').get()
    return new_page


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)

    noticia = {
        'url': selector.css("link[rel='canonical']::attr(href)").get(),
        'title': selector.css('h1.entry-title::text').get().rstrip(),
        'timestamp': selector.css('li.meta-date::text').get(),
        'writer': selector.css('a.url.fn.n::text').get(),
        'comments_count': len(selector.css(".comment-list li").getall()) or 0,
        'summary': selector.xpath("string(//p)").get().rstrip(),
        'tags': selector.css(".post-tags a::text").getall(),
        'category': selector.css('span.label::text').get(),
    }

    return noticia


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
