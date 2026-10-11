import requests
from bs4 import BeautifulSoup
from .models import Company, News

def scrape_merolagani_news():
    url = "https://merolagani.com/NewsList.aspx"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.content, 'html.parser')
        news_items = soup.find_all('div', class_='media-body')
        
        for item in news_items[:5]:
            a_tag = item.find('a')
            if a_tag:
                title = a_tag.text.strip()
                link = "https://merolagani.com" + a_tag['href']
                
                # Simple categorization hack: Keyword matching
                company = None
                for c in Company.objects.all():
                    if c.symbol in title or c.name in title:
                        company = c
                        break
                        
                News.objects.get_or_create(
                    url=link,
                    defaults={
                        'title': title,
                        'body': title,
                        'source': 'MeroLagani',
                        'company': company
                    }
                )
    except Exception as e:
        print(f"Scraping error: {e}")