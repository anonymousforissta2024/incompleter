#Source: https://stackoverflow.com/questions/53474945/cannot-plot-dataframe-as-barh-because-typeerror-empty-dataframe-no-numeric-d
import csv
import pandas
import numpy
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

set_of_teams = set()

def load_epl_games(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        raw_data = {"HomeTeam": [], "AwayTeam": [], "FTHG": [], "FTAG": [], "FTR": []}
        for row in reader:
            set_of_teams.add(row["HomeTeam"])
            set_of_teams.add(row["AwayTeam"])
            raw_data["HomeTeam"].append(row["HomeTeam"])
            raw_data["AwayTeam"].append(row["AwayTeam"])
            raw_data["FTHG"].append(row["FTHG"])
            raw_data["FTAG"].append(row["FTAG"])
            raw_data["FTR"].append(row["FTR"])
        data_frame = pandas.DataFrame(data=raw_data)
    return data_frame

def calc_points(team, table):
    points = 0
    for row_number in range(table["HomeTeam"].count()):
        home_team = table.loc[row_number, "HomeTeam"]
        away_team = table.loc[row_number, "AwayTeam"]
        if team in [home_team, away_team]:
            home_team_points = 0
            away_team_points = 0
            winner = table.loc[row_number, "FTR"]
            if winner == 'H':
                home_team_points = 3
            elif winner == 'A':
                away_team_points = 3
            else:
                home_team_points = 1
                away_team_points = 1
            if team == home_team:
                points += home_team_points
            else:
                points += away_team_points
    return points

def get_goals_scored_conceded(team, table):
    scored = 0
    conceded = 0
    for row_number in range(table["HomeTeam"].count()):
        home_team = table.loc[row_number, "HomeTeam"]
        away_team = table.loc[row_number, "AwayTeam"]
        if team in [home_team, away_team]:
            if team == home_team:
                scored += int(table.loc[row_number, "FTHG"])
                conceded += int(table.loc[row_number, "FTAG"])
            else:
                scored += int(table.loc[row_number, "FTAG"])
                conceded += int(table.loc[row_number, "FTHG"])
    return (scored, conceded)

def compute_table(df):
    raw_data = {"Team": [], "Points": [], "GoalDifference":[], "Goals": []}
    for team in set_of_teams:
        goal_data = get_goals_scored_conceded(team, df)
        raw_data["Team"].append(team)
        raw_data["Points"].append(calc_points(team, df))
        raw_data["GoalDifference"].append(goal_data[0] - goal_data[1])
        raw_data["Goals"].append(goal_data[0])
    data_frame = pandas.DataFrame(data=raw_data)
    data_frame = data_frame.sort_values(["Points", "GoalDifference", "Goals"], ascending=[False, False, False]).reset_index(drop=True)
    data_frame.index = numpy.arange(1,len(data_frame)+1)
    data_frame.index.names = ["Finish"]
    return data_frame

def get_finish(team, table):
    return table[table.Team==team].index.item()

def get_points(team, table):
    return table[table.Team==team].Points.item()

def display_hbar(tables):
    raw_data = {"Team": [], "Points": []}
    for row_number in range(tables["Team"].count()):
        raw_data["Team"].append(tables.loc[row_number+1, "Team"])
        raw_data["Points"].append(int(tables.loc[row_number+1, "Points"]))
    df = pandas.DataFrame(data=raw_data)
    #df = pandas.DataFrame(tables, columns=["Team", "Points"])
    print(df)
    print(df.dtypes)
    df["Points"].apply(int)
    print(df.dtypes)
    df.plot(kind='barh',x='Points',y='Team')

games = load_epl_games('epl2016.csv')
final_table = compute_table(games)
#print(final_table)
#print(get_finish("Tottenham", final_table))
#print(get_points("West Ham", final_table))
display_hbar(final_table)