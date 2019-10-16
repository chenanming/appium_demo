import requests
import json

class TestWecht:

    def test_get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?"
        params = {'corpid': '1970325033079614', 'corpsecret': '1688852882466545'}
        r = requests.get(url, params=params).json()
        if r.status_code == 200:
            return access_token