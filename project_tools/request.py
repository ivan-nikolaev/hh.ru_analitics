from bs4 import BeautifulSoup
#import tools.request
import random
#from tools.json_tools import *

import requests
import random

class ControlRequestClass:
    def __init__(self):
        pass

    def GetRandomUserAgent(self):
        user_agents = ['Googlebot',
                       'MSNBot',
                       'Mozilla/1.1 (compatible; MSPIE 2.0; Windows CE)',
                       'Mozilla/1.10 [en] (Compatible; RISC OS 3.70; Oregano 1.10)',
                       'Mozilla/1.22 (compatible; MSIE 1.5; Windows NT)',
                       'Mozilla/1.22 (compatible; MSIE 2.0; Windows 95)',
                       'Mozilla/1.22 (compatible; MSIE 2.0d; Windows NT)',
                       'Mozilla/1.22 (compatible; MSIE 5.01; PalmOS 3.0) EudoraWeb 2',
                       'Mozilla/2.0 (compatible; MSIE 3.01; Windows 98)',
                       'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)',
                       'Mozilla/4.0 (compatible; MSIE 5.0; Mac_PowerPC) Opera 6.0 [en]',
                       'Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.9 sun4u; X11)',
                       'Mozilla/4.0 (compatible; MSIE 5.0; Windows 2000) Opera 6.03 [ru]',
                       'Mozilla/4.0 (compatible; MSIE 5.17; Mac_PowerPC)',
                       'Mozilla/4.0 (compatible; MSIE 5.23; Mac_PowerPC)',
                       'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)',
                       'Mozilla/4.0 (compatible; MSIE 6.0; ; Linux armv5tejl; U) Opera 8.02 [en_US] Maemo browser 0.4.31 N770/SU-18',
                       'Mozilla/4.0 (compatible; MSIE 6.0; MSN 2.5; Windows 98)',
                       'Mozilla/4.0 (compatible; MSIE 6.0; Nitro) Opera 8.50 [de]',
                       'Mozilla/4.0 (compatible; MSIE 6.0; Nitro) Opera 8.50 [en]',
                       'Mozilla/4.0 (compatible; MSIE 6.0; Nitro) Opera 8.50 [es]',
                       'Mozilla/4.0 (compatible; MSIE 6.0; Nitro) Opera 8.50 [fr]',
                       'Mozilla/4.0 (compatible; MSIE 6.0; Nitro) Opera 8.50 [it]',
                       'Mozilla/4.0 (compatible; MSIE 6.0; Nitro) Opera 8.50 [ja]',
                       'Mozilla/4.0 (compatible; MSIE 6.0; Symbian OS; Nokia 6600/5.27.0; 1657) Opera 8.60 [ru]',
                       'Mozilla/4.0 (compatible; MSIE 6.0; Symbian OS; Nokia 6600/5.27.0; 1665) Opera 8.60 [en]',
                       'Mozilla/4.0 (compatible; MSIE 6.0; Symbian OS; Nokia 6600/5.27.0; 1665) Opera 8.60 [fr]',
                       'Mozilla/4.0 (compatible; MSIE 6.0; Symbian OS; Nokia 6600/5.27.0; 6329) Opera 8.00 [it]',
                       'Mozilla/4.0 (compatible; MSIE 6.0; Symbian OS; Nokia 6600/5.27.0; 6936) Opera 8.50 [zw]',
                       'Mozilla/4.0 (compatible; MSIE 6.0; Symbian OS; Nokia 6600/5.27.0; 9399) Opera 8.65 [ja]',
                       'Mozilla/4.0 (compatible; MSIE 6.0; Symbian OS; Nokia 6600/5.27.0; 9424) Opera 8.65 [ch]',
                       'Mozilla/4.0 (compatible; MSIE 6.0; Symbian OS; Nokia 6630/4.03.38; 6937) Opera 8.50 [es]',
                       'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
                       'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.0.3705; .NET CLR 1.1.4322; Media Center PC 4.0; .NET CLR 2.0.50727)',
                       'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)',
                       'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)',
                       'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.50',
                       'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; .NET CLR 1.1.4322)',
                       'Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux x86_64; ru) Opera 10.10',
                       'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; Arcor 5.005; .NET CLR 1.0.3705; .NET CLR 1.1.4322)',
                       'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; YPC 3.0.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
                       'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
                       'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.0.04506; .NET CLR 3.5.21022)',
                       'Mozilla/4.0 (compatible; MSIE 7.0b; Win32)',
                       'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)',
                       'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; WOW64; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.0.04506; .NET CLR 3.5.21022)',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; WOW64; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.5.21022; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Tablet PC 2.0)',
                       'Mozilla/4.1 (compatible; MSIE 5.0; Symbian OS; Nokia 6600;452) Opera 6.20 [ru]',
                       'Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7',
                       'Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
                       'Mozilla/5.0 (Windows NT 5.1; U; en) Opera 8.50',
                       'Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
                       'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.36 (KHTML, like Gecko) Chrome/12.0.742.53 Safari/534.36 QQBrowser/6.3.8908.201',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.3a) Gecko/20030105 Phoenix/0.5',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.4.154.25 Safari/525.19',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.10 Safari/532.0',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.6b) Gecko/20031215 Firebird/0.7+',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.10) Gecko/20050716 Firefox/1.0.6',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.4) Gecko/20060516 SeaMonkey/1.0.2',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.6) Gecko/20060728 SeaMonkey/1.0.4',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.1) Gecko/20061204 Firefox/2.0.0.1',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1) Gecko/20090624 Firefox/3.5',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.22) Gecko/20110902 Firefox/3.6.22',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; nl-NL; rv:1.7.5) Gecko/20041202 Firefox/1.0',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; nl; rv:1.8) Gecko/20051107 Firefox/1.5',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.8.1.17) Gecko/20080829 Firefox/2.0.0.17',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.8.1.19) Gecko/20081201 Firefox/2.0.0.19',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.20',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.8.1.9) Gecko/20071025 Firefox/2.0.0.9',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.9) Gecko/2008052906 Firefox/3.0',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.9.0.2) Gecko/2008091620 Firefox/3.0.2',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3 (.NET CLR 3.5.30729)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.2; ru; rv:1.9.0.5) Gecko/2008120122 Firefox/3.0.5',
                       'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.8.0.4) Gecko/20060508 Firefox/1.5.0.4',
                       'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
                       'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1',
                       'Mozilla/5.0 (Windows; U; Windows NT 6.0; ru; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3',
                       'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.65 Safari/525.19',
                       'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.89 Safari/532.5',
                       'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.7.8) Gecko/20050609',
                       'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.7.8) Gecko/20050609 Firefox/1.0.4',
                       'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.9) Gecko/20071025 Firefox/2.0.0.9',
                       'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.9a1) Gecko/20061204 GranParadiso/3.0a1',
                       'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.307.9 Safari/532.9',
                       'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.9) Gecko/20050711 Firefox/1.0.5',
                       'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.2) Gecko/20060308 Firefox/1.5.0.2',
                       'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3',
                       'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.6) Gecko/20060808 Fedora/1.5.0.6-2.fc5 Firefox/1.5.0.6 pango-text',
                       'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.2) Gecko/20070220 Firefox/2.0.0.2',
                       'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.2) Gecko/20070221 SUSE/2.0.0.2-6.1 Firefox/2.0.0.2',
                       'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1) Gecko/20060601 Firefox/2.0 (Ubuntu-edgy)',
                       'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090716 Ubuntu/9.04 (jaunty) Shiretoko/3.5.1',
                       'Mozilla/5.0 (X11; U; Linux x86_64; ru; rv:1.9.0.2) Gecko/2008092702 Gentoo Firefox/3.0.2',
                       'Mozilla/5.0 (X11; U; Linux x86_64; ru; rv:1.9.0.4) Gecko/2008111611 Gentoo Iceweasel/3.0.4',
                       'Mozilla/5.0 (X11; U; Linux x86_64; ru; rv:1.9.1.1) Gecko/20090730 Gentoo Firefox/3.5.1',
                       'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.0)',
                       'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.1)',
                       'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.2)',
                       'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0)',
                       'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.1)',
                       'Opera/10.00 (Windows NT 6.0; U; en) Presto/2.2.0',
                       'Opera/7.23 (Windows 98; U) [en]',
                       'Opera/7.51 (Windows NT 5.0; U) [en]',
                       'Opera/7.51 (Windows NT 5.1; U) [ru]',
                       'Opera/7.51 (Windows NT 5.2; U) [ch]',
                       'Opera/7.51 (Windows NT 6.0; U) [zw]',
                       'Opera/7.51 (Windows NT 6.1; U) [ua]',
                       'Opera/8.0 (X11; Linux i686; U; cs)',
                       'Opera/8.51 (Windows NT 5.1; U; en)',
                       'Opera/9.0 (Windows NT 5.1; U; en)',
                       'Opera/9.00 (Nintendo Wii; U; ; 1309-9; en)',
                       'Opera/9.00 (Wii; U; ; 1038-58; Wii Shop Channel/1.0; en)',
                       'Opera/9.01 (X11; Linux i686; U; en)',
                       'Opera/9.02 (Windows NT 5.1; U; en)',
                       'Opera/9.10 (Windows NT 5.1; U; en)',
                       'Opera/9.23 (Windows NT 5.1; U; ru)',
                       'Opera/9.50 (Windows NT 5.1; U; ru)',
                       'Opera/9.50 (Windows NT 6.0; U; en)',
                       'Opera/9.60 (Windows NT 5.1; U; en) Presto/2.1.1',
                       'Opera/9.80 (Windows NT 5.1; U; en) Presto/2.5.18 Version/10.50',
                       'Opera/9.80 (Windows NT 5.1; U; ru) Presto/2.2.15 Version/10.20',
                       'Opera/9.80 (Windows NT 6.1; U; ru) Presto/2.2.15 Version/10.00',
                       'Opera/9.80 (Windows NT 6.1; U; ru) Presto/2.9.168 Version/11.51',
                       'Opera/9.80 (X11; Linux x86_64; U; en) Presto/2.2.15 Version/10.10',
                       'Opera/9.80 (X11; Linux x86_64; U; ru) Presto/2.2.15 Version/10.10',
                       'StackRambler',
                       'Yandex']
        return {'User-agent': random.choice(user_agents)}

    def GetHTML(self, url, proxy_line = None, use_user_agent = False):
        session = requests.session()
        session.timeout = 10

        if(use_user_agent == True):
            session.headers = self.GetRandomUserAgent()
        if(proxy_line != None):
            Adapter = requests.adapters.HTTPAdapter(pool_connections=1, pool_maxsize=0, max_retries=2)
            session.mount('http://', Adapter)
            session.mount('https://', Adapter)
            session.proxies = {'http': proxy_line, 'https': proxy_line}
        try:
            result = session.get(url)
            #print(f'url : {url},\t status_code : {result.status_code}')
            return result.text
        except requests.exceptions.ConnectionError:
            print(f'url : {url},\tSeems like dns lookup failed..')
            return 'error'
        except requests.exceptions.ConnectTimeout:
            print(f'url : {url},\tOops. Connection timeout occured!')
            return 'error'
        except requests.exceptions.ReadTimeout:
            print(f'url : {url},\tOops. Read timeout occured')
            return 'error'
        except requests.exceptions.ConnectionError:
            print(f'url : {url},\tSeems like dns lookup failed..')
            return 'error'
        except requests.exceptions.HTTPError as err:
            print(f'url : {url},\tOops. HTTP Error occured')
            print('Response is: {content}'.format(content=err.response.content))
            return 'error'
        return ""



#======================================================================================
def GetProxiesFromPubProxy(url = "http://pubproxy.com/api/proxy?format=json"):
    cr = tools.request.ControlRequestClass()
    json_string = cr.GetHTML(url)
    proxy_json = json.loads(json_string)
    return proxy_json

def GetProxiesFromProxyDB(url = 'https://www.proxyrotator.com/free-proxy-list/'):
    proxies = []
    cr = ControlRequestClass()
    html = cr.GetHTML(url, use_user_agent = True)
    soup = BeautifulSoup(html, 'lxml')

    try:
        body = soup.find('tbody')
        trs = body.findAll('tr')
        for tr in trs:
            proxy = tr.find('td')
    except Exception:
        pass
    return proxies





def main():
    proxies = ['159.8.114.37:8123',
    '117.4.50.142:32431',
    '103.47.175.13:8080',
    '192.166.134.246:41258',
    '178.128.46.132:8080',
    '103.83.205.57:8080',
    '217.21.124.185:46216',
    '93.139.211.253:8080',
    '195.122.23.24:44132',
    '200.222.46.130:8080',
    '138.97.146.228:52103',
    '180.149.96.134:8080',
    '95.180.179.203:42110',
    '213.247.247.233:54060',
    '195.208.45.218:61608',
    '123.231.237.137:35806',
    '94.183.237.95:23500',
    '181.112.57.54:53281',
    '181.129.52.114:38124',
    '77.90.120.20:51956']


    #proxy_json = GetProxiesFromPubProxy()
    #pp_json(proxy_json)
    #print(proxy_json['data'][0]['ipPort'])
    #html = cr.GetHTML(url, proxy_json['data'][0]['ipPort'])

    url = "http://sitespy.ru/my-ip"

    cr = ControlRequestClass()

    for i in range(5):
        html = cr.GetHTML(url, proxy_line=random.choice(proxies),use_user_agent=True)
        soup = BeautifulSoup(html, 'lxml')
        ip = soup.find('span', class_ = 'ip').text.strip()
        ua = soup.find('span', class_ = 'ip').find_next_sibling('span').text.strip()
        print(ip)
        print(ua)


if __name__ == "__main__":
    # execute only if run as a script
    main()