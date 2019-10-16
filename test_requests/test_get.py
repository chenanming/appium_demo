import requests



def test_get_login(self):
    url = "https://testerhome.com/api/v3/topics.json"
    params = {'limit': 2}
    r = requests.get(url, params=params).json()
    assert r['topics'][0]['user']['name'] == "mengzh"

def test_xueqiu_search(self):
    url = "https://xueqiu.com/stock/search.json"
    params = {'code': 'sogo'}
    r = requests.get(url, params=params)
    print(r.text)