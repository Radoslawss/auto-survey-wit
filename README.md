# Selenium script for automated filling WIT Academy surveys

## Setup
To run this script, you need Python installed along with Selenium. Additionally, the Chrome browser driver (chromedriver) is required.

### Installing Selenium and Chromedriver
1. Install Selenium:
   ```bash
   pip install selenium
   ```
2. Download the appropriate version of [chromedriver](developer.chrome.com/docs/chromedriver/downloads).

### Setting Variables

Set the variables in the script(login and password are this one which you use to log in in to the ubi2.wit.edu.p):

* username: Your login
* password: Your password
* select_value: The value to be selected for each survey(from 1 to 5).
* message: The message to be entered in the last question of the survey.

## Execution
```
python selenium_script.py
```