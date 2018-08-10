from urllib.parse import urlencode
from pyquery import PyQuery as pq

import requests
import pickle
import json

base_url = 'http://m.weibo.cn/api/container/getIndex?'

headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

def get_page(page):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print ('Error', e.args)

def parse_page(json):
    if jsons:
        items = jsons.get('data').get('cards')
        for item in items:
            #print(item)
            item = item.get('mblog')
            if item:
                weibo = {}
                weibo['id'] = item.get('id')
                weibo['text'] = pq(item.get('text')).text()
                weibo['attitudes'] = item.get('attitudes_count')
                weibo['comments'] = item.get('comments_count')
                weibo['reposts'] = item.get('reposts_count')
                yield weibo

if __name__ == '__main__':
    for page in range(1,3):
        jsons = get_page(page)
        results = parse_page(jsons)
        with open('data.json', 'a+', encoding='utf-8') as file:
            for result in results:
                file.write(json.dumps(result, indent=2, ensure_ascii=False))
                print(result)

