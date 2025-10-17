from parsing import parse_file
def display_command_line():
    """
    Display data from rugby dataset to the terminal
    :return: None
    """

    data = parse_file()
    print("date,home_team,away_team,home_score,away_score,competition,stadium,city,country,neutral,world_cup")
    for line in data:
        print(f'Date:{line['date']}\n'
              f'Home Team: {line['home_team']} Away Team: {line['away_team']}\n'
              f'Home Score: {line['home_score']} Away Score: {line['away_score']}\n'
              f'Competition: {line['competition']} Stadium: {line['stadium']}\n'
              f'City: {line['city']} Country: {line['country']}\n'
              f'Neutral: {line['neutral']} World Cup: {line['world_cup']}\n')
        print("-----------------------------------------------------------------")

display_command_line()