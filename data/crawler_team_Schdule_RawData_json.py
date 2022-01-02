import os
import requests

# 모든 팀의 경기정보를 수집하는 web crawler
# 수집 사이트 : kbo Home > (상단 탭) : 일정/결과 > 경기일정/결과
# 과거 코드는 더블헤더 경기 및 취소된 다음 경기의 날짜 기록이 누락되는 문제점 존재
# 
# 수집대상 : 모든 팀
# 대상기간 : 2018 ~ 2021

# 수집할 연도 목록
list_year = list(range(2021, 2022))
list_month = ['01','02','03','04','05','06','07','08','09','10','11','12']

# 사이트('https://www.koreabaseball.com/Schedule/Schedule.aspx?seriesId=0,9')
# 접속 > 팀 목록 탭에서 '전체' 선택 > 개발자 도구 > 네트워크 > 필터 추가('GetScheduleList')
# 가장 마지막 파일 우클릭 > 복사 > 'cURL로 복사'
# 'https://curlconverter.com/#'에 접속 > 'curl command' txt box에 붙여넣기 > Language: python 선택
# > cookies, headers, data 객체 복사하여 아래 붙여넣기
# > 실행

cookies = {
    'ASP.NET_SessionId': 'dzdtuyvtoolbgfdhnmffi5b5',
    '_ga': 'GA1.2.581474984.1640291259',
    '_gid': 'GA1.2.729044495.1640378177',
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'DNT': '1',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-platform': '"macOS"',
    'Origin': 'https://www.koreabaseball.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.koreabaseball.com/Schedule/Schedule.aspx?seriesId=0,9',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6,ja;q=0.5,pt;q=0.4',
}

data = {
  'leId': '1',
  'srIdList': '0,9',
  'seasonId': '2021',
  'gameMonth': '04',
  'teamId': ''
}

dirpath = './teamScheduleRawData_json/'
os.makedirs(dirpath, exist_ok=True) # dir 생성

for year in list_year:
    data['seasonId'] = str(year)
    for mon in list_month:
        data['gameMonth'] = mon
        # fileName format : '리그종류_연도_월.json'
        fullPath = dirpath + data['srIdList'] + '_' + data['seasonId'] + '_' + data['gameMonth'] + '.json'
        response = requests.post('https://www.koreabaseball.com/ws/Schedule.asmx/GetScheduleList',
                                 headers=headers, cookies=cookies, data=data)

        with open(fullPath, 'w', encoding='utf-8-sig') as f:
            f.write(response.text)
            print(f'>>> path : {fullPath} is saved.')
    print()
    
print('\n>>> END <<<')