from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players

def retreive_player_id() -> int:
    player = None
    player_dict = players.get_players()

    while player is None:
        try:
            player_name = input("what is the name of the player? (Please capitalize the Initials of the name): ")
            player = [player for player in player_dict if player['full_name'] == player_name][0]
        except:
            print("The player name is not valid. Please try again")
    
    return player['id']

def retrieve_past_ten(stats:list[list[int]]) -> list[list[int]]:
    if len(stats)>10:
        return stats[:10]
    return stats

def find_player_stats(past_ten_data:list[list[int]]) -> dict[str, list[int]]:
    """
        This function will get a dictionary with the key of statistics category and value of statistics list given the past ten games data in the raw form from the API/web scraping. After getting the raw form data, it should return something like {'Rebounds': [10, 8, 1, 3, 10, 6, 5, 9, 2, 4], 'Assist': [1, 1, 0, 1, 0, 2, 1, 1, 0, 0], 'Steal': [2, 2, 1, 1, 0, 0, 1, 2, 0, 0], 'Blocks': [5, 0, 0, 1, 0, 1, 1, 1, 0, 0], 'Points': [17, 10, 2, 2, 8, 11, 5, 16, 2, 2]}
    """
    #most recent stats is the first index
    stats_sorted = {'Rebounds':[], 'Assist':[], 'Steal':[], 'Blocks':[], 'Points':[]}
    for i in past_ten_data:
        stats_sorted['Rebounds'].append(i[0])
        stats_sorted['Assist'].append(i[1])
        stats_sorted['Steal'].append(i[2])
        stats_sorted['Blocks'].append(i[3])
        stats_sorted['Points'].append(i[4])
    
    return stats_sorted

def get_betting_category(all_stats:dict[str, list[int]]) -> str:
    """
        This function will return the betting category the user decides to pursue. After getting the dictionary of k:statistic category(ex, points, rebounds, etc) and v:list of past statistics(ex. 20,23,23,20,18), it will print out all the options for the user, and obtain which category the user wants to make a bet on.
    """

    print("Category Options")
    count = 1
    for i in all_stats:
        print(f"\t{count}) {i}")
        count += 1

    choice = input("Please select a betting category(e.x.) Rebounds): ")
    while choice not in all_stats:
        choice = input("Please select a valid option: ")

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

    # Print the equation of the regression line and the R-squared value
    # print(f"Regression line equation: y = {slope:.2f}x + {y_intercept:.2f}")
    # print(f"R-squared value: {r_squared:.2f}")
    
    # Return the slope, y_intercept, R-squared value, Avg Residual diff
    return [slope, y_intercept, r_squared, avg_residual_diff]

def betting_decision():
    
    print("Not done")

def main():
    player_id = retreive_player_id()
    game_logs = playergamelog.PlayerGameLog(player_id=player_id, season='2022', season_type_all_star='Regular Season').get_dict()['resultSets'][0]['rowSet']

    # filter the data to 18:REB, 19:AST, 20:STL, 21:BLK, 22:PTS
    filtered_data = [[row[18], row[19], row[20], row[21], row[24]] for row in game_logs]
    # after filtering the data needed, cut the amount of data to the recent 10, then re-organize it for easier understanding
    print("after organized")
    past_ten_stats = retrieve_past_ten(filtered_data)
    organized_stats = find_player_stats(past_ten_stats)
    print(organized_stats)
    betting_category = get_betting_category(organized_stats)
    analysiscomp = analyze(betting_category, organized_stats)
    print(analysiscomp)

if __name__ == "__main__":
    main()