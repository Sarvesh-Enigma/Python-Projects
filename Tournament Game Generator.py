def get_number_of_teams():
    while True:
        num_teams=int(input("Enter the Number of Teams in the Tournament"))
        if num_teams>=2:
            break
        print("Number of teams must be greater than or equal to 2")
    return num_teams
def get_team_names(num_teams):
    teams=[]
    for idx in range(num_teams):
        while True:
            team=input(f"Enter Name of Team#{idx+1}")
            num_of_words=len(team.split(" "))
            num_char=len(team)
            if num_of_words>2:
                print("Number of words in team name cannot be greater than 2")
            elif num_char<2:
                print("Number of characters in team name can't be less than 2")
            else:
                break
        teams.append(team)
    return teams
def get_number_of_games_played(num_teams):
    while True:
        games_played=int(input("Enter number of games played by each team"))
        if games_played>=num_teams-1:
            break
        else:
            print("Each Team must play each other atleast once")
    return games_played

def get_team_wins(team_names,games_played):
    team_wins=[]
    for team in team_names:
       while True:
           wins=int(input(f"Enter number of wins by {team}"))
           if wins > games_played:
               print("Number of wins can't exceed games played by the team")
           elif wins<0:
               print("Number of wins has to be a positive number")
           else :
               break
       team_wins.append((team,wins))
    return team_wins
    
def get_second_item(item):
    return item[1]
num_teams=get_number_of_teams()
team_names=get_team_names(num_teams)
games_played=get_number_of_games_played(num_teams)
team_wins=get_team_wins(team_names,games_played)
print("Generating Games to be played in the first round of the Tournament....")
sorted_teams=sorted(team_wins,key=get_second_item)
game_pairings=[]
games_to_make=num_teams//2
for game_num in range(games_to_make):
    home_team=sorted_teams[game_num][0]
    away_team=sorted_teams[num_teams-game_num-1][0]
    game_pairings.append([home_team,away_team])
for pairing in game_pairings:
    home_team,away_team=pairing
    print(f"Home:{home_team} vs Away:{away_team}")