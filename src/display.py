from parsing import parse_file
from analytics import build_analytic_data

RAW_DATA = parse_file()
DISPLAY_DATA = build_analytic_data()

def display_raw_data_command_line():
    """
    Display raw data from rugby dataset to the terminal
    :return: None
    """
    global RAW_DATA

    for line in RAW_DATA:
        print(f'Date:{line['date']}\n'
              f'Home Team: {line['home_team']} Away Team: {line['away_team']}\n'
              f'Home Score: {line['home_score']} Away Score: {line['away_score']}\n'
              f'Competition: {line['competition']} Stadium: {line['stadium']}\n'
              f'City: {line['city']} Country: {line['country']}\n'
              f'Neutral: {line['neutral']} World Cup: {line['world_cup']}\n')
        print("-----------------------------------------------------------------")

def display_analytic_data_command_line():
    """
    Display calculated analytic data to the command line
    :return: None
    """
    for team in DISPLAY_DATA.keys():
        print(f'COUNTRY: {team.upper()}\n'
              f'TOTAL APPEARANCES: {DISPLAY_DATA[team]['total_appearances']} TOTAL WINS: {DISPLAY_DATA[team]['win_total']} '
              f'TOTAL LOSSES: {DISPLAY_DATA[team]['loss_total']} TOTAL DRAWS: {DISPLAY_DATA[team]['draw_total']}\n'
              f'WIN RATE: {DISPLAY_DATA[team]['win_rate']} LOSS RATE: {DISPLAY_DATA[team]['loss_rate']}\n'
              f'HOME APPEARANCES: {DISPLAY_DATA[team]['home_games']} AWAY APPEARANCES: {DISPLAY_DATA[team]['away_games']}')

        print("-------------------------------------------------------------------")
# display_raw_data_command_line()
display_analytic_data_command_line()