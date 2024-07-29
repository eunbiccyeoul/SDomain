import sys
import requests

# 파일의 전체 줄 수를 계산
with open('./Data/sdomain.txt', 'r') as Domains:
    lines = Domains.readlines()
    total_lines = len(lines)

# 각 줄을 처리하며 현재 줄 번호를 출력
with open('./Data/sdomain.txt', 'r') as Domains:
    for current_line, Sub in enumerate(Domains, start=1):
        Sub = Sub.strip()
        URL = f'https://{Sub}.kyobodts.co.kr'
        try:
            sys.stdout.write(f'\r[{current_line}/{total_lines}] OUTPUT : {Sub} ')
            sys.stdout.flush()
            R = requests.get(URL, timeout=5)
            if R.status_code == 200:
                sys.stdout.write(f'- {URL}\n')
                sys.stdout.flush()
        except requests.exceptions.RequestException:
            pass

print("\n모든 서브 도메인 시도 완료!")
