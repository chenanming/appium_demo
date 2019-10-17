import requests
import logging
logging.basicConfig(
    level=logging.INFO
)

class TestWecht():
    def test_get_token(self):
        get_access_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?"
        params = {
            'corpid': 'wwda2949fda2df78ef',
            'corpsecret': '7hMSoLgTRmLSEn2YQkR-Mf9FoXInu6uUvqhdujXx4vw'
        }
        res = requests.get(get_access_url, params=params)
        print(res)
        return res

    def test_approval_get_token(self):
        try:
            res = self.test_get_token()
            if res.status_code == 200:
                access_token = res.json()['access_token']
                logging.info('获取到的access_token是:' + access_token)
                return access_token
        except Exception as e:
            logging.error(e)

if __name__ == '__main__':
    we = TestWecht()
    #we.test_get_token()
    we.test_approval_get_token()