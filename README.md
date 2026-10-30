# Python Proxy Checker

A lightweight and fast multi-threaded proxy checker written in Python. It reads proxies from a text file, tests them concurrently using `ThreadPoolExecutor`, and saves the working ones to a separate file.

## Features

- **Fast & Concurrent:** Utilizes `ThreadPoolExecutor` to check multiple proxies simultaneously.
- **Duplicate Removal:** Automatically removes duplicate proxies from your input list using Python sets.
- **Timeout Protection:** Configured with a request timeout to filter out slow or dead proxies quickly.
- **Simple Output:** Saves only valid, working proxies into a clean text file.

## Prerequisites

Make sure you have Python installed along with the `requests` library. You can install requests via pip:

```bash
pip install requests
```

How to Download
git clone [https://github.com/ramfiles/proxyChecker.git](https://github.com/ramfiles/proxyChecker.git)
cd proxyChecker


How to Use
Clone or download this repository.

Add the proxies to the proxies.txt file, one per line (for example, in the format IP:PORT, or including protocols such as http://IP:PORT).

Run the script:

```bash
python main.py
```
Once the process is complete, you will find all working proxies saved in working.txt.

Code Configuration
TEST_URL: Change this URL if you want to test against a different endpoint (default is http://httpbin.org/ip).

max_workers: Adjust the number of threads in the ThreadPoolExecutor (default is 50) based on your network and system capacity.
