import csv

def parse_file():
    """Parse data from csv to python"""
    rugby_data = []
    with open("./data/results.csv") as dataFile:
        reader = csv.reader(dataFile, delimiter=',')
        line_count = 0
        for row in reader:
            if line_count == 0:
                line_count+=1
            else:
                new_data = {
                    "date": row[0],
                    "home_team": row[1],
                    "away_team": row[2],
                    "home_score": row[3],
                    "away_score": row[4],
                    "competition": row[5],
                    "stadium": row[6],
                    "city": row[7],
                    "country": row[8],
                    "neutral": row[9],
                    "world_cup": row[10]
                }
                # print(f'NEW DATA: {new_data}')
                rugby_data.append(new_data)
                line_count+= 1
    return rugby_data
