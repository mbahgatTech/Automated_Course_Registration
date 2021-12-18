from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import threading
import time

# take input of account information and login if user didn't login in window already
def takeAccInfo(browser): 
    time.sleep(2)
    print("Logging information needed:")
    userName = input("Enter your UofG username: ")
    password = input("Enter password: ")

    browser.find_element_by_id("UserName").send_keys(userName)
    browser.find_element_by_id("Password").send_keys(password)
    browser.find_element_by_id("login-button").click()

def main ():
    # open link in a new chrome window 
    browser  = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("https://colleague-ss.uoguelph.ca/Student/Planning/DegreePlans")
    browser.implicitly_wait(100000000000)

    # prompt user for account info, user can choose not to respond and manually sign in
    # through the browser window
    try: 
        threading.Thread(target=takeAccInfo, args=[browser]).start()
    except Exception as inputErr:
        print(inputErr)
    
    time.sleep(2)
    button = "schedule-next-term"
    i = 0

    # infinitely attempt registering in the planned courses for the next semester
    # ignores any errors thrown by the website like full sections and keeps attempting
    # registration till courses are registered. Infinite loop of refreshing after succesful
    # registration till program terminates.
    while 1:
        try:
            i = i + 1
            print("Registration Attempt: #" + str(i))

            browser.find_element_by_id(button).click()
            browser.find_element_by_id("register-button").click()
            time.sleep(5)
            browser.refresh()
            time.sleep(1)
        
        except Exception as err:
            browser.refresh()
            time.sleep(1)
            print(err)
    
main()