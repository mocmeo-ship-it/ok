import requests
import threading
import time

# Nhập tên file chứa danh sách proxy
proxy_file = input("Enter proxy file name: ")

# Nhập số thread
num_threads = int(input("Enter the number of threads: "))

# Đọc danh sách proxy từ file
with open(proxy_file, 'r') as f:
    proxies = f.read().splitlines()

valid_proxies = []
lock = threading.Lock()

def check_proxy(proxy):
    try:
        start_time = time.time()
        response = requests.get('http://www.google.com', proxies={'http': proxy, 'https': proxy}, timeout=5)
        elapsed_time = time.time() - start_time
        if response.status_code == 200:
            with lock:
                valid_proxies.append((proxy, elapsed_time))
                print('Valid proxy:', proxy, 'Speed:', elapsed_time)
        elif response.status_code >= 300:
            print('Invalid proxy:', proxy, 'HTTP Error:', response.status_code)
    except requests.Timeout:
        print('Invalid proxy:', proxy, 'Timeout')
    except requests.RequestException as e:
        print('Invalid proxy:', proxy, 'Error:', str(e))

# Sử dụng thread để kiểm tra các proxy đồng thời
threads = []
total_proxy = len(proxies)
batch_size = total_proxy // num_threads
start_index = 0
end_index = batch_size

for i in range(num_threads):
    if i == num_threads - 1:
        end_index = total_proxy
    proxy_batch = proxies[start_index:end_index]

    for proxy in proxy_batch:
        t = threading.Thread(target=check_proxy, args=(proxy,))
        threads.append(t)
        t.start()

    start_index += batch_size
    end_index += batch_size

for t in threads:
    t.join()

# Sắp xếp danh sách proxy hợp lệ theo tốc độ giảm dần
valid_proxies.sort(key=lambda x: x[1], reverse=True)

# Nhập tên file để lưu danh sách các proxy hợp lệ
valid_proxy_file = input("Enter valid proxy file name: ")

# Ghi danh sách các proxy hợp lệ và tốc độ vào file
with open(valid_proxy_file, 'w') as f:
    for proxy, speed in valid_proxies:
        f.write(proxy'\n')
