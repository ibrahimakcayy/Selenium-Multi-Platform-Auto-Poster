#import all libraries
from selenium.webdriver import ActionChains
from selenium import webdriver as web
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#useless
def cont():
    
    return "ibrahim-bluesky.py"


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


#login webpage
def login(s="usermane",host="host‬",usrn="username",passw="password",key="sessionid"):
    
    if host!="host":
        
        #click host in button
        driver.find_element(By.XPATH,xpaths("b-xpath",1)).click()
        time.sleep(1)
        
        #click costom  radiobutton 
        driver.find_element(By.XPATH,xpaths("b-xpath",2)).click()
        time.sleep(1)
        
        #write server address
        driver.find_element(By.XPATH,xpaths("b-xpath",3)).send_keys(host)
        time.sleep(0.3)
        
        #click done
        driver.find_element(By.XPATH,xpaths("b-xpath",4)).click()
        time.sleep(2)
        
    if s=="username":
           
        #click sing in button
        driver.find_element(By.XPATH,xpaths("b-xpath",0)).click()
        time.sleep(5)
        
        #write username
        driver.find_element(By.XPATH,xpaths("b-xpath",5)).send_keys(usrn)
        time.sleep(0.3)
        
        #write password 
        driver.find_element(By.XPATH,xpaths("b-xpath",6)).send_keys(passw)
        time.sleep(0.3)
        
        #click sing in button
        driver.find_element(By.XPATH,xpaths("b-xpath",7)).click()
        time.sleep(8)
    
        print("Logged in with using username & password")
        
    #using sessionid to bypass login progress
    else:

        #set local storage key and value
        driver.execute_script(f"localStorage.setItem('BSKY_STORAGE', '{key}');")
        driver.refresh()
        time.sleep(5)
        print("Logged in with using sessionid")


#share post (with pic or without)
def share_post(text,photo_url="none"):
    
    #share post button click
    driver.find_element(By.XPATH,xpaths("b-xpath",8)).click()
    time.sleep(6.5)

    #if you choose photo+text mode active this section (this section is not working well)
    if photo_url!="none":
        
        #open drop img section
        driver.find_element(By.XPATH,xpaths("b-xpath",9)).click()
        time.sleep(1)

        #upload img Keys.CONTROL + 'v'
        #driver.find_element(By.XPATH,xpaths("b-xpath",11)).send_keys(Keys.CONTROL + 'v')
        
        #upload img
        driver.find_element(By.XPATH,xpaths("b-xpath",10)).send_keys(photo_url)
        time.sleep(2)
        

    #write text
    driver.find_element(By.XPATH,xpaths("b-xpath",11)).send_keys(text)
    time.sleep(1)
    
    #click share button
    driver.find_element(By.XPATH,xpaths("b-xpath",12)).click()
    time.sleep(9)
    
    print("Post Shared")
