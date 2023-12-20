# Telegram Bot with Selenium and BeautifulSoup for Wikipedia

This telegram bot gives you the opportunity to get the information on Wikipedia, using Selenium to automate the web browser and BeautifulSoup (bs4) to parse the first paragraph.

## How to use

1. **Adding a bot to a group**
    Add the bot to your group and give it the necessary permission to read and send messages.
2. **Command for searching Wikipedia**

    To start a search on Wikipedia, write the command to this group:
    ```
    !wiki <query>
    ```
    Where `<query>` is your query to search Wikipedia.


## Technical details

- **Selenium:**
    The Selenium library is used to automate the web browser. The browser bot opens and searches the Wikipedia page and return the page HTML for parsing.

- **BeautifulSoup (bs4):**
    BeautifulSoup is used to parse Wikipedia HTML pages. The bot extracts the first paragraph from the text of the article.

## Note

This bot provides a convenient way to get short information from Wikipedia directly in your Telegram group.