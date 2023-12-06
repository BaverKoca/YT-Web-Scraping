#_*_coding: utf-8_*_

import selenium 
import bs4
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random

browser_data = webdriver.Chrome() # You can use any kind of search motor you want. Just check is it give permission to scraping.
eligibleUsers = set()

def getHTML(url, browser_instance):
    browser_instance.get(url)
    time.sleep(5) # You  can change time for wait there. But if chat is so crawded or your internet speed is slow, you can change till 30 second
    return browser_instance.page_source

def parselHTML(html_source):
    return BeautifulSoup(html_source, "html.parser")

def getMessages(soup):
    return soup.find_all("yt-live-chat-text-message-renderer")

def getEligibleUsers(messages):
    keyword = "keyword-here" # Write which keyword you wanna search from live-chat
    eligibleUsers = set()
    for message in messages:
        content = message.find("div", {"id":"content"})
        author = content.find("span",{"id": "author-name"}).text
        message_content = content.find("span",{"id": "message"}).text
        if keyword in message_content.lower():
            eligibleUsers.add(author)
    return eligibleUsers

print("Draw is starting!")
html_source = getHTML("YTLink-here", browser_data) # You can put any live-chat link from YT for search, just copy and past there.
soup = parselHTML(html_source)
messages = getMessages(soup)
eligibleUsers = getEligibleUsers(messages)
print("Eligible users are: ", eligibleUsers)
print("Total eligible users:", len(eligibleUsers)) # Here you can see how many people wrote your keywords in chat.
time.sleep(2) # You  can change time for wait there.
browser_data.quit()
time.sleep(3) # You  can change time for wait there.

for i in range(1, 4): # It's optional. You don't have to use that loop if you wanna see the winner quick.
    dots = i * "."
    print("A random number is draw." + dots) # Here waiting till show to winner from eligible users.
    time.sleep(1) # That is waiting time for between of all "A random number is draw." loop.
print("\n\n")

eligibleUsersList = list(eligibleUsers)
print("And the winner...", random.choice(eligibleUsersList)) # That code is for show the winner.
