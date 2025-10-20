from parsing import parse_file
from utils import init_dict

TEAMS = []
RAW_DATA = parse_file()
TEAM_WINS = {}
TOTAL_APPEARANCES = {}
WIN_RATES = {}
TEAM_LOSSES = {}
LOSS_RATES = {}
TEAM_DRAWS = {}
COMPETITIONS = []
STADIUMS = []
HOME_GAMES = {}
AWAY_GAMES = {}
HOME_WINS = {}
HOME_LOSSES = {}
AWAY_WINS = {}
AWAY_LOSSES = {}
HOME_WIN_RATES = {}
AWAY_WIN_RATES = {}
HOME_LOSS_RATES = {}
AWAY_LOSS_RATES = {}

def get_teams_competitions_stadiums():
    """
    Get countries that played from dataset as well as competitions played
    :return: List of countries that played, competitions played
    """
    global TEAMS, COMPETITIONS, STADIUMS
    for line in RAW_DATA:
        if line['home_team'] not in TEAMS:
            TEAMS.append(line['home_team'])
        if line['competition'] not in COMPETITIONS:
            COMPETITIONS.append(line['competition'])
        if line['stadium'] not in STADIUMS:
            STADIUMS.append(line['stadium'])

    return TEAMS, COMPETITIONS, STADIUMS

def calculate_win_loss_totals():
    """
    Calculate win and loss totals of each country
    :return: Tuple of win loss Dicts of countries, win_total
    """
    global TEAM_WINS, TEAM_LOSSES, TEAM_DRAWS
    TEAM_WINS = init_dict(TEAMS)
    TEAM_LOSSES = init_dict(TEAMS)
    TEAM_DRAWS = init_dict(TEAMS)

    for line in RAW_DATA:
        if line['away_score'] > line['home_score']:
            TEAM_WINS[line['away_team']] += 1
            TEAM_LOSSES[line['home_team']] += 1
        elif line['home_score'] > line['away_score']:
            TEAM_WINS[line['home_team']] += 1
            TEAM_LOSSES[line['away_team']] += 1
        elif line['home_score'] == line['away_score']:
            TEAM_DRAWS[line['home_team']] += 1
            TEAM_DRAWS[line['away_team']] += 1

    return TEAM_WINS, TEAM_LOSSES, TEAM_DRAWS

def calculate_total_appearances():
    """
    Calculate each countries total appearances
    :return: Dict of countries, total_appearances
    """
    global TOTAL_APPEARANCES
    TOTAL_APPEARANCES = init_dict(TEAMS)

    for team in TEAMS:
        for line in RAW_DATA:
            if line['away_team'] == team or line['home_team'] == team:
                TOTAL_APPEARANCES[team] +=1
    return TOTAL_APPEARANCES

def calculate_win_loss_rates():
    """
    Calculate the win rate and loss rate of each team as well as tie
    :return: Tuple of win rate and loss rate Dicts of countries, win rate
    """
    global WIN_RATES, LOSS_RATES
    WIN_RATES = init_dict(TEAMS)
    LOSS_RATES = init_dict(TEAMS)
    for team in TEAMS:
        WIN_RATES[team] = round(TEAM_WINS[team] / TOTAL_APPEARANCES[team], 4)*100
        LOSS_RATES[team] = round(100.00-WIN_RATES[team], 4)

    return WIN_RATES, LOSS_RATES

def calculate_home_away_win_loss_rates():
    """
    Calculate the win rate and loss rate of each team per home and away
    :return:
    """
    global AWAY_WIN_RATES, AWAY_LOSS_RATES, HOME_LOSS_RATES, HOME_WIN_RATES
    AWAY_LOSS_RATES = init_dict(TEAMS)
    AWAY_WIN_RATES = init_dict(TEAMS)
    HOME_WIN_RATES = init_dict(TEAMS)
    HOME_LOSS_RATES = init_dict(TEAMS)

    for team in TEAMS:
        HOME_WIN_RATES[team] = round(HOME_WINS[team] / HOME_GAMES[team], 4)*100
        HOME_LOSS_RATES[team] = round(100.00-HOME_WIN_RATES[team], 4)
        AWAY_WIN_RATES[team] = round(AWAY_WINS[team] / AWAY_GAMES[team], 4) * 100
        AWAY_LOSS_RATES[team] = round(100.00-AWAY_WIN_RATES[team], 4)


def calculate_home_away_totals():
    """
    Calculate the home and away game totals for all teams
    :return: Tuple of dictionaries, one home, one away
    """
    global HOME_GAMES, AWAY_GAMES
    HOME_GAMES = init_dict(TEAMS)
    AWAY_GAMES = init_dict(TEAMS)
    for team in TEAMS:
        for line in RAW_DATA:
            if line['away_team'] == team:
                AWAY_GAMES[team] += 1
            elif line['home_team'] == team:
                HOME_GAMES[team] += 1
    return HOME_GAMES, AWAY_GAMES

def calculate_home_away_win_loss():
    """
    Calculate the home and away win/loss totals for each team
    :return: None
    """
    global HOME_WINS, AWAY_WINS, HOME_LOSSES, AWAY_LOSSES
    HOME_WINS = init_dict(TEAMS)
    HOME_LOSSES = init_dict(TEAMS)
    AWAY_WINS = init_dict(TEAMS)
    AWAY_LOSSES = init_dict(TEAMS)

    for team in TEAMS:
        for line in RAW_DATA:
            if line['home_team'] == team and (line['home_score'] > line['away_score']):
                HOME_WINS[team] += 1
            elif line['home_team'] == team and (line['away_score'] > line['home_score']):
                HOME_LOSSES[team] += 1
            elif line['away_team'] == team and (line['home_score'] > line['away_score']):
                AWAY_LOSSES[team] += 1
            elif line['away_team'] == team and (line['away_score'] > line['home_score']):
                AWAY_WINS[team] += 1


def build_analytic_data():
    """
    Build dictionary of calculated data for ease of display
    :return: Dictionary of teams, with a dict of  their stats
    """

    analytic_data = {}
    for team in TEAMS:
        analytic_data[team] = {
            "total_appearances": TOTAL_APPEARANCES[team],
            "win_rate": WIN_RATES[team],
            "loss_rate": LOSS_RATES[team],
            "win_total": TEAM_WINS[team],
            "loss_total": TEAM_LOSSES[team],
            "draw_total": TEAM_DRAWS[team],
            "home_games": HOME_GAMES[team],
            "away_games": AWAY_GAMES[team],
            "away_wins": AWAY_WINS[team],
            "home_wins": HOME_WINS[team],
            "away_losses": AWAY_LOSSES[team],
            "home_losses": HOME_LOSSES[team],
            "home_win_rate": HOME_WIN_RATES[team],
            "home_loss_rate": HOME_LOSS_RATES[team],
            "away_win_rate": AWAY_WIN_RATES[team],
            "away_loss_rate": AWAY_LOSS_RATES[team]
        }

    return analytic_data



get_teams_competitions_stadiums()
calculate_win_loss_totals()
calculate_total_appearances()
calculate_win_loss_rates()
calculate_home_away_totals()
calculate_home_away_win_loss()
calculate_home_away_win_loss_rates()
build_analytic_data()