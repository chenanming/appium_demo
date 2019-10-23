import requests
import base64
import json

class TestEncode:
    origin_url = "http://47.95.238.18:10000/topics.txt"  # json��ʽ������
    url = "http://47.95.238.18:10000/topics_encode.txt"  # ���ܸ�ʽ������

    def test_get(self):
        r = requests.get(self.origin_url)
        print(r.content)
        assert len(r.json()['topics']) == 2

    def test_encode(self):
        r = requests.get(self.url)     # ԭʼ����raw
        print(r.content)

        data = self.decode(r.content)  # ����ԭʼ����raw
        print(data)

        j = json.loads(data)           # �Խ��ܺ�����ݣ����б���
        print(j)

        assert len(j['topics']) == 2

    def decode(self, raw):  # decode()����ԭʼ����
        return base64.b64decode(raw)

    def test_api(self):
        req=ApiRequest()
        req_data={
            'schema': 'http',
            'method': 'GET',
            'url': 'http://47.95.238.18:10000/topics_encode.txt',
            'headers': None,
            'encoding': 'base64'
        }
        j=req.send(req_data)
        print(j)
        assert len(j['topics']) == 2

class ApiRequest:
    def send(self, data: dict):
        if data['schema'] == 'http':
            # ��host�޸�Ϊip��������host header
            env = {
                "docker.testing-studio.com": {
                    "dev": "1.1.1.1",
                    "test": "1.1.1.2"
                },
                "default": "dev"
            }
            data["url"] = str(data["url"]).replace(
                "docker.testing-studio.com",
                env["docker.testing-studio.com"][env["default"]]
            )
            data["headers"]["Host"] = "docker.testing-studio.com"
            res=requests.request(data['method'], data['url'], headers=data['headers'])
            if data['encoding'] == 'base64':
                return json.loads(base64.b64decode(res.content))
            else:
                return json.loads(res.content)

        elif 'dubbo' == data['schema']:
            pass
        elif 'websocket' == data['schema']:
            pass
        else:
            pass