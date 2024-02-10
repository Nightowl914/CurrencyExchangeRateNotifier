# CurrencyExchangeRateNotifier

## Introduction
A Python script to monitor and notify user about changes in the exchange rate of a specified currency to Malaysian Ringgit (MYR). The script uses web scraping to fetch real-time exchange rate information from Google Search and sends email notifications when the exchange rate changes.

## Instructions
1. #### Clone the Repository:
```
git clone https://github.com/Nightowl914/CurrencyExchangeRateNotifier.git
```

2. #### Install Dependencies:
```
pip install requests beautifulsoup4 schedule python-dotenv
```

3. #### Run the Script:
- ##### Open the script in a text editor.
- ##### Modify the exchange_currency variable to the currency of your choice or use it as user input (e.g., "sgd", "usd").
- ##### Set your email and password for sending notifications by adding the following environment variables to the .env file:
  ```
  SENDER_EMAIL=your_email@gmail.com
  RECIPIENT_EMAIL=recipient_email@example.com
  SENDER_EMAIL_PASSWORD=your_email_password
  ```
- ##### Replace 'your_email@gmail.com' with your Gmail address, 'recipient_email@example.com' with the recipient's email address, and 'your_email_password' with your Gmail account password.
- ##### Adjust the compare_rate variable to your desired rate.
- ##### Save the changes.
- ##### Run the script:
  ```
  python main.py
  ```
- ##### The script will run at the specified times each day to check for updates in exchange rate.
- ##### You can modify the schedule by adjusting the 'schedule.every().day.at()' calls in the script to your preferred times.
  
4. #### Sit Back and Receive Notifications:
- ##### If there are changes in exchange rate, you will receive email notifications at the specified email address (RECIPIENT_EMAIL).

Feel free to customize the script according to your needs!
