
from requests import Session
import job
import socket
import urllib.request
import http.cookiejar
import socket


class Yanxuan:
    job_name = '严选签到'
    logger = job.logger
    header = {
        'Cookie': 'P_INFO=m13168782535@163.com|1531472544|0|yanxuan|00&99|gud&1531472544&yanxuan#gud&440300#10#0#0|131535&0|yanxuan&yanxuan_check&lmlc_check|13168782535@163.com; S_INFO=1531472544|0|0&60##|m13168782535|; yx_username=m13168782535%40163.com; yx_userid=32647961;NTES_SESS=D8d9HUD3eyLgl66pn8YHVK.TLpKh6feJCKDSTp5YbpgquWdmu57zsxGJWMMd2sTFpXWlmAo4R8aioClVLLNKhveyqKjT9m2_RFGpC2G9dX6wH.su_OGpo9FFFvD22Il2bP3FghJ8JbqrSSQzTUd44QcRtlAZGX4FuCKuJYEmXb.TqxdhcQZflQgJlxwJc8bBtP3VyYV5EB083mbx_4qePrEvc; yx_aui=8af8582a-b6a1-412a-9770-45615ad44a24; yx_app_uuid=45158c1ae77deaaa4bfaea0131b1ea0; yx_app_type=android; yx_app_channel=betaOnline',
        'X-Requested-With': 'com.netease.yanxuan',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,en-US;q=0.8',
        'Referer': 'https://m.you.163.com/points/index',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Content-Length': '0',
        'Host': 'm.you.163.com',
        'Origin': 'https://m.you.163.com',
        'Connection': 'Keep-Alive',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; SM-G955N Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 yanxuan/3.8.6 device-id/cbca280f2f6752ecc275f0589b0b19a5 app-chan-id/betaOnline trustId/android_trustid_4fec63e34456422a8381a16e9c0e059f'
    }

    def __init__(self, session: Session):
        self.session = session
        self.job_success = False

    def run(self):
        self.logger.info('Job Start: {}'.format(self.job_name))

        cookie  = http.cookiejar.CookieJar()
        handler = urllib.request.HTTPCookieProcessor(cookie)
        opener  = urllib.request.build_opener(handler)
        url = 'https://m.you.163.com/points/index'
        req = urllib.request.Request(url, headers = self.header)
        try:
            currentPage = opener.open(req, timeout=10).read()
            csrf = ''
            for item in cookie:
                if item.name == 'yx_csrf':
                    csrf = item.value
            url2 = 'https://m.you.163.com/xhr/points/sign.json?csrf_token=' + csrf
            header2 = {
                'Host': 'm.you.163.com',
                'Connection': 'keep-alive',
                'Content-Length': '0',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Origin': 'https://m.you.163.com',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; SM-G955N Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 yanxuan/3.8.6 device-id/cbca280f2f6752ecc275f0589b0b19a5 app-chan-id/betaOnline trustId/android_trustid_4fec63e34456422a8381a16e9c0e059f',
                'Referer': 'https://m.you.163.com/points/index',
                'Accept-Encoding': 'gzip,deflate',
                'Accept-Language': 'zh-CN,en-US;q=0.8',
                'Cookie': 'yx_csrf=' + csrf + '; P_INFO=m13168782535@163.com|1531472544|0|yanxuan|00&99|gud&1531472544&yanxuan#gud&440300#10#0#0|131535&0|yanxuan&yanxuan_check&lmlc_check|13168782535@163.com; S_INFO=1531472544|0|0&60##|m13168782535|;NTES_SESS=D8d9HUD3eyLgl66pn8YHVK.TLpKh6feJCKDSTp5YbpgquWdmu57zsxGJWMMd2sTFpXWlmAo4R8aioClVLLNKhveyqKjT9m2_RFGpC2G9dX6wH.su_OGpo9FFFvD22Il2bP3FghJ8JbqrSSQzTUd44QcRtlAZGX4FuCKuJYEmXb.TqxdhcQZflQgJlxwJc8bBtP3VyYV5EB083mbx_4qePrEvc; yx_aui=8af8582a-b6a1-412a-9770-45615ad44a24; yx_app_uuid=45158c1ae77deaaa4bfaea0131b1ea0; yx_app_type=android; yx_app_channel=betaOnline; yx_sid=269c7cee-cb38-4d6a-b773-41d4bb9ab124; yx_username=m13168782535%40163.com; yx_userid=32647961'
            }
            req = urllib.request.Request(url2, {}, headers=header2)
            currentPage = urllib.request.urlopen(req, timeout=10).read()
            print(currentPage)
        except urllib.URLError:
            print('url error')
            return None
        except socket.error:
            print('socket result')
            return None
        except Exception as e:
            print(e)
            print('other error')
            return None

        self.job_success = True
        self.logger.info('Job End.')
