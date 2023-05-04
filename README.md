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

`nba_api` is an API Client for `www.nba.com`. nba_api requires `Python 3.7+` along with the requests and numpy packages. 
```
pip install nba_api
```

## Contribution Guidelines

If you wish to contribute to SportsBetting Assist, please fork the repository and make your changes. When submitting a pull request, please explain the changes you made and why they are important.

## Credits

SportsBetting Assist was created by Shane Yokota. Data was obtained from `npa_api`. Special thanks to the creators of the libraries used in this project.