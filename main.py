#import all libraries
import twitter
import instagram
import facebook
import threads
import bluesky
import time
from selenium import webdriver as web


#import check
print(instagram.cont(),twitter.cont(),facebook.cont(),threads.cont(),bluesky.cont(),"\n")
driver = web.Chrome()
time.sleep(5)

#set all integer to 0
twtrlogged=0
instalogged=0
facelogged=0
thrdlogged=0
bskylogged=0


#counter function
def count():
    
    #open file and add 1
    f=open("count.txt","r")
    accnt=list(map(str,f.read().split()))
    accnt=int(accnt[0])
    f.close()
    fi=open("count.txt","w")
    fi.write(str(accnt+1))
    fi.close
    return accnt


#secrets.txt file inculude username and password
def secrets(check,check1):

    #open file
    f=open("secrets.txt","r")
    accnt=list(f.read().split("\n"))
    f.close()

    #set all username[1], password[2], sessionid[3], other[4](bluesky has host facebook has 2nd sessionid)
    insta=accnt[0].split(" ")
    twtr=accnt[1].split(" ")
    face=accnt[2].split(" ")
    thrd=accnt[3].split(" ")
    bsky=accnt[4].split(" ")

    if check=="insta":
    
        return(insta[check1])
    
    elif check=="twtr":

        return(twtr[check1])

    elif check=="face":

        return(face[check1])
    
    elif check=="thrd":

        return(thrd[check1])
    
    elif check=="bsky":

        return(bsky[check1])
   
    
#main activity
while True:
    
    try:
        
        #select platform
        choose =input("Twitter(x/t/twitter) || Instagram(i/instagram) || Facebook(f/facebook) || Threads(t/threads) || Bluesky(b/bluesky) || Quit(q/quit): ")
 
        if choose.lower()=="twitter" or choose.lower()=="x" or choose.lower()=="t":
            
            #write caption of post
            caption=input("Write caption: ")
            
            #select tweet mode
            post_mode=input("Normal(n/normal) || With Photo(p/photo): ")

            #set url none for text mode
            img_url="none"
            
            #if select photo mode this section will be activated
            if post_mode.lower()=="photo" or post_mode.lower()=="p":
                
                #enter photo url
                img_url=input("Enter photo url: ")
                
            #if already logged in this will be activated
            if twtrlogged:

                #open twitter
                twitter.openurl("https://x.com/home")
                print("Already logged in")
                    
            else:

                #open chromedriver
                twitter.drivers(driver)
                    
                #open twitter
                twitter.openurl("https://x.com/i/flow/login")
                time.sleep(8)

                #login twitter
                twitter.login("username",secrets("twtr", 1),secrets("twtr", 2),secrets("twtr", 3))

                #login check set 1
                twtrlogged=1

            #share tweet
            time.sleep(15)
            twitter.openurl("https://x.com/home")
            time.sleep(3)
            twitter.share_tweet(caption+str(count()),img_url)
            
        elif choose.lower()=="instagram" or choose.lower()=="i":

            #write caption of post
            caption=input("Write caption: ")
            
            #enter photo url
            img_url=input("Enter photo url: ")

            #if already logged in this will be activated
            if instalogged:

                #open instagram
                instagram.openurl("https://www.instagram.com/")
                print("Already logged in")
                
            else:
                
                #open chromedriver
                instagram.drivers(driver)

                #open instagram
                instagram.openurl("https://www.instagram.com/")
                time.sleep(8)

                #login instagram
                instagram.login("username",secrets("insta", 1),secrets("insta", 2),secrets("insta", 3))

                #login check set 1
                instalogged=1

            #share intagram post
            time.sleep(8)
            instagram.share_photo(caption+str(count()),img_url,secrets("insta", 1))
            
        elif choose.lower()=="facebook" or choose.lower()=="f":
        
          #write caption of post
          caption=input("Write caption: ")
        
          #select post mode
          post_mode=input("Normal(n/normal) || With Photo(p/photo): ")
        
          #set url none for text mode
          img_url="none"
        
          #if select photo mode this will be activated
          if post_mode.lower()=="photo" or post_mode.lower()=="p":
        
              #enter photo url
              img_url=input("Enter photo url: ")
        
          #if already logged in this will be activated
          if facelogged:
        
              #open facebook
              facebook.openurl("https://facebook.com")
              print("Already logged in")
                  
          else:
        
              #open chromedriver
              facebook.drivers(driver)
        
              #open facebook
              facebook.openurl("https://facebook.com")
              time.sleep(8)
        
              #login facebook
              facebook.login("usernamea",secrets("face", 1),secrets("face", 2),secrets("face", 3),secrets("face", 4))
                  
              #login check set 1
              facelogged=1
        
          #share facebook post
          time.sleep(10)   
          facebook.share_post(caption+str(count()),img_url)      
                       
        elif choose.lower()=="threads" or choose.lower()=="t":
            #this section is closed
            print("This section is closed")
            """
            #write caption of post
            caption=input("Write caption: ")
            
            #select threads mode
            post_mode=input("Normal(n/normal) || With Photo(p/photo): ")

            #if select normal mode this will be activated
            if post_mode.lower()=="normal" or post_mode.lower()=="n":
                
                #if already logged in this will be activated
                if thrdlogged:

                    #open threads
                    threads.openurl("https://www.threads.net/")
                    print("Already logged in")
                    
                else:

                    #open chromedriver
                    threads.drivers(driver)
                    
                    #open threads
                    threads.openurl("https://www.threads.net/login")
                    time.sleep(10)

                    #login threads
                    threads.login(secrets("thrd", 1),secrets("thrd", 2))

                    #login check set 1
                    thrdlogged=1

                #share normal thread
                time.sleep(15)
                threads.share_thread(caption+str(count()))

            #if select photo mode this will be activated
            elif post_mode.lower()=="photo" or post_mode.lower()=="p":

                #enter photo url
                img_url=input("Enter photo url: ")

                #if already logged in this will be activated
                if thrdlogged:

                    #open threads
                    threads.openurl("https://www.threads.net/")
                    print("Already logged in")
                    
                else:

                    #open chromedriver
                    threads.drivers(driver)
                    
                    #open threads
                    threads.openurl("https://www.threads.net/login")
                    time.sleep(8)

                    #login threads
                    threads.login(secrets("thrd", 1),secrets("thrd", 2))

                    #login check set 1
                    thrdlogged=1

                #share thread with photo
                time.sleep(15)
                threads.share_thread(caption+str(count()),img_url)
                
            else:
                
               print("Invalid selection")
            """
            
        elif choose.lower()=="bluesky" or choose.lower()=="b":

          #write caption of post
          caption=input("Write caption: ")

          #select post mode
          post_mode=input("Normal(n/normal) || With Photo(p/photo): ")

          #set url none for text mode
          img_url="none"

          #if select photo mode this will be activated
          if post_mode.lower()=="photo" or post_mode.lower()=="p":

              #enter photo url
              img_url=input("Enter photo url: ")

          #if already logged in this will be activated
          if bskylogged:

              #open bluesky
              bluesky.openurl("https://bsky.app/")
              print("Already logged in")
                  
          else:

              #open chromedriver
              bluesky.drivers(driver)

              #open bluesky
              bluesky.openurl("https://bsky.app/")
              time.sleep(8)

              #login bluesky
              bluesky.login("username",secrets("bsky", 4),secrets("bsky", 1),secrets("bsky", 2),secrets("bsky", 3))
                  
              #login check set 1
              bskylogged=1

          #share bluesky post
          time.sleep(10)   
          bluesky.share_post(caption+str(count()),img_url)      
            
        elif choose.lower()=="quit" or choose.lower()=="q":

            #close chromedriver
            driver.close()
            
            #exterminate loop
            break
        
        else:
            
            print("Invalid selection try again")
            
    except Exception as e:
        
        print(e)

print("Closed")
