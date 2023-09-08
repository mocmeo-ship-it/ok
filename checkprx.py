# python
import requests
import threading

# Nhập tên file chứa danh sách proxy
proxy_file = input("Enter proxy file name: ")

# Đọc danh sách proxy từ file
with open(proxy_file, 'r') as f:
    proxies = f.read().splitlines()

valid_proxies = []
lock = threading.Lock()

def check_proxy(proxy):
    try:
        response = requests.get('http://www.google.com', proxies={'http': proxy, 'https': proxy}, timeout=5)
        if response.status_code == 200:
            with lock:
                valid_proxies.append(proxy)
                print('Valid proxy:', proxy)
    except:
        print('Invalid proxy:', proxy)

# Sử dụng thread để kiểm tra các proxy đồng thời
threads = []
for proxy in proxies:
    t = threading.Thread(target=check_proxy, args=(proxy,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Nhập tên file để lưu danh sách các proxy hợp lệ
valid_proxy_file = input("Enter valid proxy file name: ")

# Ghi danh sách các proxy hợp lệ vào file
with open(valid_proxy_file, 'w') as f:
    for proxy in valid_proxies:
        f.write(proxy + '\n')
