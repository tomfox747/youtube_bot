from selenium import webdriver
import time
from random import randrange

refresh_time = 10
browser_list = []

brower_one = webdriver.Chrome("C:\\Users\\Tom\\Downloads\\chromedriver")
brower_two = webdriver.Chrome("C:\\Users\\Tom\\Downloads\\chromedriver")
brower_three = webdriver.Chrome("C:\\Users\\Tom\\Downloads\\chromedriver")

browser_list.append(brower_one)
browser_list.append(brower_two)
browser_list.append(brower_three)

for browser in browser_list:
    browser.get("https://www.youtube.com/channel/UCKmEFdiZhwXQqkDF-mKxlZg")

while(True):
    browser_num = randrange(0, len(browser_list))
    browser_list[browser_num].refresh()
    print("browser number ", browser_num, " has been refreshed")
    time.sleep(refresh_time)