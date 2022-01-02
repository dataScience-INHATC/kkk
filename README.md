# kbo_study
...
readme

###### old
	team_rawData.zip
	 코드로 수집했던 경기정보




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
