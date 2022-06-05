#!/usr/bin/env python3
from modules import web_scrape
import argparse

parser = argparse.ArgumentParser(
    description="Script that will test login to a web page!"
)
parser.add_argument("-w", "--webp", default = "https://app.sysdigcloud.com/#/login", help="URL of the login page")
parser.add_argument("-p", "--password", default = "xyz.edu", help="Password to test")
parser.add_argument("-u", "--username", default = "username", help="Username to test, email format")
args = parser.parse_args()

username, password = web_scrape.setLoginCredentials(args.username, args.password)

web_scrape.initializeChromeDriver(args.webp)

web_scrape.testLogin(username, password)

# web_scrape.closeChromeDriver()