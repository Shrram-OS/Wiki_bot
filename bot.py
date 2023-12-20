import telebot

bot = telebot.TeleBot(r"6809626698:AAHM0Yv004dSpy5qydfMv9lrBjKzjiXs1k4", parse_mode='html')

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import lxml

options = webdriver.EdgeOptions()

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0")
options.add_argument("--headless")

def wiki(query):
    driver = webdriver.Edge(options=options)
    driver.get(r"https://www.wikipedia.org/")

    search_field = driver.find_element(By.XPATH, '//*[@id="searchInput"]')

    search_field.send_keys(query)

    search_button = driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')

    search_button.click()

    driver.implicitly_wait(10)

    src = BeautifulSoup(driver.page_source, "lxml")

    if not src: return "Page not found."

    text = src.find(class_="mw-content-ltr mw-parser-output")

    if not text: return "Page not found."

    paragraph = text.find("p", recursive=False)

    if not paragraph: return "Page not found."
    
    return paragraph.get_text()


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text.startswith("!wiki"):
        bot.send_message(message.chat.id, text=f"{wiki(message.text[5:])}", parse_mode="html")


if __name__ == '__main__': 
    bot.polling(none_stop=True)
