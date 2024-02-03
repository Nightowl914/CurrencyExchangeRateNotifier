import requests
from bs4 import BeautifulSoup
import smtplib
import time

# Ask user to enter a currency of their choice (e.g., "sgd", "usd")
exchange_currency = input("Enter a currency: ")

# Website URL
url = f"https://www.google.com/search?q={exchange_currency}+to+myr&sca_esv=44922cbe319e9a1e&rlz=1C1GCEA_enMY1020MY1020&sxsrf=ACQVn0_OqfYe4b-mSTnXUOZNdrM_jxVmDQ%3A1706873512143&ei=qNK8ZbGmCLyz4-EPuYqvuAo&ved=0ahUKEwixmviqx4yEAxW82TgGHTnFC6cQ4dUDCBA&uact=5&oq=sgd+to+myr&gs_lp=Egxnd3Mtd2l6LXNlcnAiCnNnZCB0byBteXIyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQFIhhdQAFi-E3ABeAGQAQCYAQCgAQCqAQC4AQPIAQD4AQGoAhTiAwQYACBBugYGCAEQARgB&sclient=gws-wiz-serp"

# User Agent
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

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

    info = f"{title_start} {converted_rate} {title_end}"
    print(info)
    
    # Return value as tuple
    return converted_rate, info

# Function used to send email notification
def send_mail(email, pwd, info, compare_rate, converted_rate, subject):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(email, pwd)

    subject = subject
    body = f"The exchange rate has gone from {compare_rate} to {converted_rate}!\n\nThe current exchange rate is {info}.\n\nCheck the currency status through this link:\nhttps://www.google.com/search?q={exchange_currency}+to+myr&sca_esv=44922cbe319e9a1e&rlz=1C1GCEA_enMY1020MY1020&sxsrf=ACQVn0_OqfYe4b-mSTnXUOZNdrM_jxVmDQ%3A1706873512143&ei=qNK8ZbGmCLyz4-EPuYqvuAo&ved=0ahUKEwixmviqx4yEAxW82TgGHTnFC6cQ4dUDCBA&uact=5&oq=sgd+to+myr&gs_lp=Egxnd3Mtd2l6LXNlcnAiCnNnZCB0byBteXIyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQFIhhdQAFi-E3ABeAGQAQCYAQCgAQCqAQC4AQPIAQD4AQGoAhTiAwQYACBBugYGCAEQARgB&sclient=gws-wiz-serp"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        email,
        email,
        msg
    )
    print("Email Successfully Sent!")

    server.quit()

# Main function to execute the script
def main():
    compare_rate = 3.51
    email = "your email"
    pwd = "your password"

    # Execute the check_rate function to print the info and return the values as tuple
    exchange_rate_info = check_rate()
    # Extract the value from the tuple, exchange_rate_info with the index of 0 which is the converted rate
    converted_rate = exchange_rate_info[0]
    # Extract the value from the tuple, exchange_rate_info with the index of 1 which is the info
    info = exchange_rate_info[1]
    # Check if the current exchange rate is lesser or greater than the predefined rate and pass the data as parameters into the send_mail function
    if (converted_rate < compare_rate):
        send_mail(email, pwd, info, compare_rate, converted_rate, "The exchange rate has fallen!")
    elif (converted_rate > compare_rate):
        send_mail(email, pwd, info, compare_rate, converted_rate, "The exchange rate has risen!")
        
if __name__ == "__main__":
    while(True):
        main()
        # Loop the script every 1 hour to check if the rate has fallen or risen
        time.sleep(3600)

