CREATE TABLE Base_info(
    LE_ID int,
    SR_ID int,
    G_ID str NOT NULL PRIMARY KEY,
    G_DT date,
    SEASON_ID int,
    HOME_NM str,
    HOME_ID str,
    AWAY_NM str,
    AWAY_ID str,
    S_NM str,
    CROWD_CN str,
    H_W_CN int,
    H_L_CN int,
    H_D_CN int,
    A_W_CN int,
    A_L_CN int,
    A_D_CN int,
    T_SCORE_CN int,
    B_SCORE_CN int,
    START_TM time,
    END_TM time,
    USE_TM time,
    FULL_HOME_NM str,
    FULL_AWAY_NM str,
    H_INITIAL_LK str,
    A_INITIAL_LK str,
    table1 str,
    table2 str,
    table3 str,
    maxInning int,
    checkScroll int,
    code int,
    msg str
);

CREATE TABLE ScoreBoard_tbl3(
    G_ID str NOT NULL PRIMARY KEY,
    AWAY_R int,
    AWAY_H int,
    AWAY_E int,
    AWAY_B int,
    HOME_R int,
    HOME_H int,
    HOME_E int,
    HOME_B int
);

CREATE TABLE Park_idx(
    PARK_NM str NOT NULL PRIMARY KEY,
    PARK_ID int
);

CREATE TABLE Team_idx(
    TEAM_CHAR str NOT NULL PRIMARY KEY,
    TEAM_ID int
);

CREATE TABLE Game_ScoreBoard(
    G_ID str NOT NULL PRIMARY KEY,
    Inning int,
    Score int,
    AWAY_HOME int
);

CREATE TABLE Game_info(
    G_ID str NOT NULL PRIMARY KEY,
    START_TM time,
    END_TM time,
    AWAY_HOME int,
    TEAM_ID int,
    SCORE_CNT int,
    PLAY_RESULT int,
    PARK_ID int,
    YEAR int
);

