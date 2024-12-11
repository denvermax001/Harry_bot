# Telegram Movie Download Bot

This project is a **"Telegram Movie Download Bot"** that allows users to search for movies and get direct download links. It uses the **requests** library to scrape movie data from an external website and the **BeautifulSoup** library to parse and extract relevant details. When a user enters a movie query, the bot provides a list of search results with inline buttons for each movie. After the user selects a movie, the bot fetches additional information and generates shortened download links using the **URL Shortener API** for easy access.

This project demonstrates how to integrate web scraping, Telegram Bot API, and URL shortening in Python. It is built for learning purposes only. The bot scrapes movie data from publicly available sources. I do not promote or endorse piracy in any form. Please use this code responsibly, and ensure compliance with copyright laws. I am not responsible for any misuse or legal consequences.

# Deployments

1. Clone Current Repository.
2. Get Bot Token for Telegram: [BotFather](https://telegram.me/BotFather) (Insert bot_token in **"index.py"**).
3. Host Project: [Vercel](https://vercel.com/) (Insert project URL in **"index.py"**).
4. Get URL Shortner API [URLSHORTX](https://urlshortx.com/) (Insert URL Shortner API in **"scraper.py"**).
5. Make changes in **"index.py"** & **"scraper.py"**. In **"scraper.py"**, the **"search_movies"** function needs to use the correct domain when making requests.

# Check out My Projects & Resume
1. Personal Website: [https://nishchal-kansara.web.app/](https://nishchal-kansara.web.app/)
2. Resume: [https://nishchal-kansara.web.app/resume.html](https://nishchal-kansara.web.app/resume.html)

Connect with me on LinkedIn: [Nishchal Kansara](https://www.linkedin.com/in/nishchal-kansara/)
