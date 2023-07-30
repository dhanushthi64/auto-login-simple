# Used to import the webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# Get the path of chromedriver which you have install


def startBot(username, password, url):
    path = "C:\\Users\\User\\Downloads\\chromedriver-win64\\chromedriver"

    # giving the path of chromedriver to selenium webdriver
    driver = webdriver.Chrome(path)

    # opening the website in chrome.
    driver.get(url)

    # find the id or name or class of
    # username by inspecting on username input
    driver.find_element(By.__name__,
                        "username").send_keys(username)

    # find the password by inspecting on password input
    driver.find_element(By.__name__,
                        "password").send_keys(password)

    # click on submit
    login_button = driver.find_element(
        By.XPATH, "//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/span/button")
    login_button.click()


# Driver Code
# Enter below your login credentials
username = "dhanush_thil"
password = "13579135dha"
# URL of the login page of site
# which you want to automate login.
url = "https://www.instagram.com/accounts/edit/"

# Call the function
startBot(username, password, url)
