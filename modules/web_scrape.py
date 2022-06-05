from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
import re
import logging

logging.basicConfig(level=logging.INFO)
driver : webdriver.Chrome = None
def setLoginCredentials(username: str, password: str):
    if not isValidUsernameFormat(username):
        logging.critical(f"Username provided = '{username}'. Does not follow the correct email format")
        exit(1)
    return username, password

def initializeChromeDriver(web_page: str):
    try:
        global driver
        driver = webdriver.Chrome("chromedriver")
        driver.get(web_page)
        logging.info("Sysdig Login page opened")
    except:
        path = os.environ["PATH"]
        logging.error(f"[ERROR] Chrome driver not found in $PATH variable")
        logging.info(f"[INFO] Please add it to one of the following locations of the PATH variable: {path}")
        exit(1)
    
def testLogin(username_cred :str, password_cred: str):
    # Getting the username and password elements
    global wait
    wait = WebDriverWait(driver, 10)
    log_in_button = wait.until(lambda x: x.find_element_by_xpath( "//button[text()='Log in']"))
    username = wait.until(lambda x: x.find_element_by_name("username"))
    password = wait.until(lambda x: x.find_element_by_name("password"))

    # Passing the username and password credentials to the fields
    username.send_keys(username_cred)
    password.send_keys(password_cred)
    log_in_button.click()
    isSuccessfullLogin()

def closeChromeDriver():
    driver.close()

def isValidUsernameFormat(username: str):
    # Regex that validated the email format
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, username)):
        return True
    else: 
        return False

def isSuccessfullLogin():
    try:
        wait.until(lambda x: x.find_element_by_xpath( "//p[@data-output='error-message']"))
        logging.error(f"Log in Failed!")
    except:
        logging.info(f"Succesfull login")