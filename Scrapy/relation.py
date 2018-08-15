import requests
import time
import json

from urllib.parse import urlencode
from tree import Tree, Node

base_url = 'https://work.nsfocus.com/community/webajax/ucenter_ajax/'
superior = 'getDirectLeader?'
subordinate = 'getSubordinate?'

def set_header(uid):
    refer = 'https://work.nsfocus.com/community/users/' + uid
    headers = {
        'Host': 'work.nsfocus.com',
        'Referer': refer,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': 'i8community=s%3AeS-lbQHJyTWF7Hu4uEXZh1i9o91O5Fux.4Asqy2hm4cGwkAI56wwr8FfvDY61AUONju0JCQrn2xc; d=work; u=MwBmADAANgA4ADkAZgA0AC0AYgAwADMAOAAtADQAYwA0ADgALQA4ADIANQBjAC0AYgAzADQANwA4ADkAMwBiAGEAYwBmADIAfAAyADAAMQA4ADAAOAAxADQAMAA5ADMANgAwADAAfAAzAGUAZAA1AGQAMQBmADMALQBhADgAMAAwAC0ANABhADgAOAAtADgAMQA4ADMALQBjAGMANgA5ADUAMQA1AGMANQBlAGYAMgB8ADgAMgA4AGMANQAwADEAZQAwADgAMQAxAGQAMABhADYANgBlADcAYQA5AGQAYgBiAGYAMQBhAGUAYgBlADkANAA=',
        'Connection': 'keep-alive',
    }
    return headers

def get_page(uid):
    params = {'uid':uid}
    url1 = base_url + superior + urlencode(params)
    url2 = base_url + subordinate + urlencode(params)
    try:
        response_subordinate = requests.get(url2, headers=set_header(uid))
        if response_subordinate.status_code == 200:
            return {'subordinate': response_subordinate.json()}
    except requests.ConnectionError as e:
        print ('Error', e.args)


def parse_page(jsons={}):
    data = jsons['subordinate'].get('List')
    lists = []
    for items in data:
        item = {
            'id': items.get('PassportID'),
            'name': items.get('Name'),
            'inter': items.get('NamePinyin'),
            'sex': items.get('Gender'),
            'birthday': items.get('Birthday'),
            'JoinTime': items.get('JoinTime'),
            'MPhone': items.get('MPhone'),
            'OrgName': items.get('OrgName'),
            'Position': items.get('Position'),
            'Tel': items.get('Tel'),
            'City': items.get('City'),
            'Email': items.get('Email'),
            'WorkPlaceName': items.get('WorkPlaceName'),
        }
        lists.append(item)
    return lists


T = Tree()
stack_list = []
node = Node({'name': '沈'})
T.append(node, 'admin')
XML = get_page('afbbd9ea-7568-4cbb-ad7d-a49acc5dd3a7')
result = parse_page(XML)
for i in result:
    i['superior'] = node.name
    i['subordinate'] = []
    data = Node(i)
    stack_list.append(data)
    T.append(data, node.name)

try:
    while len(stack_list) > 0:
        print(len(stack_list))
        note = stack_list[0]
        XML = get_page(note.id)
        result = parse_page(XML)
        lists = []
        with open('data.json', 'w', encoding='utf-8') as file:
            for i in result:
                i['superior'] = note.name
                i['subordinate'] = []
                print(i)
                file.write(json.dumps(i, ensure_ascii=False))
                data = Node(i)
                lists.append(data)
        note.subordinate.extend(lists)
        stack_list.extend(lists)
        stack_list.pop(0)
        time.sleep(0.5)
except Exception as e:
    print ('Error', e.args)
finally:
    T.save()