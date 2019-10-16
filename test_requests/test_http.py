import json
import jsonpath
import requests
import pytest
from requests import Response
from jsonschema import validate


class TestHttp:
    def setup(self):
        self.proxies = None
        #self.proxies = {'http':'http://127.0.0.1:8080/'}

    def test_get(self):
        r = requests.get('https://testerhome.com/topics/20829').json()
        print(r)

    def test_get_query(self):
        url = "http://47.95.238.18:8090/get"
        paloy = {'key01':'value01', 'key02':{"value02", "vulue03"}}
        r = requests.get(url, params=paloy)
        self.inspect_response(r)

    def test_get_query_headers(self):
        url = "http://47.95.238.18:8090/get"
        paloy = {'key01' : 'value01', 'key02': {"value02", "vulue03"}}
        headers = {'a':'2', 'bcd':'header demo', 'Content-Type': 'application/json'}
        r = requests.get(url, params=paloy, headers=headers)
        self.inspect_response(r)

    def test_post(self):
        url = "http://47.95.238.18:8090/post"
        payload = {'key01': 'value01', 'key02': {"value02", "vulue03"}}
        headers = {'a': '2', 'bcd': 'header demo', 'accept': 'application/json'}
        r = requests.post(url, data=payload, headers=headers, proxies=self.proxies)
        self.inspect_response(r)

    def test_testhome(self):
        url = "https://testerhome.com/api/v3/topics.json"
        r = requests.get(url, params={'limit': '2'}, proxies=self.proxies)
        print(r.json())
        assert r.json()['topics'][0]['id'] == 20849

    def test_get_login(self):
        url = "https://testerhome.com/api/v3/topics.json"
        params = {'limit': 2}
        data = requests.get(url, params=params).json()
        print(data)
        assert data['topics'][0]['user']['login'] == "turinblueice"

    def test_get_login_jasnpath(self):
        url = "https://testerhome.com/api/v3/topics.json"
        params = {'limit': 2}
        data = requests.get(url, params=params)
        print(data.json())
        print(jsonpath.jsonpath(data.json(), "$..user"))
        print(jsonpath.jsonpath(data.json(), "$..user..login"))
        assert jsonpath.jsonpath(data.json(), "$.topics[?(@.user.login == 'SabrinaZhou007')].user.id")[0] == '47270'

    def test_get_login_schema(self):
        url = "https://testerhome.com/api/v3/topics.json"
        params = {'limit': 2}
        data = requests.get(url, params=params)
        schema = json.load(open("topics_schema.json"))
        validate(data, schema=schema)


    def test_xueqiu_search(self):
        url = "https://xueqiu.com/stock/search.json"
        params = {'code': 'sogo'}
        headers = {
            #"accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            #"Cookie": "aliyungf_tc=AQAAAKngz1KaNw4ABbvFcyfxfzVw5TVj; acw_tc=2760829b15711074239423186e998a0cbb959e3df712c81ecc4e6e5458d7de; s=c411z8udyg; xq_a_token=d831cd39b53563679545656fba1f4efd8e48faa0; xq_r_token=fd2f0f487c8298cad8e7519f1560abb7a18c589d; u=231571107324553; device_id=56506e653b88416904d843dbbc43bcfc; Hm_lvt_1db88642e346389874251b5a1eded6e3=1571107325,1571132965; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1571132970"
        }
        cookies = {
            #'aliyungf_tc': 'AQAAAKngz1KaNw4ABbvFcyfxfzVw5TVj',
            #'acw_tc': '2760829b15711074239423186e998a0cbb959e3df712c81ecc4e6e5458d7de',
            'xq_a_token': 'd831cd39b53563679545656fba1f4efd8e48faa0',
            #'xq_r_token': 'fd2f0f487c8298cad8e7519f1560abb7a18c589d',
            #'u':'231571107324553',
            #'device_id':'56506e653b88416904d843dbbc43bcfc'
        }
        r = requests.get(url, params=params, headers=headers, cookies=cookies).json()
        print(r)

    def inspect_response(self, r: Response):
        print(r.headers)
        print(r.cookies)
        print(r.encoding)
        print(r.status_code)
        print(r.url)
        print(r.text)
        print(r.json())