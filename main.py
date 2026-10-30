import time, requests
from concurrent.futures import ThreadPoolExecutor

TEST_URL = 'http://httpbin.org/ip'
def check_proxy(proxy_str):
    proxySet = {
        'http': proxy_str,
        'https': proxy_str,
    }

    try:
        start_time = time.time()
        response = requests.get(TEST_URL, proxies=proxySet, timeout=4)
        end_time = time.time()
        response_time = round(end_time - start_time, 2)

        if response.status_code == 200:
            print(f"[RUN] {proxy_str}: {response.url}")
            return proxy_str
        else:
            print(f"[ERROR] {proxy_str}: [CODE:{response.status_code}] {response.url}")

    except Exception as e:
        print(f"[DEAD] {proxy_str} | {e}")
    return None


proxies = set()
with open("proxies.txt", "r", encoding = "utf-8") as file:
    for line in file:
        lineEdit = line.strip()
        if lineEdit:
            proxies.add(lineEdit)

proxies = list(proxies)
print(f"{len(proxies)} unique proxies found. List is being updated")

working_proxies = []

with ThreadPoolExecutor(max_workers=50) as executor:
    results = executor.map(check_proxy, proxies)
    for result in results:
        if result:
            working_proxies.append(result)


with open("working.txt", "a", encoding="utf-8") as working_file:
    for proxy in working_proxies:
        working_file.write(f"{proxy}\n")

print("\n The checking completed. The finding have been saved to working.txt")
input("for exit press enter")