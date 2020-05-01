import constants
import time

team_imported = [constants.TEAMS]
player_roster = [constants.PLAYERS]
count = 0


def make_teams():

    global team1
    global team2
    global team3

    for team in team_imported:
        team1 = team[0]
        team2 = team[1]
        team3 = team[2]

    global panthers
    panthers = []
    global bandits
    bandits = []
    global warriors
    warriors = []

    global panthers_height
    panthers_height = []
    global bandits_height
    bandits_height = []
    global warriors_height
    warriors_height = []

    for list_of_dict in player_roster:
        for dicts_of_players in list_of_dict:
            for key, value in dicts_of_players.items():
                if value == 'NO' and len(panthers) < 4:
                    player = dicts_of_players.get("name")
                    height = dicts_of_players.get("height")
                    height = height[0:2]
                    panthers_height.append(height)
                    panthers.append(player)

                elif value == 'YES' and len(panthers) < 6:
                    player = dicts_of_players.get("name")
                    height = dicts_of_players.get("height")
                    height = height[0:2]
                    panthers_height.append(height)
                    panthers.append(player)

                elif value == 'NO' and len(bandits) < 6:
                    player = dicts_of_players.get("name")
                    height = dicts_of_players.get("height")
                    height = height[0:2]
                    bandits_height.append(height)
                    bandits.append(player)

                elif value == 'YES' and len(bandits) < 6:
                    player = dicts_of_players.get("name")
                    height = dicts_of_players.get("height")
                    height = height[0:2]
                    bandits_height.append(height)
                    bandits.append(player)

                elif value == 'NO' and len(warriors) < 6:
                    player = dicts_of_players.get("name")
                    height = dicts_of_players.get("height")
                    height = height[0:2]
                    warriors_height.append(height)
                    warriors.append(player)

                elif value == 'YES' and len(warriors) < 6:
                    player = dicts_of_players.get("name")
                    height = dicts_of_players.get("height")
                    height = height[0:2]
                    warriors_height.append(height)
                    warriors.append(player)

def start_app():
    while True:
        print("""

-------------- MENU --------------
        Here are your choices:
        1): Team Rosters
        2): Individual Player Stats
        3): Quit
        """)

        try:
            choice = int(input("Enter an option >>  "))
            if choice != 1 and choice != 2 and choice != 3:
                raise ValueError

        except ValueError as err:
            print("Input must be either 1, 2 or 3")

        else:
            if choice == 1:
                teams()
            elif choice == 2:
                players()
            else:
                exit()

def teams():

    make_teams()
    results = [int(element) for element in panthers_height]
    panthers_average_height = sum(results) / 6
    results = [int(element) for element in bandits_height]
    bandits_average_height = sum(results) / 6
    results = [int(element) for element in warriors_height]
    warriors_average_height = sum(results) / 6

    while True:
        print("-------------- TEAMS --------------")
        print("        1): "+team1+"             ")
        print("        2): "+team2+"             ")
        print("        3): "+team3+"             ")
        print("        4): Main Menu")

        try:
            choice = int(input("Enter a team number to view that teams roster, or enter 4 to go back to the main menu.  "))
            if choice != 1 and choice != 2 and choice !=3 and choice != 4:
                raise ValueError

        except ValueError as err:
            print("Input must be either 1, 2, 3, or 4")

        else:
            if choice == 1:
                print("This team consists of..", len(panthers), "players.")
                print("Average height of this team is", panthers_average_height, "inches.")
                print(', '.join(panthers))
                print("")
                print("")
                time.sleep(4)
            elif choice == 2:
                print("This team consists of..", len(bandits), "players.")
                print("Average height of this team is", round(bandits_average_height, 1), "inches.")
                print(', '.join(bandits))
                print("")
                print("")
                time.sleep(4)
            elif choice == 3:
                print("This team consists of..", len(warriors), "players.")
                print("Average height of this team is", warriors_average_height, "inches.")
                print(', '.join(warriors))
                print("")
                print("")
                time.sleep(4)
            elif choice == 4:
                start_app()

def players():

    print("""
------------- PLAYERS --------------
Which players stats would you like to view?
Type QUIT to exit program, or MENU to go back to the Main Menu.
    """)
    player_choice = str(input("Type a player name to view stats.  "))

    global count
    count = 0
    while True:

        if player_choice.upper() == "QUIT":
            quit()
        elif player_choice.upper() == "MENU":
            start_app()
        else:
            for dict_of_players in constants.PLAYERS:
                for key, value in dict_of_players.items():

                        if player_choice.upper() == value.upper():
                            this_player = dict_of_players
                            name = this_player.get('name')
                            guardians = this_player.get('guardians')
                            experience = this_player.get('experience')
                            height = this_player.get('height')
                            print("You chose:", name)
                            print("Guardians:", guardians)
                            print("Experience playing?", experience)
                            print("Height:", height)
                            count = 0
                            players()

                        else:
                            count += 1
                            if count == 72:
                                print("Sorry that player is not listed within our records")
                                print("Would you like to view our list of players?  ")
                                while True:

                                    try:
                                        list_of_players_view = input("Please enter YES or NO:  ")
                                        list_of_players_view = list_of_players_view.upper()
                                        if list_of_players_view != "YES" and list_of_players_view != "NO":
                                            raise ValueError

                                    except ValueError as err:
                                        print("Input must be either YES or NO.  ")

                                    else:
                                        if list_of_players_view == "YES":
                                            list_of_players()
                                        elif list_of_players_view == "NO":
                                            players()

def list_of_players():
    while True:
        for dict_of_players in constants.PLAYERS:
                print(dict_of_players['name'])
        players()

if __name__ == '__main__':
    start_app()
