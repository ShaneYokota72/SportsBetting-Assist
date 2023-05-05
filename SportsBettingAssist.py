from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players

class PlayerStats:
    """
        This class will get the player's statistics of the past ten games. The statistics will be in the form of a list of lists. Each list will contain the statistics of the past ten games. The statistics will be in the order of [rebounds, assist, steal, blocks, points]. The most recent game will be the first index of the list.
    """

    def __init__(self, player_id:int) -> None:
        """
            This function will initialize the player id and the past ten games statistics. The player id will be used to get the past ten games data from the API. The past ten games statistics will be in the form of a list of lists. Each list will contain the statistics of the past ten games. The statistics will be in the order of [rebounds, assist, steal, blocks, points]. The most recent game will be the first index of the list.
        """

        # Initialize the player id and the past ten games statistics
        self.player_id = player_id
        self.past_ten_stats = []
        # Get the past ten games statistics
        self.get_past_ten_stats()

    def get_past_ten_stats(self) -> None:
        """
            This function will get the past ten games statistics from the API. The statistics will be in the form of a list of lists. Each list will contain the statistics of the past ten games. The statistics will be in the order of [rebounds, assist, steal, blocks, points]. The most recent game will be the first index of the list.
        """

        # Initialize the player game log
        player_game_log = playergamelog.PlayerGameLog(player_id=self.player_id, season='2022', season_type_all_star='Regular Season').get_dict()['resultSets'][0]['rowSet']

        # filter the data to 18:REB, 19:AST, 20:STL, 21:BLK, 22:PTS
        filtered_data = [[row[18], row[19], row[20], row[21], row[24]] for row in player_game_log]

        # after filtering the data needed, cut the amount of data to the recent 10, then re-organize it for easier understanding
        past_ten_stats_raw = self.retrieve_past_ten(filtered_data)
        self.past_ten_stats = self.find_player_stats(past_ten_stats_raw)

    def retrieve_past_ten(self, stats:list[list[int]]) -> list[list[int]]:
        """ 
            This function will return the past ten games data in the raw form from the API/web scraping. The data will be in the form of a list of lists. Each list will contain the statistics of the past ten games. The statistics will be in the order of [rebounds, assist, steal, blocks, points]. The most recent game will be the first index of the list.
        """
    
        # if the stats is more than 10, cut it to 10, thenreturn the stats
        if len(stats)>10:
            return stats[:10]
        return stats

    def find_player_stats(self, past_ten_data:list[list[int]]) -> dict[str, list[int]]:
        """
            This function will get a dictionary with the key of statistics category and value of statistics list given the past ten games data in the raw form from the API/web scraping. After getting the raw form data, it should return something like {'Rebounds': [10, 8, 1, 3, 10, 6, 5, 9, 2, 4], 'Assist': [1, 1, 0, 1, 0, 2, 1, 1, 0, 0], 'Steal': [2, 2, 1, 1, 0, 0, 1, 2, 0, 0], 'Blocks': [5, 0, 0, 1, 0, 1, 1, 1, 0, 0], 'Points': [17, 10, 2, 2, 8, 11, 5, 16, 2, 2]}
        """

        # most recent stats is the first index
        stats_sorted = {'Rebounds':[], 'Assist':[], 'Steal':[], 'Blocks':[], 'Points':[]}
        # organize the raw form of data into a categorized dictionary
        for i in past_ten_data:
            stats_sorted['Rebounds'].append(i[0])
            stats_sorted['Assist'].append(i[1])
            stats_sorted['Steal'].append(i[2])
            stats_sorted['Blocks'].append(i[3])
            stats_sorted['Points'].append(i[4])
        
        return stats_sorted

def login() -> None:
    """
        This function will return a boolean value of True if the user has logged in successfully. If the user fails to log in, it will return a boolean value of False.
    """

    # Initialize the username and password
    username = ""
    password = ""

    # get all the usernames and passwords from the file 'usercredentials.txt' and store them in a dictionary
    user_pw = {}
    f = open("usercredentials.txt", "r")
    for line in f:
        line = line.strip().split(' ')
        user_pw[line[0]] = line[1]

    # Get the user's input
    user = input("Username: ")
    passw = input("Password: ")

    # check if the user and passw is in the file
    # if credential is not correct, ask until they successfully login
    while user not in user_pw or user_pw[user] != passw:
        print("Username or password is incorrect. Please try again.\n")
        user = input("Username: ")
        passw = input("Password: ")
    
    # print login successful message
    print(f"\nLogin successful!\nWelcome to sports betting assist {user}!")

def singup() -> None:
    """
        This function will get the user's input of username and password and store them in the file 'usercredentials.txt'. The username and password will be separated by a space.
    """
    
    # Get the user's input
    user = input("Username: ")
    passw = input("Password: ")
    passwcheck = input("Please re-enter your password: ")

    # Get all the usernames and passwords from the file 'usercredentials.txt' and store them in a dictionary
    user_pw = {}
    f = open("usercredentials.txt", "r")
    for line in f:
        line = line.strip().split(' ')
        user_pw[line[0]] = line[1]
    f.close()

    # Store the user's input in the file if it is valid
    while user in user_pw or passw != passwcheck:
        if user in f:
            user = input("Username already exists. Please try another username: ")
        elif passw != passwcheck:
            passw = input("Passwords did not match. Please try again: ")
            passwcheck = input("Please re-enter your password: ")

    # add the user's input(username and password) to the file
    f = open("usercredentials.txt", "a")
    f.write(f"{user} {passw}\n")
    f.close()

    # Lead them to the login page
    print("\nLOGIN")
    login()

def retreive_player_id() -> int:
    """ 
        This function will return the player id given the player name. The player name will be given by the user. The player id will be used to get the past ten games data from the API.
    """

    # Initialize player and player_dict(API data)
    player = None
    player_dict = players.get_players()

    # Get the player id
    while player is None:
        try:
            player_name = input("\nWhat is the name of the player? (Please capitalize the Initials of the name): ")
            player = [player for player in player_dict if player['full_name'] == player_name][0]
        except:
            print("The player name is not valid. Please try again")
    
    return player['id']

def get_betting_category(all_stats:dict[str, list[int]]) -> str:
    """
        This function will return the betting category the user decides to pursue. After getting the dictionary of k:statistic category(ex, points, rebounds, etc) and v:list of past statistics(ex. 20,23,23,20,18), it will print out all the options for the user, and obtain which category the user wants to make a bet on.
    """

    # Print out all the options for the user
    print("Category Options")
    count = 1
    for i in all_stats:
        print(f"\t{count}) {i}")
        count += 1

    # Get the user's choice
    choice = input("\nPlease select a betting category(e.x.: Rebounds): ")
    while choice not in all_stats:
        choice = input("\nPlease select a valid option: ")

    return choice

def analyze(category:str, sorted_data:dict[str, list[int]]) -> list[float]:
    """
        This function will return an integer value showing the degree of if the user should bet above or below the threshold. In the analysis, I will be using linear regression to see the trends and come up with a data based decision.
    """

    # Initialize the data
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    datalist = sorted_data[category]
    datalist.reverse()
    y = datalist

    # In case theres no data(ex) havent played in a long time)
    if len(y)<1:
        return [0,0,0,0]

    # Calculate the mean of x and y
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)

    # Calculate the slope
    numerator = 0
    for xi, yi in zip(x, y):
        numerator += (xi - mean_x) * (yi - mean_y)

    denominator = 0
    for xi in x:
        denominator += (xi - mean_x)**2

    slope = numerator / denominator

    # Calculate the y-intercept
    y_intercept = mean_y - slope*mean_x

    # Calculate the predicted values of y
    y_predicted = []
    for x_i in x:
        y_hat = slope*x_i + y_intercept
        y_predicted.append(y_hat)

    # Calculate the total sum of squares
    total_sum_squares = 0
    for yi in y:
        total_sum_squares += (yi - mean_y)**2

    # Calculate the residual sum of squares
    residual_sum_squares = 0
    residuals = []
    for yi, y_hat in zip(y, y_predicted):
        residual = yi - y_hat
        residuals.append(abs(residual))
        residual_sum_squares += residual ** 2

    # Calculate the R-squared value
    r_squared = 1 - (residual_sum_squares/total_sum_squares)

    # Calculate the avg redisual difference
    avg_residual_diff = sum(residuals)/ len(residuals)
    
    # Return the slope, y_intercept, R-squared value, Avg Residual diff
    return [slope, y_intercept, r_squared, avg_residual_diff]

def betting_decision(analysis_data:list[int], threshhold:float) -> None:

    """ 
        This function will print out the betting decision based on the analysis data. The analysis data will be a list of slope, y_intercept, R-squared value, Avg Residual diff. The threshold will be the value the user wants to bet on.
    """

    # Get the analysis data
    slope = analysis_data[0]
    y_intercept = analysis_data[1]
    r_squared = analysis_data[2]
    avg_residual_diff = analysis_data[3]

    # Regression line = y = slope*x + y_intercept
    # R^2 = r_squared   Avg Res Diff = avg_residual_diff
    if r_squared < 0.2:
        # data is too spreaded. An accurate analysis and decision making is not possible
        print("\tThe data is scattered and the outcome is unpredictable. I recommend NOT making a bet.")
    else :
        # data is reliable
        predicted_value = 11*slope + y_intercept
        
        # threshold is above the predicted value, so suggest to bet that outcome will be less than the threshold 
        if threshhold > predicted_value:
            # very confident
            if abs(threshhold - predicted_value) > avg_residual_diff:
                print("\tI STRONGLY recommend to bet that outcome will be less than the threshold")
            # normal confidence
            else :
                print("\tI would bet that outcome will be less than the threshold")
        # threshold is below the predicted value, so suggest to bet that outcome will be more than the threshold 
        else:
            # very confident
            if abs(threshhold - predicted_value) > avg_residual_diff:
                print("\tI STRONGLY recommend to bet that outcome will be more than the threshold")
            # normal confidence
            else :
                print("\tI would bet that outcome will be more than the threshold")

def main():
    """
        This function will be the main function of the program. It will call all the other functions and run the program.
    """

    # login/signup as a user and make sure the option is valid
    option = ""
    while option != "1" and option != "Login" and option != "2" and option != "Sign Up":
        option = input("1) Login\n2) Sign Up\n\nPlease select an option: ")
    
    if option == "1" or option == "Login":
        login()
    elif option == "2" or option == "Sign Up":
        singup()

    # keep running the sports betting assist until the user wants to stop
    response = "y"
    while response.lower() == "y":
        # get the player id
        player_id = retreive_player_id()

        # make the PlayerStats object
        Target_Player_Stats = PlayerStats(player_id)
        betting_category = get_betting_category(Target_Player_Stats.past_ten_stats)
        analysiscomp = analyze(betting_category, Target_Player_Stats.past_ten_stats)
        
        # get the betting threshold
        threshold = None
        while threshold == None:
            try:
                threshold = float(input("\nWhat is the betting threshold?(e.x: 3.5, 23, 25.5): "))
                break
            except:
                print("\nPlease enter a valid number")
        
        # print out the betting decision
        betting_decision(analysiscomp, threshold)

        # ask the user if they want to continue
        response = input("\nDo you want to continue (enter y or n)?").strip().lower()

    input("\nThank you for using the sports betting assist!")

if __name__ == "__main__":
    main()
