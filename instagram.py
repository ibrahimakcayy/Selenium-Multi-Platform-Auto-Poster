from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

#useless
def cont():
    return "ibrahim-instagram.py"


#get driver from main page
def drivers(driv):
    
    global driver
    driver=driv


#open url and max window
def openurl(url, opt="none"): 
    #Headless option (it is background process)
    options = webdriver.ChromeOptions()
    #headless option
    if opt=="headless":
        print("Headless mode activated")
        options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    
    driver.get(url)
    driver.set_window_size(1300, 650)
    
    #wait until email input is displayed
    wait = WebDriverWait(driver, timeout=2)
    wait.until(lambda _ : driver.find_element(By.CSS_SELECTOR, '[name="email"]').is_displayed())
    print("Webpage opened")


#login instagram
def login(s="usermane",usern="username",passw="password",key="sessionid"):
    
    if s=="username":
        #write username
        driver.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys(usern)
        
        #write password
        driver.find_element(By.CSS_SELECTOR, '[name="pass"]').send_keys(passw)
    
        #click login button
        driver.find_element(By.CSS_SELECTOR, '[id="login_form"] [role="button"] [role="none"]').click()
        
        
        print("Logged in with using username & password")
        
    #using sessionid to bypass login progress
    else:

        #set cookie
        driver.add_cookie({"name": "sessionid", "value": key})

        print("Logged in with using sessionid")
        
    #click notification decline
    #driver.find_element(By.CSS_SELECTOR,'[role=dialog] button:nth-child(2)').click()
    #time.sleep(2)
    
    driver.get(f"https://www.instagram.com/{usern}/")


#share photo in instagram wait options in not working on instagram (bot error) idk why
def share_photo(text,photo_url,usern):
    
    print("Start Sharing")

    #open create popup
    wait = WebDriverWait(driver, timeout=10)
    wait.until(lambda _ : driver.find_element(By.CSS_SELECTOR, '[data-visualcompletion="ignore-dynamic"] > div > div > div:nth-child(2) > div > div:nth-child(6)').is_displayed())
    driver.find_element(By.CSS_SELECTOR, '[data-visualcompletion="ignore-dynamic"] > div > div > div:nth-child(2) > div > div:nth-child(6)').click()
    
    #upload photo
    #wait.until(lambda _ : driver.find_element(By.CSS_SELECTOR, 'svg[viewBox="0 0 97.6 77.3"]').is_displayed())
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, '[role="presentation"] input[type="file"]').send_keys(photo_url)

    
    #share action
    #wait.until(lambda _ : driver.find_element(By.CSS_SELECTOR, 'section > div > div > div > div:nth-child(3) > button').is_displayed())
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'section > div > div > div > div:nth-child(3) > button').click()

    
    #write caption
    #wait.until(lambda _ : driver.find_element(By.CSS_SELECTOR, 'textarea').is_displayed())
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'textarea').send_keys(text)
    
    #share action
    #wait.until(lambda _ : driver.find_element(By.CSS_SELECTOR, 'section > div > div > div > div:nth-child(3) > button').is_displayed())
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'section > div > div > div > div:nth-child(3) > button').click()

    print("Post Shared")

    #open profile
    driver.get(f"https://www.instagram.com/{usern}/")
