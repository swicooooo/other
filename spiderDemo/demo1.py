import requests,logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s: %(message)s')

# ajax exam
INDEX_URL='https://spa1.scrape.center/api/movie/?limit=10&offset={}'
DETAIL_URL='https://spa1.scrape.center/api/movie/{}/'

def scrape_index(page):
    url=INDEX_URL.format((page-1)*10)
    return scrape_api(url)

def scrape_detail(id):
    url=DETAIL_URL.format(id)
    return scrape_api(url)

def scrape_api(url):
    logging.info('scraping %s...', url)
    try:
        resp=requests.get(url)
        if resp.status_code==200:
            return resp.json()
        logging.error('get invalid status code %s while scraping %s', resp.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)

def main():
    for page in range(1, 11):
        page_data=scrape_index(page)
        for item in page_data.get('results'):
            id=item.get('id')
            detail_data=scrape_detail(id)
            logging.info('detail data %s', detail_data.get('drama'))

if __name__=='__main__':
    main()
