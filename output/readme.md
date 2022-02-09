
proc_ScoreBoard/proc_play_review.ipynb 수행결과


## Game_info Feature 구성
# G_ID :: BaseInfo['G_ID']. Game id
# START_TM :: BaseInfo['START_TM']. 경기 시작 시간
# END_TM :: BaseInfo['END_TM']. 경기 종료 시간
# AWAY_HOME :: 홈/어웨이 팀 구분. 어웨이:1, 홈:2
# TEAM_ID :: Team_idx와 join. 팀 코드를 두자리 int로 구성된 ID 값으로 대체.
# SCORE :: 해당 팀의 경기 점수 출력
# PLAY_RESULT :: BaseInfo['T_SCORE_CN','B_SCORE_CN']의 값을 비교하여 승:3, 무:2, 패:1
# PRAK_ID :: BaseInfo['S_NM']과 Park_idx join 수행. asos code와 동일.
# YEAR :: G_ID 앞 4자리