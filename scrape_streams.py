import requests
import re
from bs4 import BeautifulSoup

class ScrapeStreams:
    @staticmethod
    def scrape_streameast():
        url = 'https://www.thestreameast.to/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'        
        }
        response = requests.get(url + 'v2/', headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        ul_element = soup.find('ul', {'id': 'CanliMaclar'})

        streams = []
        if ul_element:
            list_items = ul_element.find_all('li')
            for li in list_items:
                pattern = r'^[A-Z]+\n\n\n'
                name = li.text.strip()

                league = name.split('\n')[0]

                name = re.sub(pattern, '', name)
                name = name.split('\n')[0]

                a_tag = li.find('a')
                if a_tag and 'href' in a_tag.attrs:
                    href_value = a_tag['href']

                stream_info = {'name': name, 'league': league, 'url': url + href_value}
                print(stream_info)

                streams.append(stream_info)

        return streams


    def scrape_crackstreams():
        url = 'https://crackstreams.biz/'
        subcategories = ['nhlstreams', 'nflstreams', 'cfbstreams']

        streams = []

        return streams
