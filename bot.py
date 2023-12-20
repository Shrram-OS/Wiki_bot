import telebot

bot = telebot.TeleBot(r"YOUR_TOKEN", parse_mode='html')

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import lxml

options = webdriver.EdgeOptions()

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0")
options.add_argument("--headless")

def wiki(query):
    driver = webdriver.Edge(options=options)
    driver.get(r"https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0")

    search_field = driver.find_element(By.XPATH, '//*[@id="searchInput"]')

    search_field.send_keys(query)

    search_button = driver.find_element(By.XPATH, '//*[@id="searchButton"]')

    search_button.click()

    driver.implicitly_wait(10)

    src = BeautifulSoup(driver.page_source, "lxml")

    if not src: return "Page not found."

    paragraph = src.find(class_="mw-content-ltr")

    if not paragraph: return "Page not found."

    paragraph = paragraph.find("p", recursive=False)

    if not paragraph: return "Page not found."

    text = ""

    for tag in paragraph:
            text += tag.text

    return text



@bot.message_handler(content_types=['text'])
def text(message):
    if message.text.startswith("!wiki"):
        bot.send_message(message.chat.id, text=f"{wiki(message.text[5:])}", parse_mode="html")


if __name__ == '__main__': 
    bot.polling(none_stop=True)
