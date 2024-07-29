import requests
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

parser = argparse.ArgumentParser(description="Process some subdomains.")
parser.add_argument('--d', type=str, required=True, help='The base domain to use')
args = parser.parse_args()
domain = args.d

lock = Lock()

def fetch_url(Sub, current_line, total_lines, domain):
    Sub = Sub.strip()
    URL = f'https://{Sub}.{domain}'
    try:
        with lock:
            print(f'\r[{current_line}/{total_lines}] OUTPUT : {Sub} ', end='', flush=True)
        R = requests.get(URL, timeout=5)
        if R.status_code == 200:
            with lock:
                print(f'\r[{current_line}/{total_lines}] OUTPUT : {Sub} - {URL}\n', end='', flush=True)
    except requests.exceptions.RequestException:
        pass

with open('./Data/sdomain.txt', 'r') as Domains:
    lines = Domains.readlines()
    total_lines = len(lines)

with ThreadPoolExecutor(max_workers=30) as executor:
    futures = [
        executor.submit(fetch_url, Sub, current_line, total_lines, domain)
        for current_line, Sub in enumerate(lines, start=1)
    ]

    for future in as_completed(futures):
        future.result()

print("\nDone.")