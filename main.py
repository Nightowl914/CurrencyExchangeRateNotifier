import os
import requests
from bs4 import BeautifulSoup
import smtplib
import time
import schedule
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Ask user to enter a currency of their choice (e.g., "sgd", "usd")
exchange_currency = input("Enter a currency: ")

# Website URL
url = f"https://www.google.com/search?q={exchange_currency}+to+myr&sca_esv=44922cbe319e9a1e&rlz=1C1GCEA_enMY1020MY1020&sxsrf=ACQVn0_OqfYe4b-mSTnXUOZNdrM_jxVmDQ%3A1706873512143&ei=qNK8ZbGmCLyz4-EPuYqvuAo&ved=0ahUKEwixmviqx4yEAxW82TgGHTnFC6cQ4dUDCBA&uact=5&oq=sgd+to+myr&gs_lp=Egxnd3Mtd2l6LXNlcnAiCnNnZCB0byBteXIyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQFIhhdQAFi-E3ABeAGQAQCYAQCgAQCqAQC4AQPIAQD4AQGoAhTiAwQYACBBugYGCAEQARgB&sclient=gws-wiz-serp"

# User Agent
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# Global variable to store the previous exchange rate
previous_exchange_rate = 3.53

# Function used to extract exchange rate information
def check_rate():
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # Target the desired data
    title_start = soup.find(class_="vk_sh c8Zgcf B682Df").get_text()
    exchange_rate = soup.find(class_="DFlfde SwHCTb").get_text()
    title_end = soup.find('span', {'data-name': 'Malaysian Ringgit'}).get_text()

    # Convert exchange rate into float value
    converted_rate = float(exchange_rate)

    info = f"{title_start} {converted_rate} {title_end}."
    print(info)
    
    # Return value as tuple
    return converted_rate, info

# Function used to send email notification
def send_mail(email, recipient, pwd, subject, text):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(email, pwd)

    subject = subject
    body = f"{text}\n\nCheck the currency status through this link:\n{url}"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        email,
        recipient,
        msg
    )
    print("Email Successfully Sent!")

    server.quit()

# Main function to execute the script
def main():
    global previous_exchange_rate 
    email = os.environ.get('SENDER_EMAIL')
    recipient = os.environ.get('RECIPIENT_EMAIL')
    pwd = os.environ.get('SENDER_EMAIL_PASSWORD')

    # Execute the check_rate function to print the info and return the values as tuple
    exchange_rate_info = check_rate()
    # Extract the value from the tuple, exchange_rate_info with the index of 0 which is the converted rate
    converted_rate = exchange_rate_info[0]
    # Extract the value from the tuple, exchange_rate_info with the index of 1 which is the info
    info = exchange_rate_info[1]

    if previous_exchange_rate is not None:
        # Compare rates and pass relevant data as parameters to the send_mail function
        if (converted_rate < previous_exchange_rate):
            send_mail(email, recipient, pwd, "The Exchange Rate Has Fallen!", f"The exchange rate has gone from {previous_exchange_rate} to {converted_rate}\n\nThe current exchange rate is {info}")
        elif (converted_rate > previous_exchange_rate):
            send_mail(email, recipient, pwd, "The Exchange Rate Has Risen!", f"The exchange rate has gone from {previous_exchange_rate} to {converted_rate}!\n\nThe current exchange rate is {info}")
        elif (converted_rate == previous_exchange_rate):
            send_mail(email, recipient, pwd, "Exchange Rate Update", f"The current exchange rate still remain the same at {info}")

    # Update previous_flight_price with the latest exchange rate
    previous_exchange_rate = converted_rate
        
if __name__ == "__main__":
    # Schedule the script to run at specified time using schedule library
    schedule.every().day.at("08:30").do(main)
    schedule.every().day.at("14:00").do(main)
    schedule.every().day.at("23:43").do(main)

    while True:
        schedule.run_pending()
        time.sleep(1) 
