import requests
from bs4 import BeautifulSoup

exchange_currency = 'sgd'

url = f"https://www.google.com/search?q={exchange_currency}+to+myr&sca_esv=44922cbe319e9a1e&rlz=1C1GCEA_enMY1020MY1020&sxsrf=ACQVn0_OqfYe4b-mSTnXUOZNdrM_jxVmDQ%3A1706873512143&ei=qNK8ZbGmCLyz4-EPuYqvuAo&ved=0ahUKEwixmviqx4yEAxW82TgGHTnFC6cQ4dUDCBA&uact=5&oq=sgd+to+myr&gs_lp=Egxnd3Mtd2l6LXNlcnAiCnNnZCB0byBteXIyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQEyExAAGIAEGIoFGEMY6gIYtALYAQFIhhdQAFi-E3ABeAGQAQCYAQCgAQCqAQC4AQPIAQD4AQGoAhTiAwQYACBBugYGCAEQARgB&sclient=gws-wiz-serp"

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title_start = soup.find(class_="vk_sh c8Zgcf B682Df").get_text()
rate = soup.find(class_="DFlfde SwHCTb").get_text()
title_end = soup.find('span', {'data-name': 'Malaysian Ringgit'}).get_text()

print(f"{title_start} {rate} {title_end}")

