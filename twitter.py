#import all libraries
from selenium.webdriver import ActionChains
from selenium import webdriver as web
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#useless
def cont():
    
    return "ibrahim-twitter(X).py"


#get driver from main page
def drivers(driv):
    
    global driver
    driver=driv


#open url and max window
def openurl(url):
    
    driver.get(url)
    driver.maximize_window()
    time.sleep(1.5)

    print("Webpage opened")


#get xpaths from notepad
def xpaths(name,paths):
    f=open(f"{name}.txt","r")
    raw_xpaths=list(f.read().split("\n"))
    f.close()
    b=[i.split(":")[1] for i in raw_xpaths]
    return(b[paths])


#login twitter
def login(s="usermane",usern="username",passw="password",key="sessionid"):
    
    if s=="username":
        
        #write username
        driver.find_element(By.XPATH,xpaths("x-xpath",0)).send_keys(usern)
        time.sleep(0.3)
    
        #click next button
        driver.find_element(By.XPATH,xpaths("x-xpath",1)).click()
        time.sleep(5)
    
        #write password
        driver.find_element(By.XPATH,xpaths("x-xpath",2)).send_keys(passw)
        time.sleep(0.3)
    
        #click login button
        driver.find_element(By.XPATH,xpaths("x-xpath",3)).click()
        time.sleep(1)
        print("Logged in with using username & password")
        
    #using sessionid to bypass login progress
    else:

        #set cookie
        driver.add_cookie({"name": "auth_token", "domain":".x.com", "value": key})
        driver.refresh()
        time.sleep(5)
        print("Logged in with using sessionid")


#share tweet (with pic or without)
def share_tweet(tweet_text,photo_url="none"):

    #again open twitter
    time.sleep(5)
    print("Start Sharing")


    #write tweet
    driver.find_element(By.XPATH,xpaths("x-xpath",4)).send_keys(tweet_text)
    time.sleep(1)

    #if you want to tweet with photo photo_url chage false to url
    if photo_url!="none":
        
        #photo Keys.CONTROL + 'v'
        #driver.find_element(By.XPATH,xpaths("x-xpath",4)).send_keys(Keys.CONTROL + 'v')
        
        #enter photo
        driver.find_element(By.XPATH,xpaths("x-xpath",5)).send_keys(photo_url)
        time.sleep(8)

    #tweet button
    driver.find_element(By.XPATH,xpaths("x-xpath",6)).click()  

    print("Tweet shaerd")
