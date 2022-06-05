from modules import web_scrape

username, password = web_scrape.setLoginCredentials("username@domain.com", "password")

web_scrape.initializeChromeDriver("https://app.sysdigcloud.com/#/login")

web_scrape.testLogin(username, password)

# web_scrape.closeChromeDriver()