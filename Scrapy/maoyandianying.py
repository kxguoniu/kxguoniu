import requests

def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'

    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return none

def main():
    url = 'http://maoyan.com/board/4'
    html = get_one_page(url)
    print(html)

main()