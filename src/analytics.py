from parsing import parse_file

TEAMS = []
DATA = parse_file()
TEAM_WINS = {}
TOTAL_APPEARANCES = {}
WIN_RATES = {}

def get_countries():
    """
    Get countries that played from dataset
    :return: List of countries that played
    """
    global DATA, TEAMS
    for line in DATA:
        if line['home_team'] not in TEAMS:
            TEAMS.append(line['home_team'])
    print(TEAMS)
    return TEAMS

def calculate_win_totals():
    """
    Calculate win totals of each country
    :return: Dict of countries, win_total
    """
    global TEAM_WINS, TEAMS, DATA
    for team in TEAMS:
        TEAM_WINS[team] = 0

    for line in DATA:
        if line['away_score'] > line['home_score']:
            TEAM_WINS[line['away_team']] += 1
        elif line['home_score'] > line['away_score']:
            TEAM_WINS[line['home_team']] += 1
    print(TEAM_WINS)
    return TEAM_WINS

def calculate_total_appearances():
    """
    Calculate each countries total appearances
    :return: Dict of countries, total_appearances
    """
    global DATA, TOTAL_APPEARANCES, TEAMS
    for team in TEAMS:
        TOTAL_APPEARANCES[team] = 0

    for team in TEAMS:
        for line in DATA:
            if line['away_team'] == team or line['home_team'] == team:
                TOTAL_APPEARANCES[team] +=1
    print(TOTAL_APPEARANCES)
    return TOTAL_APPEARANCES

def calculate_win_rates():
    """
    Calculate the win rate of each team
    :return: Dict of countries, win rate
    """
    global DATA, TEAMS

get_countries()
calculate_win_totals()
calculate_total_appearances()