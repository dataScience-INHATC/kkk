# kbo_study

###### changes
22.01.02.v01

  - https://github.com/dataScience-INHATC/kkk/blob/master/data/playReview_ScoreBoard_Rawdata.csv
    - 2018~2021까지 play된 경기의 scoreboard 정보.
  - 수집 방법
    - data/ScheduleList_rawdata_v3.csv :: '게임센터' 필드의 gameId 파라미터를 추출하여 그 gameId목록으로 game play review data(2종. scoreboard, boxscore) crawling.
      >> result :: data/teamReviewRawData_json/
  - 수집 후 처리 내용
    - 수집한 RawData(data/teamReviewRawData_json/) 중 scoreboard file만 parsing
    - 제외사항
      - 원래 Schedule 되었던 경기 3187 rows.
      - 취소경기 304 rows :: play되지 않은 경기이므로 review data 자체가 없음.
      - 18~19 올스타전 경기 2 rows(드림 vs 나눔). 현재 비교대상이 아니므로 제외.(gameid는 부여되었지만 crawling 대상에서 제외.)
      ** 3187 - 304 - 2 = 2881 rows
    - 특이사항
      - SR_ID는 정규리그의 경우 모두 0으로 확인되었는데
        2021 결승전(gameId : 20211031KTSS0)
        2021.10.31.(일) KT(1) vs 삼성(0) 경기의 경우 유일하게 SR_ID값이 6으로 부여됨
      - 2018.08.01.(수) NC(9) vs 삼성(5) 경기의 boxscore 정보가 사이트 오류로 없음. scoreboard는 존재. 다른 사이트에서 양식에 맞게 가져올 필요 있음.
        * https://www.koreabaseball.com/Schedule/GameCenter/Main.aspx?gameDate=20180801&gameId=20180801WOSK0&section=REVIEW

  - 향후 작업계획
    - 각 팀의 경기 횟수가 올바른지는 확인 필요.
      * 하지만 각 팀의 game_id는 모두 중복 없음.





여기 아래 정보는 갱신 중...
###### data
  # 기상자료
    SURFACE_ASOS_RawData.zip
        *** https://data.kma.go.kr/data/grnd/selectAsosRltmList.do?pgmNo=36
          * 링크 > 파일셋 메뉴
    - 기상청 종관기상정보(ASOS).
    - 전국에 위치한 여러 기상정보 관측기 중 야구장과 인접한 관측기 11곳에서 식별한 종관기상정보.
    - 각각의 기상관측기는 3자리 숫자 코드로 식별됨.

  # 전국 야구장 위치와 각각에 인접한 ASOS 관측소 위치 코드
      *** https://data.kma.go.kr/data/grnd/selectAsosRltmList.do?pgmNo=36
    parkLocation.csv
    - 1, 2 홈구장
    - 기상청에서 주소 검색하면 인접한 ASOS 관측소 위치를 보여줌.

  # 모든 팀의 경기 정보
    teamRawData_json.zip
      *** https://www.koreabaseball.com/Schedule/Schedule.aspx?seriesId=0,9
    - 기간 : 2010 ~ 2021
    - 상기 페이지에서 자료를 제공해주는 별도 api서버로부터 받아온 경기 정보가 담긴 json data
    - 사용된 크롤러 첨부

  # data frame에 올려놓은 코드
    proc_AsosRawData.ipynb
      ASOS 자료를 dataframe에 올려놨던 최종 자료

    proc_json.ipynb
      teamRawData_json.zip의 경기정보가 담긴 json 파일을 분석하여 dataframe에 올려놓은 자료

###### old
  team_rawData.zip
   코드로 수집했던 경기정보