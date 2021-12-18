from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import time



def main ():
    browser  = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("https://colleague-ss.uoguelph.ca/Student/Planning/DegreePlans")
    browser.implicitly_wait(100000000000)
    
    
    userName = ""
    password = ""

    browser.find_element_by_id("UserName").send_keys(userName)
    browser.find_element_by_id("Password").send_keys(password)
    browser.find_element_by_id("login-button").click()
    
    time.sleep(2)
    button = "schedule-next-term"
    
    while 1:
        try:
            browser.find_element_by_id(button).click()
            browser.find_element_by_id("register-button").click()
            time.sleep(6)
            browser.refresh()
            time.sleep(1)
            print("Hello\n")
        
        except Exception as err:
            browser.refresh()
            time.sleep(1)
            print(err)
            print("\n")
    
main()