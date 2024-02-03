# CurrencyExchangeRateNotifier

## Introduction
A Python script to monitor and notify user about changes in the exchange rate of a specified currency to Malaysian Ringgit (MYR). The script uses web scraping to fetch real-time exchange rate information from Google Search and sends email notifications when the rate falls or rises beyond a predefined rate.

## Instructions
1. #### Clone the Repository:
```
git clone https://github.com/Nightowl914/CurrencyExchangeRateNotifier.git
```

2. #### Install Dependencies:
```
pip install requests beautifulsoup4
```

3. #### Run the Script:
- ##### Open the script in a text editor.
- ##### Modify the exchange_currency variable to the currency of your choice or use it as user input (e.g., "sgd", "usd").
- ##### Set your email and password for sending notifications (Use Google create app password under Manage Your Google Account -> Security -> 2-Step Verification -> App passwords. Make sure to turn on 2-Step Verification on your account). 
- ##### Adjust the compare_rate variable to your desired rate.
- ##### Save the changes.
- ##### Run the script:
  ```
  python main.py
  ```

4. #### Sit Back and Receive Notifications:
- ##### The script will check the exchange rate every hour (Adjust according to your needs). 
- ##### You will receive email notifications if the rate falls or rises beyond the specified rate.

Feel free to customize the script according to your needs!
