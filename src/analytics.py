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

def get_countries_competitions_stadiums():
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

    print(STADIUMS)
    # print(COMPETITIONS)
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
            "draw_total": TEAM_DRAWS[team]
        }

    return analytic_data



get_countries_competitions_stadiums()
calculate_win_loss_totals()
calculate_total_appearances()
calculate_win_loss_rates()
build_analytic_data()