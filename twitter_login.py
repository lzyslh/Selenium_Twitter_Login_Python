from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


Twitter_URL = "https://www.twitter.com/"
driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver, 10)



driver.get(Twitter_URL)
sleep(1)   



def TwitterSignInSequence(twitter_user_email, twitter_username, twitter_password):  
    #Getting to the sign in page.                                              
    sign_in = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
    sign_in.click()


    ############################
    #Locating the email text field, and sending user email.
    sleep(2)                                                   
    username = wait.until(EC.visibility_of_element_located((By.NAME, "text")))
    username.send_keys(twitter_user_email)

    #Locating the Next button, and performing a click event.
    sleep(2)  
    next_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0'")))
    ActionChains(driver).move_to_element(next_button).click().perform()



    ############################
    #This block is when Twitter detects a suspicious login activity and asks for username/phone.
    sleep(2) 
    try:
        #Locating the username/phone field and sending the username.
        #The code send only the username, maybe later I'll add a posibilty to send phone as well.
        usercheck_span = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span[class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0']")))                                                 
        if(usercheck_span):
            usercheck = wait.until(EC.visibility_of_element_located((By.NAME, "text")))
            usercheck.send_keys(twitter_username)

        #Locating the Next button, and performing a click event.
        sleep(2)  
        next_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0'")))
        ActionChains(driver).move_to_element(next_button).click().perform()

    except Exception as e:
        print(e)
        




    ############################
    #Locating the password text field, and sending the password.
    sleep(2)                                                   
    password_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "Input[type='password']")))
    password_box.send_keys(twitter_password)
    #Locating the log in button, and performing a click event.
    sleep(2)  
    next_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0'")))
    ActionChains(driver).move_to_element(next_button).click().perform()


   





if __name__ == '__main__':

    twitter_user_email = "myTwitterEmail@domain.com" #Enter the email you use to login to Twitter
    twitter_username = "myTwitterUsername" #Enter your twitter username without the '@'
    twitter_password = "myTwitterPassword" #Enter you twitter account's password

    TwitterSignInSequence(twitter_user_email, twitter_username, twitter_password)

     #you're logged in, do as you please as long as it's not illegal.
