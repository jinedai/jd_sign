from requests import Session
import job
import json
import urllib.request
import http.cookiejar
import socket


class Nuts:
    job_name = '坚果vpn签到'
    logger = job.logger
    header = {
        'Content-Type': 'application/json',
        'Content-Length': '315',
        'Connection': 'Keep-Alive',
        'Accept-Language': 'zh-CN,en,*',
        'User-Agent': 'Mozilla/5.0',
        'Host': 'dfrzrujw.com',
    }

    def __init__(self, session: Session):
        self.session = session
        self.job_success = False

    def run(self):
        self.logger.info('Job Start: {}'.format(self.job_name))
        header = {
            'Content-Type': 'application/json',
            'Content-Length': '315',
            'Connection': 'Keep-Alive',
            'Accept-Language': 'zh-CN,en,*',
            'User-Agent': 'Mozilla/5.0',
            'Host': 'dfrzrujw.com',
        }
        opener  = urllib.request.build_opener()
        url = 'https://dfrzrujw.com/api/client/v4/signin'
        data = {
            "app_channel": "pc",
            "app_version": "nuts",
            "app_version_number": "1.0.1",
            "device_model": "pc",
            "device_name": "CNCFCWD1000110",
            "device_uuid": "6C:4B:90:51:EF:2E",
            "net_env": "network",
            "operator": "pc",
            "password": "z2sfhsyk",
            "platform": "pc",
            "system_version": "windows 10.0 10240",
            "username": "sup12914098"
        }
        data = json.dumps(data).encode(encoding='UTF8')
        req = urllib.request.Request(url, data, headers = header)
        try:
            currentPage = urllib.request.urlopen(req, timeout=10).read()
            data = json.loads(currentPage)
            apiToken = data['data']['user']['api_token']

            header2 = {
                'Content-Type': ' application/json',
                'Authorization': apiToken,
                'Connection': ' Keep-Alive',
                'Accept-Language': ' zh-CN,en,*',
                'User-Agent': ' Mozilla/5.0',
                'Host': ' dfrzrujw.com',
            }
            url = 'https://dfrzrujw.com/api/client/v1/users/checkin'
            req = urllib.request.Request(url, {}, headers = header2)
            result = opener.open(req, timeout=10).read()
            print(result)
        except socket.error:
            print('socket result')
            return None
        except Exception as e:
            print(e)
            print('other error')
            return None

        self.job_success = True
        self.logger.info('Job End.')
