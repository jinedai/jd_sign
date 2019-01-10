# -*- coding:utf-8 -*-
import urllib.request
import socket
import json
import re

header = {
'Cookie': 'aliyungf_tc=AQAAAO+7/jMCCAQAAbo8OlnhNhV4HzD6; SourcePage=; FirstBrowsePage=http%3A%2F%2Fwww.fanhuan.com%2F; _ga=GA1.2.772854643.1516592781; gr_user_id=f1e07026-8192-40db-9dfc-37c54547fd16; fingerprint=67ddbd3d08e1c9c010e26488b85b1c65; bfd_g=bc54ecf4bbe35d40000007d9000019b756d4e826; Hm_lvt_29a7ebc4f6a8c90821d8b062a0bf830e=1516592781,1516865374; tma=144470946.37210948.1516592780928.1516592780928.1516865374224.2; A9D5EMD96D5E5G=4WmIDYDShWC9zUeZoKnnCJsvOKHrxTMn02PbFbgxMK0=; userDetial=749290765%40qq.com%7c8816762%7c3; user_name=749290765%40qq.com; checkNum=0cbd0035045dd458ad330291cbb407af; Hm_lpvt_29a7ebc4f6a8c90821d8b062a0bf830e=1516865433; amvid=54037e58055cb7f80c23c95b7075d1b6; _pk_id.www.fanhuan.com.b017=25081c976ec260cd.1516592780.3.1516869625.1516869625.',
'Pragma': 'no-cache',
'X-Requested-With': 'XMLHttpRequest',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Language': 'zh-CN,en-US;q=0.8',
'Referer': 'https://lh.fanhuan.com/Home/IntegralPark?usertype=1&paraname=token&originfortrack=1e425921cbf1cf7c6fc1e7439092851f&token=4WmIDYDShWC9zUeZoKnnCJsvOKHrxTMn02PbFbgxMK0%3D&basic=NFdtSURZRFNoV0M5elVlWm9Lbm5DSnN2T0tIcnhUTW4wMlBiRmJneE1LMD0mbGdmeg==',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Host': 'www.fanhuan.com',
'Connection': 'Keep-Alive',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}

##====================以下为方法========================##
def getContent():
    url = 'http://www.fanhuan.com/ajax/SignIn/?callback=?&s=1'
    req = urllib.request.Request(url, headers = header)
    try:
        currentPage=urllib.request.urlopen(req, timeout=10).read()
        currentPage = json.loads(re.match(".*?({.*}).*", currentPage,re.S).group(1))
        print(currentPage)
    except urllib.URLError:
        print('url error')
        return None
    except socket.error:
        print('socket result')
        return None
    except Exception(e):
        print(e)
        print('other error')
        return None


if __name__ == '__main__':
    red_session = getContent()

