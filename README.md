![GitHub repo size](https://img.shields.io/github/repo-size/ShaneYokota72/SportsBetting-Assist)
# SportsBetting Assist

SportsBetting Assist is a Python project designed to provide sports bettors with data-driven insights that can help them make more informed betting decisions. By leveraging data from an online API, the program calculates a linear regression line and an r^2 value for a given player's performance in various categories such as points, rebounds, and steals. Based on this information, users can determine whether they should place a bet above, below, or not at all.

## Getting Started

To use SportsBetting Assist, you will need to follow these steps:

1. Clone the repository to your local machine.
2. Open the `SportsBettingAssist.py` file and run the file.
3. When prompted, login or signup.
4. Then when prompted, enter the name of the player you wish to analyze and get betting assist on.
5. The program will obtain the relevant data, calculate the linear regression line and r^2 value, and display the suggested betting decision.

## Technologies Used

SportsBetting Assist was built using Python and the following libraries:

* `nba_api`: Used to send HTTP requests to the API and retrieve data.

[nba_api](https://pypi.org/project/nba-api/) is an API Client for `www.nba.com`. nba_api requires `Python 3.7+` along with the requests and numpy packages. 

```
pip install nba_api

# or

pip install nba-api

# or

pip3 install nba_api

# or

pip3 install nba-api
```

## Real Data Results
| Player Name        | Betting Category | Betting Threshold | Betting Date | Program Output     | Actual Outcome | Accuracy |
|--------------------|------------------|-------------------|--------------|--------------------|----------------|----------|
| Aaron Gordon       | Steal            | 0.5               | Jun 4th      | Strongly bet on less than threshold     | Less           | O        |
| Kevin Love         | Rebounds         | 4.0               | Jun 4th      | Scattered - Don't make a bet | More           | O        |
| Jimmy Butler       | Rebounds         | 6.0               | Jun 4th      | Scattered - Don't make a bet | More           | O        |
| Michael Porter Jr  | Rebounds         | 8.0               | Jun 4th      | Scattered - Don't make a bet | Less           | O        |
| Gabe Vincent       | Points           | 13.5              | Jun 4th      | Strongly bet on more than threshold     | More           | O        |
| Nikola Jokic       | Assist           | 11                | Jun 4th      | Scattered - Don't make a bet | Less           | O        |
| Nikola Jokic       | Points           | 0.5               | Jun 1st      | Strongly bet on more than threshold     | More           | O        |
| Jimmy Butler       | Assists          | 6.0               | Jun 1st      | Scattered - Don't make a bet | More           | O        |
| Jamal Murray       | Points           | 25.5              | Jun 1st      | Strongly bet on more than threshold     | More           | O        |
| Gabe Vincent       | Points           | 12.5              | Jun 1st      | Scattered - Don't make a bet | More           | O        |
| Ban Adebayo        | Assists          | 3.5               | Jun 1st      | Scattered - Don't make a bet | More           | O        |
| Jamal Murray       | Rebounds         | 5.0               | Jun 1st      | Strongly bet on more than threshold     | More           | O        |
| Caleb Martin       | Rebounds         | 7                 | Jun 1st      | Strongly bet on more than threshold     | Less           | X        |




## Contribution Guidelines

If you wish to contribute to SportsBetting Assist, please fork the repository and make your changes. When submitting a pull request, please explain the changes you made and why they are important.

If you wish to contribute to the Real Data Results, please privately contact me with all the above column information filled.

## Credits

SportsBetting Assist was created by Shane Yokota. Data was obtained from `npa_api`. Special thanks to the creators of the libraries used in this project.
